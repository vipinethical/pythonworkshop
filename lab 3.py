#!/usr/bin/env python
# coding: utf-8

# ## ques1

# In[1]:


i=1


# In[2]:


while i<4:
    print(i)
    i+=1
else :
    print("inside else")


# ## ques 2

# In[3]:


for i in range(2,12,2):
    for j in range(i,12):
        print(i)
        break


# ## ques 3
# 

# In[4]:


for num in range(1,7):
    if num%2 !=0:
        continue
    print(num)


# ## ques4

# In[5]:


mutex= True
if (mutex == True):
    pass
else :
    print('False')


# ## ques 5

# In[6]:


string = "something"
print(len(string))


# ## ques 6
# 

# In[7]:


string= "insert here"
string.count("e")


# ## ques 7

# In[8]:


str= "insert here"
if len(str) >=2:
    print(str[0:2]+ str[-2:])


# ## ques 8

# In[12]:


str1='insert the text'
char = str1[0]
length= len(str1)
str1=str1.replace(char,'*')
str1= char + str1[1:]
print(str1)


# ## ques 9

# In[13]:


str1='vipin'
str2='chaudhary'
stra=str2[0]+str1[1:]
strb=str1[0]+str2[1:]
str3=stra+''+strb
print(str3)


# In[ ]:




