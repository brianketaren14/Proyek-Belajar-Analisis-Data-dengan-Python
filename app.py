import streamlit as st
import datetime
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df_grouping = pd.read_csv('air_quality.csv')
df_grouping['date'] = pd.to_datetime(df_grouping['date'])
min_date = df_grouping['date'].min()
max_date = df_grouping['date'].max()

with st.sidebar:
  st.image("https://cdn2.iconfinder.com/data/icons/weather-flat-14/64/weather02-512.png")

  start_date, end_date = st.date_input(
      label='Rentang Waktu', min_value=min_date,
      max_value=max_date,
      value=[min_date, max_date]
  )

df_grouping = df_grouping[(df_grouping["date"] >= str(start_date)) & 
                (df_grouping["date"] <= str(end_date))]

df_Aotizhongxin_Changping_Dingling_Dongsi = df_grouping[(df_grouping['station'] == 'Aotizhongxin') | (df_grouping['station'] == 'Changping') | (df_grouping['station'] == 'Dingling') | (df_grouping['station'] == 'Dongsi')]
df_Guanyuan_Gucheng_Huairou_Nongzhanguan = df_grouping[(df_grouping['station'] == 'Guanyuan') | (df_grouping['station'] == 'Gucheng') | (df_grouping['station'] == 'Huairou') | (df_grouping['station'] == 'Nongzhanguan')]
df_Shunyi_Tiantan_Wanliu_Wanshouxigong = df_grouping[(df_grouping['station'] == 'Shunyi') | (df_grouping['station'] == 'Tiantan') | (df_grouping['station'] == 'Wanliu') | (df_grouping['station'] == 'Wanshouxigong')]


def create_line_plot(df, column, title):
    fig = plt.figure(figsize=(25,7))
    sns.lineplot(data=df, x='date', y = column , hue='station')
    plt.title(title, fontsize = 25)
    plt.show()
    st.pyplot(fig)

col1, col2, col3, col4, col5 = st.columns(5) 
with col1:
  st.metric("Mean Of PM2.5", value=np.round(df_grouping['PM2.5'].mean()))
  st.metric("Mean Of PM10", value=np.round(df_grouping['PM10'].mean()))

with col2:
  st.metric("Mean Of SO2", value=np.round(df_grouping['SO2'].mean()))
  st.metric("Mean Of NO2", value=np.round(df_grouping['NO2'].mean()))

with col3:
  st.metric("Mean Of CO", value=np.round(df_grouping['CO'].mean()))
  st.metric("Mean Of O3", value=np.round(df_grouping['O3'].mean()))

with col4:
  st.metric("Mean Of TEMP", value=np.round(df_grouping['TEMP'].mean()))
  st.metric("Mean Of PRES", value=np.round(df_grouping['PRES'].mean()))

with col5:
  st.metric("Mean Of DEWP", value=np.round(df_grouping['DEWP'].mean()))
  st.metric("Mean Of RAIN", value=np.round(df_grouping['RAIN'].mean()))



col6, col7 = st.columns(2) 

with col6:
  st.subheader('Sum PM2.5 By Station')
  fig = plt.figure()
  plot = sns.barplot(df_grouping.groupby(by=['station'])['PM2.5'].sum().reset_index(), x="station", y="PM2.5")
  plt.xticks(rotation=90)
  st.pyplot(fig)

with col7:
  st.subheader('Sum PM10 By Station')
  fig = plt.figure()
  plot = sns.barplot(df_grouping.groupby(by=['station'])['PM10'].sum().reset_index(), x="station", y="PM10")
  plt.xticks(rotation=90)
  st.pyplot(fig)

with col6:
  st.subheader('Sum PM2.5 By Season')
  fig = plt.figure()
  plot = sns.barplot(df_grouping.groupby(by=['musim'])['SO2'].sum().reset_index(), x="musim", y="SO2")
  st.pyplot(fig)

with col7:
  st.subheader('Temp and SO2 By Season')
  fig = plt.figure()
  plot = sns.scatterplot(data=df_grouping, x='TEMP', y='SO2', hue='musim')
  st.pyplot(fig)
st.subheader('Table')
st.write(df_grouping)