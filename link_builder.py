from serpapi import GoogleSearch
from dotenv import load_dotenv
import os
import json
import web_data

class LinkBuilder:
    

    

    def pull_links() -> dict:

        load_dotenv()

        api_key = os.getenv('API')
        
        search_query = LinkBuilder.user_search_builder()

        #Pull data from google search api
        params = GoogleSearch({
            "q": search_query, 
            "device": "desktop",
            "api_key": api_key
        })

        results = params.get_dict()

        return results["organic_results"]
    
#Append user submitted search terms and return final query string
    def user_search_builder() -> str:
        with open(web_data.WebData.APPLICATION + "search_query.txt", 'r') as file:
            search_query = file.read()
            
        with open(web_data.WebData.APPLICATION + "user_search_words.txt") as file:
            search_words = file.read().split(",")
        
        for i in range (len(search_words)):
            search_query += " " + search_words[i]
            
        return search_query + " reddit"


#Parse data into formatted JSON file
    def write_to_json(links: dict):
        file = open("Web Files/link_results.json", 'w+')
        
        file.write(json.dumps(links, indent = 4))
        
        file.close()



LinkBuilder.write_to_json(LinkBuilder.pull_links())




    

