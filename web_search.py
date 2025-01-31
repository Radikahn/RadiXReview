import web_data


class WebSearch:
    
    #class variables
    words  = {""}
      
    test  = web_data.WebData("https://radikahn.com")
    
    test.save_data()
    
    def word_set():
        with open("user_search_words.txt", 'r') as file:
            word_list = file.read()
            WebSearch.words = word_list.split(',')

            
        
    
    def parse_data(words: set):
        keywords = open("keywords.txt", "w")
        
        with open("./web_source.txt", "r") as file:
            content = file.read()
            for word in words:
                if word in content:
                    print(word)
                    keywords.write(f"'{word}' \n")

obj = WebSearch()
    
WebSearch.word_set()            
WebSearch.parse_data(obj.words)