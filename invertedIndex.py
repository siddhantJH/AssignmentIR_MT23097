#This is pickle module that would help us store the Inverted index back into the 
#storage space, and if we need it later we can retrive it and perform our query on that
import pickle


#Create an Empty dictionary on which we will make our index
#the terms will be store as a key and the value as a posting list 
InvertedIndex = {}  # Creating a dictionary to store key and value pairs

#looping through preprocessed files and making inverted index on them
#First taking a file one by one starting from 0 to 999
#Than extracting lines from it step by step 
for num in range(1, 1000):
    string = "preprocessed_text_files/file" + str(num) + ".txt"
    with open(string, 'r') as f:
        for line_num, line in enumerate(f.readlines(), start=1):
            words = line.split(" ")
            for word in words:
                if word in InvertedIndex.keys():
                    if num in InvertedIndex[word]:
                        pass
                    else:
                        InvertedIndex[word].append(num)
                else:
                    InvertedIndex[word] = [num]


#printing the dictionary before sorting it 
print("Before Sorting the dictionary")
# Example: Print all keys and values
for key in InvertedIndex:
    print(f" {key} -> {InvertedIndex[key]}")
    

#sorting the dictionary by the keys than storing the Inverted index
myKeys = list(InvertedIndex.keys())
myKeys.sort()
sorted_dict = {i: InvertedIndex[i] for i in myKeys}
print("-----------------------------------------------------------------")
print("----------------------------------------------------------------")
 
 
#Dictionary after sorting all the elements by keys 
print("After Sorting the dictionary")
for i in sorted_dict:
    print(f"{i} ->{sorted_dict[i]}")
                
# Dumping the inverted index using pickle back into hdd
with open('inverted_index.pickle', 'wb') as pickle_file:
    pickle.dump(InvertedIndex, pickle_file)