#!/usr/bin/env python
# coding: utf-8

# # Practical 6

# AIM: You are given n words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.
# 
# Sample Input 
# 4 
# bcdef 
# abcdefg 
# bcde 
# bcdef
# 
# Sample Output 
# 3 
# 2 1 1 
# 
# Explanation: There are 3 distinct words. Here, "bcdef" appears twice in the input at the first and last positions. The other words appear once each. The order of the first appearances are "bcdef", "abcdefg" and "bcde" which corresponds to the output.

# In[4]:


# taking number of test cases
test_case = int(input())

# List for storing words
words = []

# taking words form the user
for _ in range(test_case):
    str = input()
    words.append(str)

# convert list to set to remove duplicates
temp = set(words)

# count the number of duplicates and store it in a list
count = []
for _ in temp:
    number = words.count(_)
    count.append(number)

print(len(temp))
print(count)

