from unittest import result
from xml.sax.saxutils import prepare_input_source


w=float(input("vazn khod ra avared nmaeid: ")) 
h=float(input("lotfan ghad khod ra vared namaeid: ")) 

bmi = w / (h**2)

print(bmi)

if  35 < bmi :
    print("extrwmwly obese") 

if  30 < bmi < 34.9 :
    print("obese")
    
if  25 < bmi < 29.9 :
    print("overweight") 
     
if 18.5 < bmi < 24.9 : 
    print("normal") 
    
if bmi < 18.5 :
    print("underweight")

    