import math

adade_aval = int(input("adad avale khod ra vared konid: "))
adade_dovom = int(input("adad dovome khod ra vared konid: "))

op = input() 

if op == "+" :
    result = adade_aval + adade_dovom

if op == "-" : 
    result = adade_aval - adade_dovom

if op == "*" :
    result = adade_aval * adade_dovom

if op == "/" :
    if adade_dovom != 0 :
        result =  adade_aval / adade_dovom
    else:
        print("khataaa")

if op=="rad":
    result= math.sqrt(adade_aval)

if op=="sin":
    result= math.sin(adade_aval)

if op=="tan" :
    result= math.tan(adade_aval)

if op=="cos" :
    result= math.cos(adade_aval)

if op=="fac" :
    result= math.factorial(adade_aval) 
 

print (result) 


