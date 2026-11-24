import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Student Performance", layout="wide")

st.title("Student Performance Analysis Dashboard")
st.write("Analysis of factors associated with student academic performance")

df = pd.read_csv("student-mat.csv", sep=None, engine="python")

st.header("Dataset Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Total Students", len(df))
col2.metric("Average Grade", round(df["G3"].mean(), 2))
col3.metric("Missing Values", int(df.isnull().sum().sum()))

st.dataframe(df.head(10))

st.header("1. Study Time and Final Grades")

st.bar_chart(df.groupby("studytime")["G3"].mean())

st.write("Students with longer study times generally have higher average grades.")

st.header("2. Absences and Final Grades")

fig, ax = plt.subplots()
ax.scatter(df["absences"], df["G3"], alpha=0.6)
ax.set_xlabel("Number of Absences")
ax.set_ylabel("Final Grade")
st.pyplot(fig)

st.write("Absences show a very weak linear relationship with final grades.")

st.header("3. Previous Failures and Final Grades")

st.bar_chart(df.groupby("failures")["G3"].mean())

st.write("Students with more previous failures tend to have lower final grades.")

st.header("4. Interactive Student Filter")

study = st.selectbox("Select Study Time Category", [1, 2, 3, 4])

filtered = df[df["studytime"] == study]

st.metric("Average Final Grade", round(filtered["G3"].mean(), 2))

st.dataframe(filtered)

st.header("Conclusion")

st.write("""
- Longer study time is generally associated with better grades.
- Previous failures are associated with lower academic performance.
- Absences have a very weak linear correlation with final grades.
- These relationships do not necessarily prove causation.
""")
