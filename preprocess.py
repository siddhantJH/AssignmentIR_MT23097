

from nltk.tokenize import sent_tokenize, word_tokenize #importing nltk library that would help us in tokenizing the sentence and a word
from nltk.corpus import stopwords #these gives us the list of stop words which we can remoce from the text
from bs4 import BeautifulSoup #this helps us in removing the html tag from the file and extract the remaining word
import string  #helps us in string operation

#this gives us the list of all the stop words which exist int english alphabet 
all_stop_words=set(stopwords.words('english'))
all_stop_words_list=list(all_stop_words)



#writing back the token list back in the file
def writeback(new_token_list,file_no):
    string="preprocessed_text_files/file"+str(file_no)+".txt"
    with open(string,"a") as f:
        f.write(" ".join(new_token_list))
        f.close()

#purify the all_token list by removoing stop words and lowering the words
def purify(all_token_list,fileno):
    new_token_list = []
    for word in all_token_list:
        if word.lower() in all_stop_words_list:                     #Then we are removeing the stop words along with the lowring the word
          pass
        else:
            new_token_list.append(word.lower())
    writeback(new_token_list,fileno)


#save all tokens of a file in a list named as all_token(has impurity)
def preprocess_and_save(string,fileno):
    all_token=[]
    global file_no
    lines = lines.translate(str.maketrans('' '', string.punctuation))    #removing the punctuations
    tokens=word_tokenize(string)                                         #Tokenizingation is done here first 
    for word in tokens:
        all_token.append(word)
    file_no=fileno
    purify(all_token,fileno)                                             
    all_token.clear()



#lower case all the text
def preprocessed_text_files(file_path,num):
    with open(file_path,'r') as f:
        for lines in f.readlines():                        
            soup=BeautifulSoup(lines,"html.parser")                      #first removing all the html tags from the lines present in our original text
            lines=soup.get_text()                                        #for that we are using the beacutiful soup function gettext()       
            preprocess_and_save(lines,num)







            











        