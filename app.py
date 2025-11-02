# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import plotly.express as px
from statsmodels.stats.proportion import proportions_ztest

st.set_page_config(page_title="A/B Testing Analysis", layout="wide")

# -----------------------------
# Load Data
# -----------------------------
st.title("A/B Testing Analysis App")

file_path = "data/ab_testing.csv"
df = pd.read_csv(file_path)

# Preprocess
df['Conversion'] = df['Conversion'].map({'Yes': 1, 'No': 0})

# -----------------------------
# Tabs
# -----------------------------
tabs = st.tabs(["Problem & Goal", "Solution & Methodology", "Raw Data"])

# -----------------------------
# Tab 1: Problem & Goal
# -----------------------------
with tabs[0]:
    st.header("Problem & Goal")
    st.markdown("""
    ### Scenario:
    A retail website wants to test if changing the background color from **White (Group A)** 
    to **Black (Group B)** increases user engagement.
    
    ### Goal:
    Determine if the treatment (Black background) significantly improves conversion rate 
    and engagement metrics like time spent and page views.
    
    ### Dataset:
    Sample A/B testing data for 5,000 users across the UK.
    Columns include:
    - `User ID`
    - `Group` (A or B)
    - `Page Views`
    - `Time Spent`
    - `Conversion` (Yes/No)
    - `Device`
    - `Location`
    """)

# -----------------------------
# Tab 2: Solution & Methodology
# -----------------------------
with tabs[1]:
    st.header("Solution & Methodology")

    st.subheader("1️⃣ Hypothesis Testing")
    st.markdown("""
    **High-Level Explanation:**  
    We want to know if changing the website background from **White (Group A)** to **Black (Group B)** 
    significantly affects conversions.  

    **Test Conditions:**  
    - Null Hypothesis (H0): Conversion rate of Group A = Conversion rate of Group B  
    - Alternative Hypothesis (H1): Conversion rate of Group B ≠ Conversion rate of Group A  
    - Significance threshold: 0.05  

    **Interpretation for Non-Technical Audience:**  
    The test checks if the observed difference in conversions is likely due to the background color change 
    or just random chance. If the p-value is very small (below 0.05), the difference is considered real.
    """)

    convert_a = df[df['Group']=='A']['Conversion'].sum()
    convert_b = df[df['Group']=='B']['Conversion'].sum()
    n_a = df[df['Group']=='A'].shape[0]
    n_b = df[df['Group']=='B'].shape[0]
    count = [convert_a, convert_b]
    nobs = [n_a, n_b]
    stat, pval = proportions_ztest(count, nobs)

    st.write(f"**Z-statistic:** {stat:.6f}")
    st.write(f"**p-value:** {pval:.30f}")

    st.markdown(f"""
    **Conclusion:**  
    The p-value is extremely small, far below 0.05, so the observed difference is very unlikely due to chance.  
    ✅ We **reject the null hypothesis**. This means changing the background to black (Group B) significantly increased conversions.
    """)

    st.subheader("2️⃣ Conversion Rate by Group")
    conversion_summary = df.groupby('Group')['Conversion'].mean().reset_index()
    fig = px.bar(conversion_summary, x='Group', y='Conversion',
                 color='Group',
                 color_discrete_map={'A':'skyblue','B':'salmon'},
                 text=conversion_summary['Conversion'].apply(lambda x: f"{x:.4f}"),
                 title="Conversion Rate by Group")
    fig.update_layout(yaxis=dict(range=[0,1]))
    st.plotly_chart(fig, config={"displayModeBar": False}, use_container_width='stretch')

    st.subheader("3️⃣ Engagement Metrics")
    st.markdown("Time Spent and Page Views distributions by group:")

    col1, col2 = st.columns(2)

    with col1:
        fig = px.box(df, x='Group', y='Time Spent', color='Group',
                     color_discrete_map={'A':'lightgreen','B':'lightgreen'},
                     title="Time Spent by Group")
        fig.update_traces(boxmean='sd')
        st.plotly_chart(fig, config={"displayModeBar": False}, use_container_width='stretch')

    with col2:
        fig = px.box(df, x='Group', y='Page Views', color='Group',
                     color_discrete_map={'A':'lightcoral','B':'lightcoral'},
                     title="Page Views by Group")
        fig.update_traces(boxmean='sd')
        st.plotly_chart(fig, config={"displayModeBar": False}, use_container_width='stretch')

    st.subheader("4️⃣ Segmentation Insights")
    st.markdown("Conversion rates by device and location:")

    col1, col2 = st.columns(2)

    with col1:
        device_summary = df.groupby('Device')['Conversion'].mean().reset_index()
        fig = px.bar(device_summary, x='Device', y='Conversion',
                     color='Device',
                     color_discrete_sequence=px.colors.qualitative.Pastel,
                     text=device_summary['Conversion'].apply(lambda x: f"{x:.4f}"),
                     title="Conversion Rate by Device")
        fig.update_layout(yaxis=dict(range=[0,1]))
        st.plotly_chart(fig, config={"displayModeBar": False}, use_container_width='stretch')

    with col2:
        location_summary = df.groupby('Location')['Conversion'].mean().reset_index()
        fig = px.bar(location_summary, x='Location', y='Conversion',
                     color='Location',
                     color_discrete_sequence=px.colors.qualitative.Pastel,
                     text=location_summary['Conversion'].apply(lambda x: f"{x:.4f}"),
                     title="Conversion Rate by Location")
        fig.update_layout(yaxis=dict(range=[0,1]))
        st.plotly_chart(fig, config={"displayModeBar": False}, use_container_width='stretch')

# -----------------------------
# Tab 3: Raw Data
# -----------------------------
with tabs[2]:
    st.header("Raw Dataset")
    st.dataframe(df)
