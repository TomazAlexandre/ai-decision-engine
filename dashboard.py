import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

st.set_page_config(page_title="AI Decision Dashboard", layout="wide")

st.title("🚀 AI Decision Engine Dashboard")

engine = create_engine("sqlite:///./decisions.db")

query = "SELECT * FROM decisions ORDER BY created_at DESC"

df = pd.read_sql(query, engine)

st.subheader("📊 Decisions History")

st.dataframe(df)

# métricas simples
total = len(df)
approved = len(df[df["decision"] == "APPROVED"])
rejected = len(df[df["decision"] == "REJECTED"])

col1, col2, col3 = st.columns(3)

col1.metric("Total Decisions", total)
col2.metric("Approved", approved)
col3.metric("Rejected", rejected)