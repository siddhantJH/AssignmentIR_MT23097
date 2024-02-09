import nltk
from bs4 import BeautifulSoup
from nltk import sent_tokenize , word_tokenize
from nltk.corpus import stopwords
import string 


#step 1 performing lowercase and storing in a different files/printing
def lowercase_it(file_no):
    for num in range(file_no,file_no+1):
        with open("text_files/file"+str(num)+".txt",'r') as f:
            for num in f.readlines():
                num1=num.lower()
                print(num1)
    f.close()            
               
#step 2 tokenization and printing it 
def tokenization(file_no):
    for num in range(file_no,file_no+1):
        with open("text_files/file"+str(num)+".txt",'r') as f:
            for num in f.readlines():
                print(sent_tokenize(num))
                print(word_tokenize(num))
    f.close()   
    
    
list_of_stop_words=stopwords.words('english')
#step 3 remove stop words and print it 
def removeStopWords(file_no):
    for num in range(file_no,file_no+1):
        with open("text_files/file"+str(num)+".txt",'r') as f:
            for num in f.readlines():
                list1=num.split(" ")
                for w in list1:
                    if w in list_of_stop_words:
                        pass
                    else:
                        print(w,end=" ")
    f.close()  


#step 4 remove punctuations from the sentence 
def removePunc(file_no):
    for num in range(file_no,file_no+1):
        with open("text_files/file"+str(num)+".txt",'r') as f:
            for num in f.readlines():
                num = num.translate(str.maketrans('', '', string.punctuation))
                print(num)
    f.close()

#step 5 remove blank space tokens
def removeBlank(file_no):  
    for num in range(file_no,file_no+1):
        with open("text_files/file"+str(num)+".txt",'r') as f:
            for num in f.readlines():
                output_string = ' '.join(num.split())
                print(output_string)
                


# lowercase_it(11);
# print('\n')
# lowercase_it(12);
# print('\n')
# lowercase_it(13);
# print('\n')
# lowercase_it(14);
# print('\n')
# lowercase_it(15);



# tokenization(11);
# print('\n')
# tokenization(12);
# print('\n')
# tokenization(13);
# print('\n')
# tokenization(14);
# print('\n')
# tokenization(15);


# removeStopWords(11);
# print('\n')
# removeStopWords(12);
# print('\n')
# removeStopWords(13);
# print('\n')
# removeStopWords(14);
# print('\n')
# removeStopWords(15);


# removePunc(11);
# print('\n')
# removePunc(12);
# print('\n')
# removePunc(13);
# print('\n')
# removePunc(14);
# print('\n')
# removePunc(15);


# removeBlank(11);
# print('\n')
# removeBlank(12);
# print('\n')
# removeBlank(13);
# print('\n')
# removeBlank(14);
# print('\n')
# removeBlank(15);


