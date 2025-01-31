import web_data


class WebSearch:
    
    #class variables
    words  = ("")
    
    test  = web_data.WebData("https://radikahn.com")
    
    test.save_data()
    
    def word_set():
        with open("Web Files/user_search_words.txt", 'r') as file:
            word_list = file.read()
            WebSearch.words = word_list.split(',')

            
        
    
    def parse_data_phrase(words: list):
        keywords = open("Web Files/keywords.txt", "w")
        
        with open("Web Files/web_source.txt", "r") as file:
            content = file.read()
            for word in words:
                if word in content:
                    print(word)
                    keywords.write(f"'{word}' \n")
                    
        keywords.close()
        
    def parse_data_sentence(words: list):
        keyphrases = open("Web Files/keyphrases.txt", "w")
        
        with open("Web Files/web_source.txt", "r") as file:
            for line in file:
                for i in range(len(words)):
                    if words[i] in line:
                        keyphrases.write(line)
                        
        keyphrases.close()
                    
                    
                

obj = WebSearch()
    
WebSearch.word_set()            
# WebSearch.parse_data_phrase(obj.words)
WebSearch.parse_data_sentence(obj.words)


