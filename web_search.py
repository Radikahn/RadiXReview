import web_data


class WebSearch:
    
    #class variables
    words  = ("")
    link_list = ("")
    
    
#Loads links.txt into list, then runs search on each link
    def link_queries(self):
        
        #clear result docs before appending
        WebSearch.reset_data()
        
        with open(web_data.WebData.APPLICATION + "links.txt") as file:
            self.link_list = file.readlines()
        
        for i in range(len(self.link_list)):
            link_const = web_data.WebData(self.link_list[i])
            link_const.save_data()
            
            print(self.link_list[i])
            WebSearch.word_set()
            WebSearch.parse_data_phrase(self.words)
            WebSearch.parse_data_sentence(self.words)

#Parse user inputted words into list
    def word_set():
        with open(web_data.WebData.APPLICATION + "user_search_words.txt", 'r') as file:
            word_list = file.read()
            WebSearch.words = word_list.split(',')
            
#Creates keywords.txt file, shows what words from user list were found    
    def parse_data_phrase(words: list):
        keywords = open(web_data.WebData.APPLICATION + "keywords.txt", "a")
        
        with open(web_data.WebData.APPLICATION + "web_source.txt", "r") as file:
            content = file.read()
            for word in words:
                if word in content:
                    print(word)
                    keywords.write(f"'{word}' \n")
                    
        keywords.close()

#Returns the HTML line in whicht keywords were found
    def parse_data_sentence(words: list):
        keyphrases = open(web_data.WebData.APPLICATION + "keyphrases.txt", "a")
        
        with open(web_data.WebData.APPLICATION + "web_source.txt", "r") as file:
            for line in file:
                for i in range(len(words)):
                    if words[i] in line:
                        keyphrases.write(line)
                        
        keyphrases.close()
        
#Resets keyphraselist.txt and keywordslist.txt

    def reset_data():
        with open(web_data.WebData.APPLICATION + "keyphrases.txt", "w") as file:
            file.write("")
            file.close()
        
        with open(web_data.WebData.APPLICATION + "keywords.txt", "w") as file:
            file.write("")
            file.close()
        
        
                    
obj = WebSearch()

obj.link_queries()

with open(web_data.WebData.APPLICATION + "links.txt", 'r') as file:
    list_sentence = file.readlines()
    
with open(web_data.WebData.APPLICATION + "keyphrases.txt", 'w') as file:
        sentences = set(list_sentence)
        for phrase in sentences:
            file.write(phrase)
        


