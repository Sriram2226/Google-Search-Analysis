# backend.py
from fastapi import FastAPI
from pydantic import BaseModel
from pytrends.request import TrendReq
import pandas as pd

app = FastAPI()

# Create a model for incoming requests
class KeywordRequest(BaseModel):
    keyword: str
    timeframe: str

# Initialize pytrends object
pytrends = TrendReq(hl='en-US', tz=360)

@app.post("/get_trends/")
async def get_trends(request: KeywordRequest):
    try:
        keyword = request.keyword
        timeframe = request.timeframe
        pytrends.build_payload([keyword], cat=0, timeframe=timeframe)
        
        # Fetch interest over time data
        data = pytrends.interest_over_time()
        
        # Check if data is empty
        if data.empty:
            return {"error": "No data found for the given keyword and timeframe."}
        
        # Sort and return the top 10 results
        data_sorted = data.sort_values(by=keyword, ascending=False).head(10)
        data_sorted = data_sorted.reset_index()
        return {"data": data_sorted.to_dict(orient="records")}
    except Exception as e:
        return {"error": str(e)}

