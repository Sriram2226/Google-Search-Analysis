# app.py
import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

# FastAPI URL
API_URL = "http://127.0.0.1:8000/get_trends/"

# Streamlit App
def main():
    st.title("Google Trends Data Visualizer")

    # Input section
    keyword = st.text_input("Enter a Keyword:", "Cloud Computing")
    timeframe = st.selectbox("Select Timeframe:", ["today 12-m", "2018-01-01 2018-02-01"])

    if st.button("Fetch Trends Data"):
        if keyword:
            # Request data from the FastAPI backend
            try:
                response = requests.post(API_URL, json={"keyword": keyword, "timeframe": timeframe})
                data = response.json()

                if "data" in data:
                    df = pd.DataFrame(data["data"])

                    # Display the data as a table
                    st.write(df)

                    # Plotting the data
                    plt.figure(figsize=(10, 5))
                    plt.bar(df['date'], df[keyword])
                    plt.xlabel('Date')
                    plt.ylabel('Interest Level')
                    plt.title(f"Interest Over Time for {keyword}")
                    plt.xticks(rotation=45)
                    st.pyplot(plt)
                else:
                    st.error(f"Error: {data.get('error')}")
            except requests.exceptions.RequestException as e:
                st.error(f"Error fetching data: {str(e)}")

if __name__ == "__main__":
    main()
