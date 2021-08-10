#wap count and display the number of words used by the user to give the introduction

words = input("Enter some words:")
#happy
#charactercount for counting the letters and wordcound for counting words
charactercount = 0
wordcount = 1

for i in words:
    charactercount = charactercount + 1
    if(i==' '):
        wordcount = wordcount + 1
print("Number of letters: ", charactercount)
print("Number of words: ", wordcount)


