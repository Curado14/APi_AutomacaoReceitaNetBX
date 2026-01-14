unit uServidorAutomacaoReceitaBX;

interface

uses
  mORMot, SynCommons, uServidorBase, mORMotSQLite3, mORMotHttpClient, mORMotHttpServer, StrUtils, SysUtils,
  SynLog, mORMotWrappers, intfAutomacaoReceitaBX, implAutomacaoReceitaBX, uModeloAutomacaoReceitaBX;

type
  TServidorAutomacaoReceitaBX = class(TServidorHTTP)
  protected
    procedure OnServiceCreateInstance(Sender: TServiceFactoryServer; Instance: TInterfacedObject); override;
    procedure PreencherListaServices; override;

    procedure CriarModelo; override;
    procedure CriarRestServer; override;


  end;


implementation


{ TServidorAutomacaoReceitaBX }

procedure TServidorAutomacaoReceitaBX.CriarModelo;
begin
  inherited;
  fModel := PegarModeloAutomacaoReceitaBX;

end;

procedure TServidorAutomacaoReceitaBX.CriarRestServer;
begin
  inherited;
  fRestServer := TSQLRestServerDB.Create(fModel, ExeVersion.ProgramFilePath+'dbficus-controle-planilha-SPED.db', false);

  AddToServerWrapperMethod(fRestServer,
  ['C:\Desenvolvimento\LibDelphi\mORMot\CrossPlatform\templates',
  'C:\Desenvolvimento\LibDelphi\mORMot\CrossPlatform\templates']);

  fRestServer.CreateMissingTables;
end;

procedure TServidorAutomacaoReceitaBX.OnServiceCreateInstance(
  Sender: TServiceFactoryServer; Instance: TInterfacedObject);
begin
  inherited;

end;

procedure TServidorAutomacaoReceitaBX.PreencherListaServices;
var
  serviceInfo: TServiceInfo;
begin
  serviceInfo := TServiceInfo.Create;
  serviceInfo.ServiceInterfaces := [IAutomacaoReceitaBX];
  serviceInfo.ServiceInstanceImplementation := sicShared;
  serviceInfo.ServiceImplementationClass := TServiceAutomacaoReceitaBX;
  fListaServices.Add(serviceInfo);
end;

end.
