import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime

if "data" not in st.session_state:
  df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
  df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
  df_data = df_data[df_data["Value(£)"] > 0 ]
  df_data = df_data.sort_values(by="Overall", ascending=False)
  st.session_state["data"] = df_data

st.markdown("# FIFA23 OFFICIAL DATASET!")

btn = st.link_button("Acesse os dados no kaggle", "https://www.kaggle.com/datasets/stefanoleone992/fifa-23-complete-player-dataset")

st.markdown("""
Esse dataset prove os dados dos jogadoes do modo carreira do FIFA 17 ao FIFA 23.
""")