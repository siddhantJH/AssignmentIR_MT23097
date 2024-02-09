import pickle
with open("inverted_index.pickle", 'rb') as f:
        inverted_index = pickle.load(f)
        
        
for i,j in inverted_index.items():
    print(f"{i}-->{j}")