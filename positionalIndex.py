#This is pickle module that would help us store the Inverted index back into the 
#storage space, and if we need it later we can retrive it and perform our query on that
import pickle

PositionalIndex = {}  # Creating a dictionary to store key and value pairs


#This function by giving the key finds the position of a word in the file 
#Then when a word comes again it will maintain a counter that would help us 
#In counting whether it it a first occurance of a word or second occurance 
def find_position_on_file(file_no,word,n):
    string = "preprocessed_text_files/file" + str(file_no) + ".txt"
    with open(string, 'r') as f:
        count=0
        for lines in f.readlines():
            for w in lines.split(' '):
                count=count+1
                if word == w:
                    if count>n:
                        return count 


#Here we are going through all the files in preprocessed folder 
#and going through each file one by one and making a index of the individual terms which occurs in it 
for num in range(1, 1000):
    string = "preprocessed_text_files/file" + str(num) + ".txt"
    with open(string, 'r') as f:
        for line_num, line in enumerate(f.readlines(), start=1):
            words = line.split(" ")
            for word in words:
                if word in PositionalIndex.keys():
                    if num in PositionalIndex[word].keys():
                        PositionalIndex[word][num].append(find_position_on_file(num,word,PositionalIndex[word][num][-1]))
                    else:
                        PositionalIndex[word][num]=[find_position_on_file(num,word,0)]    
                else:
                    PositionalIndex[word]={num:[find_position_on_file(num,word,0)]}


# for key in PositionalIndex:
#     print(f" {key} -> {PositionalIndex[key]}")
    

#sorting the dictionary by the keys  
myKeys = list(PositionalIndex.keys())
myKeys.sort()
sorted_Positional_dict = {i: PositionalIndex[i] for i in myKeys}
print("-----------------------------------------------------------------")
print("----------------------------------------------------------------")
 
 
print("After Sorting the dictionary")
for i in sorted_Positional_dict:
    print(f"{i} ->{sorted_Positional_dict[i]}")
                
#Dumping the inverted index using pickle
with open('positional_index.pickle', 'wb') as pickle_file:
     pickle.dump(PositionalIndex, pickle_file)