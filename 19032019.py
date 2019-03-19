# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 10:54:44 2019

@author: Meister_S10
"""
"""
#write a function
x=input("enter string:")
s=0
a='0123456789'
y=0
for i in x.split():
    if i in a:
        y=int(i)
        s=s+y
    
print(s)


#create a function to replace 
x="adarsh is boy adarsh"
x1="pagal"
for i in x.split():
    print(i.replace("boy","pagal"), end=" ")
    



string="adarsh is a boy"
print(string.replace("boy","pagal"))







"""
#dealing with classess
class student:
  def __init__(self, name,roll_no,branch):
    self.name = name
    self.roll_no = roll_no
    self.branch=branch
    
  def grade(self,marks):
      self.marks=marks
      
      if(marks<=100 and marks>90):
          grade="A"
      elif(marks<=90 and marks>80):
          grade="B"
      elif(marks<=80 and marks>70):
          grade="C"
      elif(marks<=70 and marks>60):
          grade="D"
      elif(marks<=60 and marks>50):
          grade="E"
      else:
          grade="F"
                          
                              
      return grade
    
  
    
    
p1 = student("MEISTER", 180101276,"B.Tech")

print(p1.name)
print(p1.roll_no)
print(p1.branch)
print(p1.grade(100))



