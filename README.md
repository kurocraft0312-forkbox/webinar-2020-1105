# python初心者でも５分でアプリを作ろう！

2020-11月05日のデイトラウェビナーで解説した流れをまとめました。
こちらを見ながらstreamlitを使い、Pythonで簡単にアプリを作る体験してみましょう！

streamlitはPythonでWebアプリを簡単に作れるフレームワークです。

![5ed15d93ea8434e97414e47f_5e1115140227d02d6777adcb_AV_website_large](https://user-images.githubusercontent.com/69081467/98185663-6d81cd00-1f50-11eb-945e-c9d54d7359be.gif)

## Python初学者がstreamlitを使うメリット
https://www.streamlit.io/

機械学習、データ可視化、分析用のアプリをフロントのコーディングなどなしに、
非常にシンプルなコードでサクッと作れます！

<img width="745" alt="uberpicksc" src="https://user-images.githubusercontent.com/69081467/98186112-63ac9980-1f51-11eb-9704-4452ff2b3ead.png">

もちろんデータ分析以外のアプリを作る時でもOK!
コードが非常にシンプルなので、Python初心者の方でも馴染みやすいと思います。


### Pythonのアプリの解説とstreamlitの位置付けをマインドマップで解説してみました。
https://mm.tt/1679296151?t=URbLdlR6D4

<img width="922" alt="スクリーンショット 2020-11-05 11 28 52" src="https://user-images.githubusercontent.com/69081467/98190327-2698d500-1f5a-11eb-8803-e02c5f85fe32.png">

streamlitはフロントの実装がいらないので、サクッとデータ分析、
可視化アプリを作ってシェアしたい方向けです。

また、Flask⇨FastAPIに移行する人が増えています。
がっつり作りたいなら色々揃って作りやすいDjangoまたは
軽量で高速なFastAPIが良いでしょう。

### 日本語でstreamlitの使い方を一覧で見やすくまとめてあるサイト
https://bit.ly/38cEUJF

初めての方はまずこのようなサイトで書き方を見て慣れると習得が早いのでおすすめです。

### streamlitの公式APIリファレンス（使い方一覧・英語)
https://docs.streamlit.io/en/stable/api.html
(streamlitのコマンドが乗っています。)

### データフレームについての解説(データフレームが分からない人用)
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

### 注意点
Pythonのバージョンが古い場合はインストールの際にうまくいかず、
エラーが起こる場合があるのでバージョンアップしましょう。

また、colabではインストールが難しいようです。

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
と入力してEnterを押します。

すると下記のようにURLが出るので、
そちらをクリックするとブラウザが立ち上がってアプリを見ることができます。

<img width="371" alt="スクリーンショット 2020-11-05 10 34 21" src="https://user-images.githubusercontent.com/69081467/98186632-8b503180-1f52-11eb-8865-f210ee790214.png">


## 実際にアプリを作ってみよう

それでは、ここから実際にプログラムを使ってアプリを作る体験をしてみましょう！


# Youtubeの24時間以内に一定回数以上再生された動画情報を取得

youtube-24.pyのプログラムを使っていきます。

Youtube APIにて、指定したキーワードでYoutube内を検索して、
24時間以内に1万回以上再生された動画をピックアップしてくれる
プログラムです。

このような感じでデータを取得して見れるようになります。
<img width="754" alt="スクリーンショット 2020-11-05 11 23 07" src="https://user-images.githubusercontent.com/69081467/98189969-63b09780-1f59-11eb-99db-c99749305c6e.png">


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

完成イメージはこのような形になります。(6758 Sonyの株価を予測しています。)
<img width="766" alt="スクリーンショット 2020-11-05 11 52 04" src="https://user-images.githubusercontent.com/69081467/98191869-74fba300-1f5d-11eb-8887-cc4b82aa246e.png">

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

最終的にはこのような感じのアプリができます。

<img width="755" alt="スクリーンショット 2020-11-05 11 40 52" src="https://user-images.githubusercontent.com/69081467/98191095-d458b380-1f5b-11eb-8e9c-6027c3b95160.png">

こちらは、

https://towardsdatascience.com/build-quick-and-beautiful-apps-using-streamlit-85f32ed01fb2
の記事の流れに沿ってチュートリアルを進めていきます。

使っていくデータはvgsales.csvです。

こちらはあらかじめ
https://www.kaggle.com/gregorut/videogamesales
からダウンロードしておきます。


# 各国のコロナ感染者状況の可視化

![picture_pc_9c61e950332308c91b631eb2bd40f097](https://user-images.githubusercontent.com/69081467/98193161-df154780-1f5f-11eb-8108-8cb4a13c7533.png)

ウェビナーでは時間の都合上できませんでしたが、
コロナ感染者状況のグラフについての解説は過去のnoteに記載
しました。

https://note.com/hipotaso/n/n26a9d5d386e2

こちらを見ながらstreamlitによるグラフ可視化をぜひトライ
してみて下さい。
