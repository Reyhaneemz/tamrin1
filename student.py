from ast import If


name = input("name khod ra vared konid: ")
family = input("famile khod ra vared konid: ") 
nomre1 = float(input("nomre aval: ")) 
nomre2 = float(input("nomre dovom: ")) 
nomre3 = float(input("nomre sevom: ")) 

average = (nomre1 + nomre2 + nomre3) / 3

 
if average >= 17: 
     result= "great"

if average < 17 and 12 >= average:
    result =  "normal" 

if average < 12:
    result = "fail" 

print(result)
