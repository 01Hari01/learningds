#This file is dedicarted for the purpose of understnding the lists concepts step by step in python 3.
#Author: HariKrishna Thoka
#Date Created: 21-02-2023

numbers=[1,2,6,5,545,454,34]
total=sum(numbers)
sizze=len(numbers)
numbers.extend((24,43,232))
numbers.insert(4,54)
print(numbers,total,sizze)

#Learning point 1: Most important functions on lists(specifically numbers) are append, extend, insert, pop, remove, reverse, sort

sentence=input("Enter a sentence: ")
words=sentence.split()
characters=list(words)
print(sentence,words,characters)
from collections import *
stringArr="The white chocolate bar is the best in the world"
words_list=stringArr.split()
word_count=Counter(words_list)
print(word_count)






