import preprocess
import pickle
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import string
import math

lines = int(input())
list_of_stop_words = stopwords.words('english')
U = set()
for i in range(1,1000):
    U.add(i)

def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1


def remove_punctuation(input_string):
    translator = str.maketrans("", "", string.punctuation)
    result_string = input_string.translate(translator)
    return result_string

count=0
def Document_retrievalStep(list_of_terms, list_of_op):
    global count
    count=count+1
    with open("inverted_index.pickle", 'rb') as f:
        inverted_index = pickle.load(f)
        docs_sets=[]
        ans_docs_set = set()
        for term in list_of_terms:
            if term in inverted_index.keys():
                 docs_sets.append(set(inverted_index[term]))
            else:
                docs_sets.append(set([]))
        dup=list_of_op.copy()
        print("Query: ",end="")
        for term in list_of_terms:
            print(term,end=" ")
            if(len(list_of_op)):
                print(list_of_op[0],end=" ")
                list_of_op.remove(list_of_op[0])
        for term in dup:
                s1=docs_sets[0]
                s2=docs_sets[1]
                docs_sets.remove(s1)
                docs_sets.remove(s2)
                if(term=="OR"):
                    docs_sets.insert(0,s1.union(s2))
                if(term=="AND"):
                    docs_sets.insert(0,s1.intersection(s2))
                if(term=="AND NOT"):
                    docs_sets.insert(0,s1.intersection(U.difference(s2)))
                if(term=="OR NOT"):
                    docs_sets.insert(0,U.union(U.difference(s2)))
        print("\n")
        print(f"QUERY {count} :No of documents retrived for query: {len(docs_sets[0])}")
        print(f"Names of document retrived for Query {count} is: ",end="")
        for docs in docs_sets:
           for ele in docs:
               print("file"+str(ele)+".txt ,",end="") 
        print('\n')    

def perform_retrival(list_of_query,list_of_op):
    for i in range(0,len(list_of_op)):
        Document_retrievalStep(list_of_query[i],list_of_op[i])
                   
def Input_give(lines):
    list_of_query=[]
    list_of_oper=[]
    for num in range(1, lines + 1):
        user_input = input()
        str1 = input()
        list_of_op = str1.split(',')
        list_of_oper.append(list_of_op)
        inp = user_input.lower()
        word_list = word_tokenize(inp)
        list1 = [w for w in word_list if w not in list_of_stop_words]
        sentence = ' '.join(list1)
        sentence = remove_punctuation(sentence)
        list_of_terms = sentence.split(' ')
        list_of_query.append(list_of_terms)
    perform_retrival(list_of_query,list_of_oper)
    
    
    
Input_give(lines) 
    
    
    
    
