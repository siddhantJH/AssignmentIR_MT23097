import preprocess                                   #importing the preprocess file in order to clean the query we will use this 
import pickle
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import string
import math



#first we are taking as input the number of lines as input that will help us in 
#taking input in the required format as asked by the user 
lines = int(input())
list_of_stop_words = stopwords.words('english')

#Making a universal set out of all the element 
U = set()
for i in range(1,1000):
    U.add(i)



#convert list into string
def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1


#this functoon specificially helps us in removing the punctuations 
def remove_punctuation(input_string):
    translator = str.maketrans("", "", string.punctuation)
    result_string = input_string.translate(translator)
    return result_string


#This function takes as input the list of terms 
#and this function will help us find the documents which will 
#contain all the terms.
count=0
def Document_retrievalStep(list_of_terms):
    global count
    count=count+1
    with open("positional_index.pickle", 'rb') as f:
        positional_index = pickle.load(f)
        s1=U                                                #I have taken the universe , from which i will filter the docs 
        for item in list_of_terms:
                if item in positional_index.keys():
                    s1=s1.intersection(positional_index[item].keys())
                else:
                    s1=set()
        if(len(s1)!=999):
            print(f"Number of document retrived for query {count} using positional index: {len(s1)}")
            print(f"Names of document retrived for query {count} using positional index: ",end="")
            for docs in s1:
                print("File"+str(docs)+".txt ,")      
        else:
            print(f"Number of document retrived for query {count} using positional index: {0}")
            print(f"Names of document retrived for query {count} using positional index: {0}",end="")
            print("\n")
            
#This function takes as input list of query and will give 
#the document_retrievalStep() function one query at a time and give the result as a  set of documents 
def perform_retrival(list_of_query):
    for i in range(0,len(list_of_query)):
        Document_retrievalStep(list_of_query[i])
                   
def Input_give(lines):
    list_of_query=[]
    list_of_oper=[]
    for num in range(1, lines + 1):
        user_input = input()
        # list_of_op = str1.split(',')
        # list_of_oper.append(list_of_op)
        inp = user_input.lower()                                        #convert to lower
        word_list = word_tokenize(inp)                                  #tokenize the string
        list1 = [w for w in word_list if w not in list_of_stop_words]   #remove the stop words
        sentence = ' '.join(list1)                                  
        sentence = remove_punctuation(sentence)                         #remove the punctuatoons 
        list_of_terms = sentence.split(' ')
        list_of_query.append(list_of_terms)
    perform_retrival(list_of_query)                                      #perform the retrival of the queries
    
    
    
Input_give(lines)










   


    