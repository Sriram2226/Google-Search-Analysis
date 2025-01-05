
---

# Google Search Analysis

This repository contains a Python-based web application to fetch and visualize Google Trends data for a given keyword over a specified timeframe. The project uses a FastAPI backend to request Google Trends data, and a Streamlit frontend to visualize it.

## Directory Structure

```
Sriram2226-Google-Search-Analysis/
    ├── Google_Search_Analysis_with_Python.ipynb
    ├── app.py
    └── frontend.py
```

### Files:

- **Google_Search_Analysis_with_Python.ipynb**: A Jupyter notebook showcasing the Google Trends analysis in Python.
- **app.py**: The backend implementation using FastAPI to fetch Google Trends data using the `pytrends` library.
- **frontend.py**: The frontend implementation using Streamlit to interact with the backend and visualize the data.

## Setup Instructions

### Prerequisites

1. Python 3.x installed on your machine.
2. Virtual environment setup (optional but recommended).

### Installing Dependencies

You can install the required dependencies by running the following command:

```bash
pip install -r requirements.txt
```


### Running the Application

1. **Backend (FastAPI)**

   Start the FastAPI backend server by running the following command in your terminal:

   ```bash
   uvicorn app:app --reload
   ```

   This will start the FastAPI server locally at `http://127.0.0.1:8000`.

2. **Frontend (Streamlit)**

   In another terminal window, run the following command to start the Streamlit frontend:

   ```bash
   streamlit run frontend.py
   ```

   This will open a web browser where you can interact with the Google Trends data visualizer.

## API Documentation

### `/get_trends/` (POST)

This API endpoint accepts a JSON request body containing two parameters: `keyword` and `timeframe`. It returns the top 10 interest over time data for the provided keyword.

#### Request

```json
{
  "keyword": "Cloud Computing",
  "timeframe": "today 12-m"
}
```

#### Response

```json
{
  "data": [
    {
      "date": "2024-01-01",
      "Cloud Computing": 75.0
    },
    {
      "date": "2024-01-02",
      "Cloud Computing": 85.0
    },
    ...
  ]
}
```

If no data is found, the response will contain an error message:

```json
{
  "error": "No data found for the given keyword and timeframe."
}
```

### Error Handling

In case of an error while fetching the data, the response will contain an error message:

```json
{
  "error": "Error fetching data: <error_message>"
}
```

## Features

- **Search Keyword**: Allows users to input a keyword to fetch trends data.
- **Select Timeframe**: Users can choose a timeframe (e.g., "today 12-m", "2018-01-01 2018-02-01").
- **Data Visualization**: Visualizes Google Trends data over time using bar charts.
- **Error Handling**: Displays appropriate error messages when there are issues with fetching or displaying data.

