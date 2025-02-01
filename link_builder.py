from serpapi import GoogleSearch

class LinkBuilder:

    search_term: str



    search = GoogleSearch({
        "q": "coffee", 
        "location": "Austin,Texas",
        "api_key": "404d047e6067da14d3be3d7434b6a6bd381c82bbee15c457e0c4d7cfa517aeca"
    })

    result = search.get_dict()

    

