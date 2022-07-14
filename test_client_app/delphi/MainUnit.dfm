object MainFrm: TMainFrm
  Left = 0
  Top = 0
  Caption = 'Flask-RESTX API Demo'
  ClientHeight = 586
  ClientWidth = 885
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'Tahoma'
  Font.Style = []
  OldCreateOrder = False
  PixelsPerInch = 96
  TextHeight = 13
  object Label1: TLabel
    Left = 16
    Top = 20
    Width = 45
    Height = 13
    Caption = 'API URL'
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clWindowText
    Font.Height = -11
    Font.Name = 'Tahoma'
    Font.Style = [fsBold]
    ParentFont = False
  end
  object Label3: TLabel
    Left = 16
    Top = 360
    Width = 43
    Height = 13
    Caption = 'Wiki Url'
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clWindowText
    Font.Height = -11
    Font.Name = 'Tahoma'
    Font.Style = [fsBold]
    ParentFont = False
  end
  object Label2: TLabel
    Left = 16
    Top = 330
    Width = 85
    Height = 13
    Caption = 'Common Name'
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clWindowText
    Font.Height = -11
    Font.Name = 'Tahoma'
    Font.Style = [fsBold]
    ParentFont = False
  end
  object Label4: TLabel
    Left = 16
    Top = 296
    Width = 86
    Height = 13
    Caption = 'Scientific Name'
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clWindowText
    Font.Height = -11
    Font.Name = 'Tahoma'
    Font.Style = [fsBold]
    ParentFont = False
  end
  object APIURL: TEdit
    Left = 80
    Top = 16
    Width = 785
    Height = 21
    TabOrder = 0
    Text = 'http://127.0.0.1:5000/api/v1/trees'
  end
  object GetBtn: TButton
    Left = 16
    Top = 72
    Width = 75
    Height = 25
    Caption = 'Get'
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clWindowText
    Font.Height = -11
    Font.Name = 'Tahoma'
    Font.Style = [fsBold]
    ParentFont = False
    TabOrder = 1
    OnClick = GetBtnClick
  end
  object GetResponse: TMemo
    Left = 16
    Top = 104
    Width = 849
    Height = 161
    ScrollBars = ssBoth
    TabOrder = 2
  end
  object PostBtn: TButton
    Left = 16
    Top = 400
    Width = 75
    Height = 25
    Caption = 'Post'
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clWindowText
    Font.Height = -11
    Font.Name = 'Tahoma'
    Font.Style = [fsBold]
    ParentFont = False
    TabOrder = 3
    OnClick = PostBtnClick
  end
  object scientific_name: TEdit
    Left = 120
    Top = 293
    Width = 489
    Height = 21
    TabOrder = 4
  end
  object common_name: TEdit
    Left = 120
    Top = 327
    Width = 489
    Height = 21
    TabOrder = 5
  end
  object wiki_url: TEdit
    Left = 120
    Top = 360
    Width = 489
    Height = 21
    TabOrder = 6
  end
  object PostResponse: TMemo
    Left = 16
    Top = 433
    Width = 849
    Height = 136
    ScrollBars = ssBoth
    TabOrder = 7
  end
  object NetHTTPClient: TNetHTTPClient
    UserAgent = 'Embarcadero URI Client/1.0'
    Left = 160
    Top = 48
  end
  object NetHTTPRequest: TNetHTTPRequest
    Client = NetHTTPClient
    Left = 264
    Top = 48
  end
end
