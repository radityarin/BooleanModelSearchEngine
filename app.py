from bmse import BooleanModelSearchEngine

if __name__ == "__main__": 
    example_query = "Honda and murah not boros"
    bmse = BooleanModelSearchEngine('data/corpus.txt')
    a = bmse.ask(example_query)
    print(a) 