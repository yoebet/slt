import streamlit as st

conn = st.connection("postgresql", type="sql")

df = conn.query('SELECT * FROM t_user;', ttl="10m")

for row in df.itertuples():
    st.write(f"u_{row.id}, phone number: {row.phone_number}, role: {row.role}")
