unit implAutomacaoReceitaBX;

interface
uses
  mORMot, SynCommons, intfAutomacaoReceitaBX, System.Generics.Collections, SysUtils, uImportacaoExportacaoExcelVO, System.RegularExpressions,
  uModeloAutomacaoReceitaBX, classes, mORMotDB, SynTable;


type
  TServiceAutomacaoReceitaBX = class(TInjectableObjectRest, IAutomacaoReceitaBX)

  public
    procedure ImportarDadosDaPlanilhaSubvencao(const aArquivo : RawByteString);
    function ExtrairCNPJ(const Texto: string): string;
    function ExtrairNome(const Texto: string): string;
    function ExisteControle(const ACNPJ, ATipoStr, APeriodo, ANome, ACertificadoProcuracao: string): Boolean;
    procedure ControleParaCNPJ(const ACNPJ, ANome, ACertificadoProcuracao: string; const ATipos: TTiposSped);
    procedure ControleParaPendentes;
    function PegarProximaParadaPraBaixar : TRetornoPegarProximaParadaPraBaixarObjArray;
    function FinalizarProcesso(const aCNPJ, aPeriodo, aTipo : String) : Boolean;
    function MoverArquivos: TMoverArquivosArray;


  private
    fLista: TObjectList<TRetornoPegarProximasParadaPraBaixar>;

  end;


implementation


uses

  System.IoUtils, System.DateUtils;


//Finalidade: mapeiar, a qual ajuda na consistência do banco
function TipoSpedToString(ATipo: TTipoSpedBaixar): string;
begin
  case ATipo of
    tsbEFDICMS: Result := 'EFDICMS' ;
    esbEFDContribuicoes: Result := 'EFDContribuicoes';
    tsbECF: Result := 'ECF';
    tsbECD: Result := 'ECD';
  end;
end;

{ TServiceAutomacaoReceitaBX }



//Finalidade: Gerar (caso não exista) a grade de controle em TControlePlanilha para um CNPJ. É a mesma ideia de criar checkpoints para a automação saber onde parou a ideia de baixar/processar os arquivos
procedure TServiceAutomacaoReceitaBX.ControleParaCNPJ(const ACNPJ, ANome, ACertificadoProcuracao: string;
  const ATipos: TTiposSped);   // Preenche TControlePlanilha

var
  LTipo: TTipoSpedBaixar;
  LPeriodoTipo: TPeriodoSped;
  LAtual, LFinal, LInicio : TDateTime;
  LPeriodoStr : string;
  LTipoStr : string;
  LControle : TControlePlanilha;
begin
  LInicio := IncMonth(Now, -60);
  LFinal := Now;


  for LTipo in ATipos do
  begin
    LPeriodoTipo := CPeriodoDeCadaTipo[LTipo];
    LTipoStr := TipoSpedToString(LTipo);

    LAtual := LInicio;

   // LAtual := IncMonth(Now, -60);

    while LAtual < LFinal do
    begin
      if LPeriodoTipo = tpsMensal then
        LPeriodoStr := FormatDateTime('yyyymm', LAtual)
      else
        LPeriodoStr := FormatDateTime('yyyy', LAtual);

      if not ExisteControle(ACNPJ, LTipoStr, LPeriodoStr, ANome, ACertificadoProcuracao) then
      begin
        LControle := TControlePlanilha.Create;
        try
          LControle.CNPJ := ACNPJ;
          LControle.DATA := LPeriodoStr;
          LControle.TIPO := LTipoStr;
          LControle.DataProcessamento := 0;
          LControle.NOME := ANome;
          LControle.CertificadoProcuracao := ACertificadoProcuracao;

          fServer.Add(LControle, true);
        finally
          LControle.Free;

        end;
      end;

      if LPeriodoTipo = tpsMensal then
        LAtual := IncMonth(LAtual, 1)
      else
        LAtual := IncYear(LAtual, 1);

    end;
  end;


end;

//Finalidade: Consumir TPlanilhaMensal que ainda não foi processada, ou seja, DataProcessamento = 0, daí para cada item: extraiCNPJ, verifica o tipo do certificado, gera controle (ControleParaCNPJ) e marca o item da planilha como processado e atualiza no banco
procedure TServiceAutomacaoReceitaBX.ControleParaPendentes;
var
  LItem: TPlanilhaMensal;
  LCNPJ, LNOME, LTipoArquivo: string;
  LCNPJs: TDictionary<string, string>;
  LTipos: TTiposSped;
begin
  LTipos := [tsbEFDICMS, esbEFDContribuicoes, tsbECF, tsbECD];

  LItem := TPlanilhaMensal.CreateAndFillPrepare(fServer, 'DataProcessamento = ?', [DateTimeToSQL(0)]);

    try
      while LItem.FillOne do
      begin
        LCNPJ := ExtrairCNPJ(LItem.NomeEmpresa);
        LNOME := ExtrairNome(LItem.NomeEmpresa);

        if (LCNPJ <> '') and (LNOME <> '') then
        begin

         LTipoArquivo := trim(LItem.TipoCertificado);

         if SameText(LTipoArquivo, 'Certificado digital') then
            LTipoArquivo := 'CERTIFICADO DIGITAL'

         else if SameText(LTipoArquivo, 'Procuração eletrônica') then
          LTipoArquivo := 'PROCURAÇÃO ELETRÔNICA'

          else
            LTipoArquivo := '';

            if LTipoArquivo <> '' then

            begin
              try
                ControleParaCNPJ(LCNPJ, LNOME, LTipoArquivo, LTipos);
                LItem.DataProcessamento := Now;
                fServer.Update(LItem);
              except
                raise;

              end;
            end;
        end;
      end;

    finally
      LItem.Free;
    end;
  end;


//Finalidade: Verificar se já existe no banco um registro TControlePlanilha para a combinação (evita duplicação)
function TServiceAutomacaoReceitaBX.ExisteControle(const ACNPJ, ATipoStr,
  APeriodo, ANome, ACertificadoProcuracao: string): Boolean;
  var
    LID: int64;
begin
  LID := StrToInt64Def(fServer.OneFieldValue(
      TControlePlanilha,
      'ID',
      'CNPJ = ? AND TIPO = ? AND DATA = ? AND NOME = ? AND CertificadoProcuracao = ?',
      [ACNPJ, ATipoStr, APeriodo, StringToUTF8(ANome), StringToUTF8(ACertificadoProcuracao)]),
      0);

      Result := LID > 0;

end;

//Finalidade: Como diz o nome da função, a ideia é extrair o cnpj da string que vem na planilha (OBS: Extrai com o formato cnpj, ou seja, xx.xxx.xxx/000x-xx)
function TServiceAutomacaoReceitaBX.ExtrairCNPJ(const Texto: string): string;
var
  match: System.RegularExpressions.TMatch;
begin
  Result := '';
  Match := TRegex.Match(Texto, '(\d{2}\.\d{3}\.\d{3}\/\d{4}\-\d{2})');
  if Match.Success then
    Result := Match.Value;
end;

//Finalidade> Como diz o nome da função, a ideia é extrair o nome da string que vem na planilha
function TServiceAutomacaoReceitaBX.ExtrairNome(const Texto: string): string;
var
  p: integer;
begin
  p := pos('-', Texto); //Função pos() tem como ideia a mesma lógica de um Substr(x, y, z) do SQLite
  Result := Copy(Texto, 1, p - 1);
  //OBS: Caso queira limitar a quantidade de caracteres basta usar a função copy() sem a função pos()
  //Lembrando que, copy(string, onde_comeca, quantos_caracteres_copiado)
end;

function TServiceAutomacaoReceitaBX.FinalizarProcesso(const aCNPJ, aPeriodo,
  aTipo: String): Boolean;
begin

  var cp := TControlePlanilha.Create(fServer, 'cnpj = ? and data = ? and tipo = ?', [aCNPJ, aPeriodo, aTipo]);
  try
    result := False;
    if cp.ID > 0 then
    begin
      cp.DataProcessamento := Now;
      result := fServer.Update(cp);
    end;
  finally
    cp.Free;
  end;
end;



//Finalidade: Receber a planliha (em bytes), manter temporariamente em disco, daí importa os registros para TPlanilhaMensal e grava os itens no banco marcando como "pendente"
procedure TServiceAutomacaoReceitaBX.ImportarDadosDaPlanilhaSubvencao(
  const aArquivo: RawByteString);
  var
    LItem: TPlanilhaMensal;
    LControle: TControlePlanilha;

begin
  if length(aArquivo) = 0 then
    exit;

  var stream := RawByteStringToStream(aArquivo);
  try
    var fileName := TPath.GetTempFileName;
    var fs := TFileStream.Create(filename, fmCreate);
    try
      fs.CopyFrom(stream);
    finally
      fs.Free;
    end;

  var imp := TImportacaoExportacaoExcelVO<TPlanilhaMensal>.Create(nil);

  try
    imp.ImportarExcel(fileName, '');

    for LItem in imp.ListaImportada do
    begin
      LItem.DataImportacao := Now;
      LItem.DataProcessamento := 0;

      fServer.Add(LItem, true);
    end;
  finally
    imp.Free;
  end;

  finally
      stream.Free;
  end;

end;


//Finalidade: Montar uma lista de "proxima parada" para a automação, logo, agrega registros pendentes (TControlePlanilha com DataProcessamento = 0), daí envia 1 item, sendo ele um intervalo de tempo
function TServiceAutomacaoReceitaBX.PegarProximaParadaPraBaixar: TRetornoPegarProximaParadaPraBaixarObjArray;
var
  item : TRetornoPegarProximasParadaPraBaixar;
  dataConversao, s: RawUTF8;
  dic: TDictionary<RawUTF8, TRetornoPegarProximasParadaPraBaixar>;
  r : variant;
  LNome: string;

begin
  SetLength(Result, 0);
  var cp := TControlePlanilha.CreateAndFillPrepare(fServer, 'DataProcessamento = ? ', [DateTimeToSQL(0)]);
  dic := TDictionary<RawUTF8, TRetornoPegarProximasParadaPraBaixar>.Create;

  try

    while cp.FillOne do
    begin
      dataConversao := StringToUTF8(cp.DATA);

      s := FormatUTF8('%|%|%|%', [cp.CNPJ, cp.TIPO, cp.NOME, cp.CertificadoProcuracao]);

      if not dic.TryGetValue(s, item) then
      begin
        item := TRetornoPegarProximasParadaPraBaixar.Create;
        item.Nome := cp.NOME;
        item.Cnpj := cp.CNPJ;
        item.Tipo := cp.TIPO;
        item.CertificadoProcuracao := cp.CertificadoProcuracao;
        item.IntervaloData(dataConversao);

        dic.Add(s, item);
        ObjArrayAdd(Result, item);

      end

      else
        begin
          item.IntervaloData(dataConversao);
        end;

    end;

  finally
    cp.Free;
    dic.Free;
  end;

end;
end.
