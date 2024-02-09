import preprocess


#This functioonn specificially takes all the files form the text_files folder and performs the 
# preprocessing on them, Tokenization, lower ,stopWords,punctuation and blank space token  
#and stores the preprocessed files back in preprocessed_text_files folder with same name
for num in range(1, 1000):
    filename = "text_files/file" + str(num) + ".txt"
    preprocess.preprocessed_text_files(filename, num)
    


            
