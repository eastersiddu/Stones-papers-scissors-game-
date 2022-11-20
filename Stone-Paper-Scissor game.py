#!/usr/bin/env python
# coding: utf-8

# In[4]:


p1=input("enter the frist person: ")
p2=input("enter the second person: ")
if p1=="Stone":
    if p2=="Scissor":
        print("p1 wins")
    elif p2=="Paper":
        print("p2 wins")
    elif p2=="Stone":
        print("match tie")
elif p1=="Scissor":
    if p2=="Scissor":
        print("match tie")
    elif p2=="Paper":
        print("p1 wins")
    elif p2=="Stone":
        print("p2 wins")
elif p1=="Paper":
    if p2=="Scissor":
        print("p2 wins")
    elif p2=="Paper":
        print("match tie")
    elif p2=="Stone":
        print("p1 wins")
else:
    print("lost game")
    

