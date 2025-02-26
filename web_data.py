from contextlib import redirect_stdout
import requests
import io
from bs4 import BeautifulSoup

class WebData:

    #Class Variables
    web_query: requests
    link: str
    APPLICATION = "Web Files/"

    #grab web information
    def __init__(self, link: str):
        self.web_query = requests.get(link)
        
    
    #check status code of website (success is 200)
    #source dump into local txt file
    def save_data(self):
        
        #Check if link was valid

        try:
            soup = BeautifulSoup(self.web_query.content, 'html.parser')
            soup.prettify()
            soup_str = str(soup)
                
                
            web_source = open(WebData.APPLICATION + "web_source.txt", "w")
            web_source.write(soup_str)
            web_source.close()
            
        except Exception:
            #we are passing in this case because not all links will be accessible
            pass

