#!/usr/bin/env python
# coding: utf-8

# # Practical 7

# In[5]:


# define a function which checks lapindrome
def is_lapindrome(str):
    #     if string is palindrome then it is lapindrome
    if (str == str[::-1]):
        return True
    else:
        #         if string length is even
        if (len(str) % 2 == 0):
            #         divide ths string in 2 parts and after sorting compare it
            if sorted(str[:len(str) // 2]) == sorted(str[len(str) // 2:]):
                return True
            else:
                return False

        #           if string length is odd
        else:
            #         divide ths string in 2 parts and after sorting compare it
            if sorted(str[:len(str) // 2]) == sorted(str[len(str) // 2 + 1:]):
                return True
            else:
                return False


# taking number of test cases
test_case = int(input())

# To store the words
words = []

# Taking String from user
for _ in range(test_case):
    words.append(input("Enter Your String: "))

# Iterate over a words list and check is it lapindrome
for _ in words:
    if is_lapindrome(_):
        print('YES')
    else:
        print('NO')


# In[6]:


-jt !r

