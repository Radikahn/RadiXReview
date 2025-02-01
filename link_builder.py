from serpapi import GoogleSearch
from dotenv import load_dotenv
import os
import json

class LinkBuilder:

    def pull_links() -> dict:

        load_dotenv()

        api_key = os.getenv('API')


        params = GoogleSearch({
            "q": "coffee", 
            "location": "San Jose,California",
            "device": "desktop",
            "api_key": api_key
        })

        results = params.get_dict()

        return results["organic_results"]
    


    def write_to_json(links: dict):
        file = open("Web Files/link_results.json", 'w+')
        
        file.write(json.dumps(links, indent = 4))
        
        file.close()

        

LinkBuilder.write_to_json(LinkBuilder.pull_links())




    

