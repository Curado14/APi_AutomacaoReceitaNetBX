unit uModeloAutomacaoReceitaBX;

interface

uses
  mORMOt, SynCommons, ComObj, Variants, System.Generics.Collections, uAtributosVoNovo; //uImportacaoExportacaoExcelVO;

type
  TPlanilhaMensal = class(TSQLRecord)
  private
    //fID: integer; ---> Chave Primaria (PK) declarada de forma implicita pelo mORMOt
    fNomeEmpresa: string;
    fTipoCertificado: string;
    fValidade: TDateTime;
    fStatus: string;
    fDataImportacao: TDateTime;
    fDataProcessamento: TDateTime;
  public
    class procedure InitializeTable(Server: TSQLRestServer; const FieldName: RawUTF8;
      Options: TSQLInitializeTableOptions); override;

  published
    [TInfoColuna('Nome da Empresa', 0)]
    property NomeEmpresa : string read fNomeEmpresa write fNomeEmpresa;
    [TInfoColuna('Tipo certificado digital/procuração eletrônica', 1)]
    property TipoCertificado : string read fTipoCertificado write fTipoCertificado;
    [TInfoColuna('Validade', 2, tcDataHora)]
    property Validade : TDateTime read fValidade write fValidade;
    [TInfoColuna('Status Cetificado', 3)]
    property Status: string read fStatus write fStatus;
    [TInfoColuna('Data de importação', 4, tcDataHora)]
    property DataImportacao: TDateTime read fDataImportacao write fDataImportacao;
    [TInfoColuna('Data de processamento', 5, tcDataHora)]
    property DataProcessamento: TDateTime read fDataProcessamento write fDataProcessamento;


  end;

  TControlePlanilha = class(TSQLRecord)
    private
      fCNPJ: string;
      fDATA: string;
      fTIPO: string;
      fDataProcessamento: TDateTime;
      fNOME: string;
      fCertificadoProcuracao: string;

    public
      class procedure InitializeTable(Server: TSQLRestServer; const FieldName: RawUTF8;
        Options: TSQLInitializeTableOptions); override;

    published

      [TInfoColuna('CNPJ do Cliente', 0)]
      property CNPJ: string read fCNPJ write fCNPJ;
      [TInfoColuna('Data de importação', 1)]
      property DATA: string read fData write fData;
      [TInfoColuna('Tipo do Arquivo', 2)]
      property TIPO: string read fTIPO write fTIPO;
      [TInfoColuna('Data de pro\cessamento', 3)]
      property DataProcessamento: TDateTime read fDataProcessamento write fDataProcessamento;
      [TInfoColuna('Nome da Empresa', 4)]
      property NOME: string read fNOME write fNOME;
      [TInfoColuna('Procuração ou Certificado', 5)]
      property CertificadoProcuracao: string read fCertificadoProcuracao write fCertificadoProcuracao;

  end;



implementation

function PegarModeloAutomacaoReceitaBX: TSQLModel;
begin
  result := TSQLModel.Create([TPlanilhaMensal, TControlePlanilha], 'automacao_receita_bx');
  result.SetCustomCollationForAll(sftUTF8Text, 'NOCASE');
  result.SetCustomCollationForAll(sftDateTime, 'NOCASE');

end;


{ TPlanilhaMensal }


class procedure TPlanilhaMensal.InitializeTable(Server: TSQLRestServer;
  const FieldName: RawUTF8; Options: TSQLInitializeTableOptions);
begin
  inherited;

end;

{ TControlePlanilha }

class procedure TControlePlanilha.InitializeTable(Server: TSQLRestServer;
  const FieldName: RawUTF8; Options: TSQLInitializeTableOptions);
begin
  inherited;

end;

end.










