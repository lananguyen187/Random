#!/usr/bin/env python
# coding: utf-8

# In[2]:


n=20006

while n!=1:
  print(n, end=", ")
  if n%2 ==0:
    n=n//2
  else:
    n=n*3+1
print(n,end=" .\n")


# In[8]:


# check number of digit
n = 25
count = 0
while n!=0:
    n=n//10
    count=count+1   
print(count)


# In[10]:


# print number of digit is 0,5

n= 405670
count = 0
while n!=0:
    n=n//10
    digit=n%10
    if digit ==0 or digit == 5:
        count=count+1

print(count)
    


# In[ ]:




