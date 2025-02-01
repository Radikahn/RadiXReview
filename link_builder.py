from serpapi import GoogleSearch
from dotenv import load_dotenv
import os

class LinkBuilder:

    search_term: str

    load_dotenv()

    api_key = os.getenv('API')
   
    

    params = GoogleSearch({
        "q": "coffee", 
        "location": "San Jose,California",
        "tbm": "xxx",
        "output": "json",
        "device": "desktop",
        "api_key": api_key
    })

    search = GoogleSearch(params)
    results = search.get_dict()
    organic_results = results["organic_results"]




    

