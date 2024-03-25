import streamlit as st
import pandas as pd

conn = st.connection("postgresql", type="sql")

df = conn.query('SELECT id,phone_number,role FROM t_user', ttl="10m")

st.dataframe(df)
