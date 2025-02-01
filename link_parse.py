import json
import web_data

class LinkParse:
    
    json_data = ""
    
    def __init__(self):
        #constructor will open json file and read contents
        json_file = open(web_data.WebData.APPLICATION + "link_results.json", 'r')
        self.json_data = json.load(json_file)
    
    #parse json file for links
    def find_links(self):

        links_file = open(web_data.WebData.APPLICATION + "links.txt", 'w+')
        
        link = {""}
        
        for i in range(len(self.json_data)):
            if "link" in self.json_data[i]:
                
                #create string of link for each position, (+8 for isolating link fron "link: " prefix)
                start = str(self.json_data[i]).index("link") + 8
                
                cat = str(self.json_data[i])[start::]
                
                #isolation link from quote suffix
                end = cat.index(",") + start - 2
                
                links_file.write(f"{str(self.json_data[i])[start:end]}\n")
                
                

        
        
    
        
obj = LinkParse()

obj.__init__()

obj.find_links()