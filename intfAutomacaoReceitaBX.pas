unit intfAutomacaoReceitaBX;

interface

 uses
  mORMot,
  SynCommons,
  uModeloAutomacaoReceitaBX;

type
  TTipoSpedBaixar = (tsbEFDICMS, esbEFDContribuicoes, tsbECF, tsbECD);
  TPeriodoSped = (tpsMensal, tpsAnual);
  TTiposSped = set of TTipoSpedBaixar;

const
  CPeriodoDeCadaTipo: array[TTipoSpedBaixar] of TPeriodoSped = (
  tpsMensal,   // ---> Referente a tsbEFDICMS
  tpsMensal,  // ---> ... tsbEFDContribuicoes
  tpsAnual,  // ----> ... tsbECF
  tpsAnual   // ----> ... tsbECD
  );

type
  TRetornoPegarProximasParadaPraBaixar = class(TSynPersistent)
  private
    fDataInicio: RawUTF8;
    fDataFinal: RawUTF8;
    fCnpj: RawUTF8;
    fTipo: RawUTF8;
    fCertificadoProcuracao: RawUTF8;
    fNome: RawUTF8;

    function PeriodoToOrd(const APeriodo: RawUTF8): Integer;

  public
    procedure IntervaloData(const APeriodo : RawUTF8);


  published
    property DataInicio: RawUTF8 read fDataInicio write fDataInicio;
    property DataFinal: RawUTF8 read FDataFinal write fDataFinal;
    property Cnpj: RawUTF8 read fCnpj write fCnpj;
    property Tipo: RawUTF8 read fTipo write fTipo;
    property CertificadoProcuracao: RawUTF8 read fCertificadoProcuracao write fCertificadoProcuracao;
    property Nome: RawUTF8 read fNome write fNome;

  end;
  TRetornoPegarProximaParadaPraBaixarObjArray = array of TRetornoPegarProximasParadaPraBaixar;


  IAutomacaoReceitaBX = interface(IInvokable)
  ['{D25A929D-5BCA-4F5C-8D7E-C4CF3DAD6EA4}']
    procedure ImportarDadosDaPlanilhaSubvencao(const aArquivo : RawByteString);
    procedure ControleParaPendentes;
    procedure ControleParaCNPJ(const ACNPJ, ANome, ACertificadoProcuracao: string; const ATipos: TTiposSped);
    function ExisteControle(const ACNPJ, ATipoStr, APeriodo, ANome, ACertificadoProcuracao: string): Boolean;
    function ExtrairCNPJ(const Texto: string): string;
    function PegarProximaParadaPraBaixar : TRetornoPegarProximaParadaPraBaixarObjArray;
    function FinalizarProcesso(const aCNPJ, aPeriodo, aTipo : String) : Boolean;

  end;


implementation

uses
  SysUtils;


procedure TRetornoPegarProximasParadaPraBaixar.IntervaloData(
  const APeriodo: RawUTF8);
var
  oNovo, oIni, oFim: Integer;
begin
  oNovo := PeriodoToOrd(APeriodo);
  if oNovo = 0 then
    Exit;

  if fDataInicio = '' then
  begin
    fDataInicio := APeriodo;
    fDataFinal  := APeriodo;
    Exit;
  end;

  if fDataFinal = '' then
    fDataFinal := fDataInicio;

  oIni := PeriodoToOrd(fDataInicio);
  oFim := PeriodoToOrd(fDataFinal);

  if (oIni = 0) or (oFim = 0) then
  begin
    fDataInicio := APeriodo;
    fDataFinal  := APeriodo;
    Exit;
  end;

  if oNovo < oIni then
    fDataInicio := APeriodo;

  if oNovo > oFim then
    fDataFinal := APeriodo;
end;

function TRetornoPegarProximasParadaPraBaixar.PeriodoToOrd(
  const APeriodo: RawUTF8): Integer;
var
  s: string;
  ano, mes: integer;
begin
  Result := 0;
  if APeriodo = '' then
    Exit;

  s := UTF8ToString(APeriodo);

  if length(s) = 4 then
    exit(StrToIntDef(s, 0));

  if length(s) = 6 then
  begin
    ano := StrToIntDef(Copy(s, 1, 4), 0);
    mes := StrToIntDef(Copy(s, 5, 2), 0);

    if (ano > 0) and (mes >= 1) and (mes <= 12) then
      exit(ano * 100 + mes);

  end;
end;



{ TRetornoPegarProximasParadaPraBaixar }


initialization
  TJSONSerializer.RegisterClassForJSON([TRetornoPegarProximasParadaPraBaixar]);
  TJSONSerializer.RegisterObjArrayForJSON(TypeInfo(TRetornoPegarProximaParadaPraBaixarObjArray), TRetornoPegarProximasParadaPraBaixar);
  TInterfaceFactory.RegisterInterfaces([TypeInfo(IAutomacaoReceitaBX)]);

end.

