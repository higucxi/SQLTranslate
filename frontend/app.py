import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8001/generate_sql/"

st.title("🧠 Natural Language → SQL Generator")
st.write("Enter a natural language question and get an SQL query (and optional execution results).")

nl_query = st.text_area("Your natural language query:")
execute_query = st.checkbox("Execute SQL on sample DB")

if st.button("Generate SQL"):
    with st.spinner("Generating SQL..."):
        response = requests.post(API_URL, json={"text": nl_query, "execute": execute_query})
        data = response.json()

        st.subheader("🧾 Generated SQL:")
        st.code(data["sql"], language="sql")

        if execute_query:
            if "error" in data["result"]:
                st.error(f"SQL Execution Error: {data['result']['error']}")
            else:
                rows = data["result"]["rows"]
                cols = data["result"]["columns"]
                if rows:
                    df = pd.DataFrame(rows, columns=cols)
                    st.dataframe(df)
                else:
                    st.info("No results returned.")
