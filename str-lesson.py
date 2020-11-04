import streamlit as st
import numpy as np
import pandas as pd

# st.titleでタイトルの表示
st.title('ビデオゲーム売り上げ分析')

st.write("Here's our first attempt at using data to create a table:")

# st.writeの中にデータフレームを突っ込むことでデータフレームが描画できる
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

## st.line_chart()の中にデータフレームを入れることでチャートが描ける
st.line_chart(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

# チャートデータのデータフレームを作成
chart_data = pd.DataFrame(
     np.random.randn(3, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

st.subheader('ウィジェット')
if st.checkbox('チェックボックス'):
    st.write('チェックしました。')

option = st.selectbox(
    'この中から一つ選んで下さい',
    ('りんご', 'みかん', 'バナナ')
)

st.write('あなたが選んだのは:', option)

import time

if st.button('今すぐ申し込み'):
    text = st.empty()
    bar = st.progress(0)

    for i in range(100):
        text.text(f'ダウンロード中...')
        bar.progress(i+1)
        time.sleep(0.1)
    st.success('ダウンロードが完了しました。')
    st.balloons()