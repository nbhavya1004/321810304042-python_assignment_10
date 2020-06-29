# 321810304042-python_assignment_10


# Bhavyasree N - 321810304042


##      1.      Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

for i in range(1,101):
	if(i%3==0):
	       print("fizz")
	       
	elif(i%5==0):
			print("buzz")
			
	elif(i%3==0 and i%5==0):
				print("fizzbuzz")
				
	else:
					print(i)
					
					
					
					
					
##       2.      Write a Python program to remove consecutive duplicates from list.

x=[1,2,2,3,3,3,4,4,4,5,5,5,6,6,6,8,1]
previous_value = None
new_lst = []

for elem in x:
   if elem != previous_value:
       new_lst.append(elem)
       previous_value = elem

print(new_lst)





##      3.     Write a python program to find unique element from a list.

list=[1,2,4,6,8,8,2,1]
uniqueitems=[]
dupitems=set()
for ele in list:
	if ele is not dupitems:
		uniqueitems.append(ele)
		dupitems.add(ele)
print(dupitems)





##      4.      Write a function that checks whether a number is in a given range (inclusive of high and low).

def  a(num,low,high):
    for i in range(low,high+1):
        if num==i:
            print('Number is within the range',)
            break
    else :
            print('Number is out of range')
a(4,5,10)





##      5.      Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

#Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'

#Expected Output : 

#No. of Upper case characters : 4

#No. of Lower case Characters : 33

#HINT: Two string methods that might prove useful .isupper()

def p(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

p('MYASSIGNMEnt')
