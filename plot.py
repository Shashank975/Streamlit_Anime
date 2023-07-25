import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as ply


st.header("-------------------------Line Plot-------------------------")
df=pd.DataFrame(np.random.randn(20,3),columns=["Line-1","Line-2","Line-3"])
st.line_chart(df)


st.header("-------------------------Area Plot-------------------------")
st.area_chart(df)

st.header("-------------------------Bar Plot-------------------------")
st.bar_chart(df)




