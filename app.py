import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Data Analysis Toolkit",layout="wide")
st.title("📊 Data Analysis Toolkit")

f=st.file_uploader("Upload CSV, Excel, JSON or TXT",type=["csv","xlsx","json","txt"])
df=None
if f:
    if f.name.endswith(".csv"):
        df=pd.read_csv(f)
    elif f.name.endswith(".xlsx"):
        df=pd.read_excel(f)
    elif f.name.endswith(".json"):
        df=pd.read_json(f)
    else:
        df=pd.read_csv(f,sep=None,engine="python")
if df is not None:
    st.subheader("Preview")
    st.dataframe(df.head())
    if st.button("Describe"):
        st.write(df.describe(include="all"))
    if st.button("Missing Values"):
        st.write(df.isnull().sum())
    if st.button("Data Types"):
        st.write(df.dtypes)
    if st.button("Shape"):
        st.write(df.shape)
    if st.button("Remove Duplicates"):
        df=df.drop_duplicates()
        st.success("Duplicates removed")
    if st.button("Drop Missing Rows"):
        df=df.dropna()
        st.success("Missing rows removed")
    st.download_button("Download Clean CSV",df.to_csv(index=False),"cleaned_data.csv","text/csv")
    st.subheader("Visualization")
    num=df.select_dtypes(include=np.number).columns.tolist()
    chart=st.selectbox("Chart",["Bar","Line","Scatter","Histogram"])
    if num:
        x=st.selectbox("X",df.columns)
        y=st.selectbox("Y",num)
        fig,ax=plt.subplots()
        if chart=="Bar":
            ax.bar(df[x].astype(str),df[y])
        elif chart=="Line":
            ax.plot(df[x],df[y])
        elif chart=="Scatter":
            ax.scatter(df[x],df[y])
        else:
            ax.hist(df[y],bins=10)
        plt.xticks(rotation=45)
        st.pyplot(fig)
