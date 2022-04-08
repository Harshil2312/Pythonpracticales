#!/usr/bin/env python
# coding: utf-8

# # Practical 4 Find runner-up from given list

# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.
# 
#  
# 
# Input Format: The first line contains. The second line contains an array A[]  of n integers each separated by a space.
# 
# Constraints:
# 
#   
# 
# 
# Output Format: Print the runner-up score.
# 
# Sample Input
# 
# 5
# 
# 2 3 6 6 5
# 
# Sample Output
# 
# 5
# 
# Explanation: Given list is [2,3,6,6,5]. The maximum score is 6, second maximum is 5. Hence, we print 5 as the runner-up score.

# In[8]:


# Taking input of n (size of array)
n = int(input())

# taking list form user using map finction and convert it into list
# first take a string from user which consist room numbers and after that split it using split
# function and convert in into int and after that map function pass it to list function which
# add that int into set.
# convert scores into set (for removing duplicates)
scores = list(set(map(int, input().split(" "))))

# sort the list in ascending order
scores.sort()
print(scores[-2])


# In[ ]:




