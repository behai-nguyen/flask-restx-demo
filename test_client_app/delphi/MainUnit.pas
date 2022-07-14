unit MainUnit;

interface

uses
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants, System.Classes, Vcl.Graphics,
  Vcl.Controls, Vcl.Forms, Vcl.Dialogs, Vcl.StdCtrls, System.Net.URLClient,
  System.Net.HttpClient, System.Net.HttpClientComponent;

type
  TMainFrm = class(TForm)
    Label1: TLabel;
    APIURL: TEdit;
    GetBtn: TButton;
    GetResponse: TMemo;
    PostBtn: TButton;
    scientific_name: TEdit;
    common_name: TEdit;
    wiki_url: TEdit;
    Label3: TLabel;
    Label2: TLabel;
    Label4: TLabel;
    PostResponse: TMemo;
    NetHTTPClient: TNetHTTPClient;
    NetHTTPRequest: TNetHTTPRequest;
    procedure GetBtnClick(Sender: TObject);
    procedure PostBtnClick(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  MainFrm: TMainFrm;

implementation
uses System.Net.Mime
     ;

{$R *.dfm}

procedure TMainFrm.GetBtnClick(Sender: TObject);
var
  ResponseContent: TMemoryStream;
begin
  ResponseContent := TMemoryStream.Create();
  try
    NetHTTPRequest.Get( APIURL.Text, ResponseContent );
    GetResponse.Lines.LoadFromStream( ResponseContent );
  finally
    FreeAndNil( ResponseContent );
  end;
end;

procedure TMainFrm.PostBtnClick(Sender: TObject);
var
  Source: TMultipartFormData;
  ResponseContent: TMemoryStream;
begin
  Source := TMultipartFormData.Create();
  try
    Source.AddField( 'scientific_name', scientific_name.Text );
    Source.AddField( 'common_name', common_name.Text );
    Source.AddField( 'wiki_url', wiki_url.Text );

    ResponseContent := TMemoryStream.Create();
    try
      NetHTTPRequest.Post( APIURL.Text, Source, ResponseContent );
      PostResponse.Lines.LoadFromStream( ResponseContent );
    finally
      FreeAndNil( ResponseContent );
    end;
  finally
    FreeAndNil( Source );
  end;
end;

end.
