# デイトラwebinar-2020-11月05日ファイル

## streamlitのインストール
pip install streamlit


## Youtubeの24時間以内に一定回数以上再生された動画情報を取得


### 1. グーグルスプレッドシートに書き込みするための準備

(参考) https://tanuhack.com/operate-spreadsheet/


・17行目の
credentials = ServiceAccountCredentials.from_json_keyfile_name('*******************************', scope)
のアスタリスクに取得したJSONファイル名を書き込む


・JSONファイルの中にあるメールアドレスを書き込みしたいスプレッドシートに共有しておく。

・書き込みしたいスプレッドシートには、
「検索結果」と「検索キーワード」という2つのシートを作っておく。
検索キーワードのシートの1列目に検索したいキーワード（複数可）を書き込む。

・21行目の
SPREADSHEET_KEY = '*************************************'
のアスタリスクに書き込みしたいスプレッドシートのアドレスバーからスプレッドシートキーを取得して書き込む。


### 2. Youtube API の取得
(参考) http://piyohiko.webcrow.jp/kids_tube/help/index.html

・27行目の
api_key = '**********************************'
のアスタリスクに取得したYoutube APIキーを記入


### 3. アプリの起動
streamlit run ファイル名
でアプリを起動させる。


## 時系列予測ライブラリのProphetを使って株価の予測


### 1. まずはProphetのインストール


### Windows
https://touch-sp.hatenablog.com/entry/2019/10/09/124145

### Mac
https://facebook.github.io/prophet/docs/installation.html




