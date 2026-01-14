unit uGerenteAutomacaoReceitaBX;

interface

uses
  System.SysUtils, System.Classes, System.IOUtils,
  mORMot, SynCommons, Messages, Forms, Windows, uConfiguracao, uConexaoLocal, uConexaoTaxas, uConexaoServidores,
  uConexaoDadosMaquina, uConfiguracaoIni, uInformacaoGeracaoBanco, intfAutomacaoReceitaBX;

type
  TClienteAutomacaoReceitaBX = class
    public
      procedure CarregarVersaoDoServidor(const ACaminhoPlanilha: string);

  end;

implementation

uses
  uConexaoAutomacaoReceitaBX;


{ TClienteAutomacaoReceitaBX }

procedure TClienteAutomacaoReceitaBX.CarregarVersaoDoServidor(const ACaminhoPlanilha: string);
var
  I : IAutomacaoReceitaBX;
  S : RawByteString;
  FS : TFileStream;
  Caminho : string;

begin

  if (ACaminhoPlanilha <> '') and TFile.Exists(ACaminhoPlanilha) then
    Caminho := ACaminhoPlanilha

  else
    Caminho := 'C:\Users\patrick\Desktop\Automacoes\Teste\Procuracoes - Certificados.xlsx';

  if not TFile.Exists(Caminho) then
    raise Exception.Create('Arquivo não encontrado');


  FS := TFileStream.Create(Caminho, fmOpenRead or fmShareDenyNone);

  try
    S := StreamToRawByteString(FS);
  finally
    FS.Free;
  end;

  if not ConexaoAutomacaoReceitaBX.Conexao.Services.Resolve(IAutomacaoReceitaBX, I) then
    raise Exception.Create('Não foi possivel conectar com o servidor IAutomacaoReceitaBX');


  I.ImportarDadosDaPlanilhaSubvencao(S);

  I.ControleParaPendentes;

  I.PegarProximaParadaPraBaixar;


end;
end.
