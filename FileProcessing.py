#MH.Movasaghinia
#2019-3-6
#mmghho77@gmail.com
File_Name = input("Enter File name : ")
logfile = open(File_Name, "r") 
wordcount = 0
my_word=input("Enter the Word that you want to find the number of that : ")
for line in logfile:
    if my_word in line.split():
        wordcount += 1

print ("The repetition of the \"%s\" word is %d times in the \"%s\" file." % (my_word,wordcount,File_Name))