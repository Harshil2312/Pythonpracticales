#!/usr/bin/env python
# coding: utf-8

# # Practical 5: Swap Case

# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa. Sample Input: HackerRank.com presents "Pythonist 2".
# 
# Sample Output: hACKERrANK.COM PRESENTS "pYTHONIST 2".

# In[3]:


# defining function which convert lowercase to uppercase and uppercase to lowerase and return it
def swap_string(str):
    #  function which convert strings
    return str.swapcase()

# defining a string
text = 'My name is Harshil.'

# printing converted string
print(swap_string(text))

