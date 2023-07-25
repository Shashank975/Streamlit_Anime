import streamlit as st
import numpy as np
import pandas as pd


st.header("-------------------Look at this Stats-------------------")
st.subheader("---------------------------Episodes Ranking--------------------------------")

df=pd.read_csv("ONE PIECE.csv")
if df is not None:
    st.table(df.head(5))

st.header("--------------------------Crew----------------------------")
img=st.image("peakpx.jpg")


st.subheader("-----------------------Upload Crew Image----------------------------")


imge= st.file_uploader("Uplode the Image : ",type=['jpg','jpeg'])
if imge is not None:
    st.image(imge)


st.subheader("------------------------Upload Crew Docmt----------------------------")

doc= st.file_uploader("Uplode the Document : ",type=['pdf','xlsx'])
if doc is not None:
    st.dataframe(doc)

st.subheader("------------------------Upload Crew Audio-----------------------------")

Aud= st.file_uploader("Uplode the Audio : ",type=['mp4'])
if Aud is not None:
    st.audio(Aud)


st.subheader("------------------------Upload Crew Video-----------------------------")

vid= st.file_uploader("Uplode the Video : ",type=['mkv'])
if vid is not None:
    st.video(vid)