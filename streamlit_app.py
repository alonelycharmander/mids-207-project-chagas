import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("code15_metadata_clinical.csv")
    return df

df = load_data()

st.title("🫀 Chagas ECG Dataset Dashboard")

# Sidebar filters
st.sidebar.header("Filters")
source_filter = st.sidebar.multiselect("Source", df['source'].unique(), default=df['source'].unique())
sex_filter = st.sidebar.multiselect("Sex", df['sex'].dropna().unique(), default=df['sex'].dropna().unique())
label_filter = st.sidebar.multiselect("Chagas Label", df['label'].dropna().unique(), default=df['label'].dropna().unique())

df_filtered = df[df['source'].isin(source_filter) & 
                 df['sex'].isin(sex_filter) & 
                 df['label'].isin(label_filter)]

st.markdown(f"### Showing {len(df_filtered)} records after filtering")

# Age Distribution
st.subheader("Age Distribution")
fig, ax = plt.subplots()
sns.histplot(df_filtered['age'].dropna(), bins=30, kde=False, ax=ax)
st.pyplot(fig)

# Clinical flags
st.subheader("Clinical Flags Breakdown")
flag_cols = ['AF', 'RBBB', 'LBBB', 'normal_ecg', 'death']
if all(col in df_filtered.columns for col in flag_cols):
    flag_counts = df_filtered[flag_cols].fillna(False).astype(int).sum().sort_values(ascending=False)
    st.bar_chart(flag_counts)

# Signal length distribution
st.subheader("Signal Length")
if 'length' in df_filtered.columns:
    fig, ax = plt.subplots()
    sns.histplot(df_filtered['length'], bins=30, ax=ax)
    st.pyplot(fig)
