# デイトラウェビナー2020-11月05日の解説

当日解説した流れをまとめました。
こちらを見ながらstreamlitで簡単にアプリを作る体験してみましょう！

## streamlitのページ
https://www.streamlit.io/

### Pythonのアプリの解説とstreamlitの位置付け
https://mm.tt/1679296151?t=URbLdlR6D4

### streamlitのAPIリファレンス（使い方一覧)
https://docs.streamlit.io/en/stable/api.html
(streamlitのコマンドが乗っています。)

### データフレームについての解説
https://docs.pyq.jp/python/pydata/pandas/dataframe.html

## 注意点
streamlitを使う際にはstreamlit run ファイル名.py
としてコマンドを打ち込むので、VSCodeやPyCharm推奨です。

## streamlitのインストール方法
コンソールにて、

```
pip install streamlit
```

と入力してEnterを押します。

## まずはstreamlitを体験してみよう
コンソールにて、

```
streamlit hello
```

と入力してEnterを押します。
すると、Exampleのアプリが起動します。

## streamlitのアプリの起動方法
コンソールにて、

```
streamlit run ファイル名.py
```

# Youtubeの24時間以内に一定回数以上再生された動画情報を取得

youtube-24.pyのプログラムを使っていきます。

Youtube APIにて、指定したキーワードでYoutube内を検索して、
24時間以内に1万回以上再生された動画をピックアップしてくれる
プログラムです。

まずは結果を書き込むためのグーグルスプレッドシートを準備していきましょう。

### 1. 結果をグーグルスプレッドシートに書き込みするための準備

(参考) https://tanuhack.com/operate-spreadsheet/
（こちらの手順でスプレッドシートへのアクセス情報などが書かれたJSONファイルを取得します。）

youtube-24.pyを見ながらやっていきます。

・youtube-24.pyの17行目の

```
credentials = ServiceAccountCredentials.from_json_keyfile_name('*******************************', scope)
```

のアスタリスクに取得したJSONファイル名を書き込む


・スプレッドシートのところで取得した、JSONファイルの中にある
メールアドレスを書き込みしたいスプレッドシートに共有しておく。

・JSONファイルはプログラムyoutube-24.pyと同じフォルダに置く。

・書き込みしたいスプレッドシートには、
「検索結果」と「検索キーワード」という名前の2つのシートを作っておく。

「検索キーワード」のシートの1列目に検索したいキーワード（複数可）を書き込む。

・youtube-24.pyの21行目の

```
SPREADSHEET_KEY = '*************************************'
```

のアスタリスクに書き込みしたいスプレッドシートのアドレスバーからスプレッドシートキーを取得して書き込む。


### 2. Youtube APIキー の取得
(参考) http://piyohiko.webcrow.jp/kids_tube/help/index.html

・27行目の

```
api_key = '**********************************'
```

のアスタリスクに取得したYoutube APIキーを記入


### 3. アプリの起動
streamlit run ファイル名
でアプリを起動させる。


# 時系列予測ライブラリのProphetを使って株価の予測

stockprophet.pyのプログラムを使っていきます。

### 1. まずはProphetのインストール

### Windowsの場合
https://touch-sp.hatenablog.com/entry/2019/10/09/124145

### Macの場合(Pystanをインストールしてから、Prophetのインストール)
https://facebook.github.io/prophet/docs/installation.html

## 8行目のファイルパスの修正

```
pd.read_csv("/Users/io/Desktop/prophet/stockdata/6758_2015_2020.csv"...
```
の

```
/Users/io/Desktop/prophet/stockdata/6758_2015_2020.csv
```

の部分を6758_2015_2020.csvのファイルを置いたパスに修正。

# ビデオゲームの売り上げ分析

videogame.pyのプログラムを使っていきます。

こちらは、

https://towardsdatascience.com/build-quick-and-beautiful-apps-using-streamlit-85f32ed01fb2
の記事の流れに沿ってチュートリアルを進めていきます。

使っていくデータはvgsales.csvです。

こちらはあらかじめ
https://www.kaggle.com/gregorut/videogamesales
からダウンロードしておきます。


