# Data type : 
""" python is loosley typed language therefor no need to define the datatype of Variables
    no need to declare variables before using them in code.

    Datatypes: immutable and mutable
    immutable - 1 number
                2 string
                3 tuples
    
    mutable   - 1 list
                2 dictionaries
                3 set

"""
x=11
y=11.26
# String : It is useful thing of a string as an ordered sequence
string="Sandeep"
print(x)
print(y)
print(string)
# In python we can change the type of expresion in python this is called typecasting
# We can convert them into float and vise versa
print(float(x))
print(int(y))
print("================================\n")
# len() command is used to obtain the lenght of string
print(len(string))
name="Sandeep Kumar"
# As string stored as sequesnce or in array form we can fetch each elements or each character from string using slicing methods
# if we want to get each 2 character
print(name[::2])
# to get the character from a certain position (starting from 0 till 5,each 2nd)
print(name[0:5:2])
# string is immutable
# name[0]='x' # we get an item assigment error

# escape sequence character - escape sequence are strings that are difficutl to input
print("for new line \n")
print("for tab \t")
print("for slace \\")

print(name.upper())
print(name.lower())
print(name.replace("e","i",2))
print(name.split(" "))

# tuple
# tuples are data struckture that store an ordered sequence of values
# tuples are immutable, this means you can not change the values
# tuples can be defined using parenthesis ()

print("===============================================")
name=("Sandeep","Kumar",'Singh')

# join function - it work with strings
"""Concatenate any number of strings.

The string whose method is called is inserted in between each given string. The result is returned as a new string."""

print(".".join(name))
print("===========================")
name="Sandeep"
print(name.find('eep'))

mytuple=(1,2,3,4,5,6)
print(mytuple)

ice_cream_flavor=('Chocolate', 'Vanilla', 'Mint', 'Strawberry', 'Choc-Chip',[10,20])
print(ice_cream_flavor[0])
print(ice_cream_flavor[5])

print(ice_cream_flavor[-3])

print(ice_cream_flavor[1:4])

print("===================Conditional Statement (if...elif....else)=====================")
ss=" mY text  {}"
print("{0},{0},{1}".format("Test","Test1"))

if ice_cream_flavor[2]=='Mint':
    print("I Like {0} falavor most....!".format(ice_cream_flavor[2]))
else:
    print("I don't like any other flavor...!")

if ice_cream_flavor[1]!='Vanilla':
    if ice_cream_flavor[2]=='Mint':
        print("We got the mint flavor")
elif ice_cream_flavor[1]=='Vanilla':
    print("I would like to have Vanilla")
else:
    print("No match found....!")


for items in ice_cream_flavor:
    print(items)

my_favrate_books=['You can win','7 habits','the alchemist',[300,200,100],(1,2,3)]

print(my_favrate_books)
print("My favorate books name is {} and the price is {}...".format(my_favrate_books[1],my_favrate_books[3][1]))
print(my_favrate_books[4][2])

# Use sorted, pop, append and extend function

print(sorted([1,6,9,55,32,3,27]))
print(my_favrate_books.pop(3))

#my_favrate_books=my_favrate_books.pop(3)
#my_favrate_books=sorted(my_favrate_books)

print(my_favrate_books)

my_favrate_books[3]='Meluha by Amish'

print(my_favrate_books)
lst=['M','F']
my_favrate_books.append(lst)
print(my_favrate_books)
lst=[21,'M','F',21]
my_favrate_books.extend(lst)
print(my_favrate_books)

# List comprehension
# Normal way is append
 
new_lst=[2,3,4,5,6,7,8,9]
res=[]
for num in new_lst:
    if num%2==0:
        res.append(num)
print(res)

i=0
while i<len(new_lst):
    res.append(new_lst[i]**2)
    i+=1
print(res)

a=list([x%2==0 for x in new_lst])
print([x**2 for x in new_lst])

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")

numSequence=[1,2,3]
mapval=tuple(map(lambda x:x*2, numSequence))
print(mapval)

def mulby2(num):
    return num*2

newTuple=map(mulby2,numSequence)
newTuple=tuple(newTuple)
print(newTuple)

def mapExmple(*string):
    var=""
    for i in string:
        var+=i*2
    return var

result=mapExmple("T","E","X","T")
print(result)
exm_tuple=("T","E","X","T")

result=list(map(mapExmple,exm_tuple))
print(result)


print("-----End-----")