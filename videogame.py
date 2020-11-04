import streamlit as st
from PIL import Image
import pandas as pd
import altair as alt

st.title('Video Game Sales Analysis')

# 開くImageの定義
image = Image.open('mario-1557240_1920.jpg')

st.image(image, caption='source: https://pixabay.com/photos/mario-luigi-yoschi-figures-funny-1557240/',
           use_column_width=True)

st.header('Exploratory Data Analysis')

st.markdown('Before we get started with the analysis, lets have a quick look at the raw data :sunglasses:')

df = pd.read_csv('vgsales.csv')

df_sample = df.head()
df_sample

st.subheader('プラットフォームごとの売り上げ')

# st.selectboxでセレクトボックスの作成。optionでリストや、データフレームの列などを指定。unique()をつけることで重複を削除
platform_name = st.selectbox('プラットフォームを選択して下さい', options=df.Platform.unique())

st.write('年ごとの売り上げ')
basic_chart = alt.Chart(df.loc[df.Platform == platform_name].groupby(['Platform', 'Year']). \
                        agg({'Global_Sales': 'sum'}).reset_index()).mark_line().encode(
    x='Year',
    y='Global_Sales'
)
st.altair_chart(basic_chart)

st.write(df.loc[df.Platform == platform_name, ['Platform', 'Year', 'NA_Sales', 'EU_Sales', 'JP_Sales', \
                                                     'Other_Sales']])

st.write('地域ごとの売り上げ')
temp = pd.melt(df.loc[df.Platform == platform_name, ['Platform', 'Year', 'NA_Sales', 'EU_Sales', 'JP_Sales', \
                                                     'Other_Sales']], id_vars=['Platform', 'Year'], var_name='Geo',
               value_name='Sales')
# sns.barplot(x="Year", y="Sales", hue="Geo", data=temp)
temp = temp.groupby(['Platform', 'Year', 'Geo']).agg({'Sales': 'sum'}).reset_index()
stacked_bar = alt.Chart(temp).mark_bar().encode(
    x='Year',
    y='Sales',
    color='Geo'
)
st.altair_chart(stacked_bar)


