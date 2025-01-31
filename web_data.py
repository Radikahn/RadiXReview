from contextlib import redirect_stdout
import requests
import io
from bs4 import BeautifulSoup

class WebData:

    #Class Variables
    web_query: requests
    link: str

    #grab web information
    def __init__(self, link: str):
        self.web_query = requests.get(link)
        
    
    #check status code of website (success is 200)
    #source dump into local txt file
    def save_data(self):
        
        #Check if link was valid
        f = io.StringIO()
        with redirect_stdout(f):  
            print(self.web_query)
        
        output = f.getvalue().strip()
        
        if output != 200:
            return Exception("The Web Address Is Not Valid")
        
        soup = BeautifulSoup(self.web_query.content, 'html.parser')
        soup.prettify()
        soup_str = str(soup)
            
            
        web_source = open("web_source.txt", "w")
        web_source.write(soup_str)
        web_source.close()

