from typing import Union
from fastapi import FastAPI
import datetime

app = FastAPI()

def get_current_season() -> str:
    """
    Determine the current season based on the current month.

    Returns:
        str: The current season ("Winter", "Spring", "Summer", or "Autumn").
    """
    month = datetime.datetime.now().month
    if month in (12, 1, 2):
        return "Winter"
    elif month in (3, 4, 5):
        return "Spring"
    elif month in (6, 7, 8):
        return "Summer"
    elif month in (9, 10, 11):
        return "Autumn"

@app.get("/")
def read_root():
    """
    Root endpoint of the API.

    Returns:
        str: Welcome message for the API.
    """
    return {"message": "Welcome to Pixity's ShowdownSMP Seasons API"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/showdown/season")
def get_season():
    """
    API endpoint to retrieve the current season.

    Returns:
        str: The current season as a JSON response.
    """
    season = get_current_season()
    return {"season": season}
