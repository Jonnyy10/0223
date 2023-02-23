#!/usr/bin/env python
# coding: utf-8

# In[3]:


def input_student(student):
    student['name'] = input("Name : ")
    student['kor'] = int(input("Kor : "))
    student['eng'] = int(input("Eng : "))
    student['math'] = int(input("Math : "))

