tuple1=tuple(('Sandeep',1,2,3,5,('Books','Mobile','Laptop')))
print(tuple1)

addTuple=("Mouse",)
tuple1+=addTuple
print(tuple1)

tuple1=list(tuple1)
tuple1.remove("Sandeep")
#print(tuple1)
tuple1=tuple(tuple1)
print(tuple1[5])

t1="Sandeep Kumar".split(" ")
print(t1)

#salary=int(input("Enter your salary "))
#yoservice=int(input("Years of service"))

#if yoservice>5:
#    salary=salary+(salary*.5)
#    print("You are eligible for bonus {0} .".format(salary))
#else:
#    print("You are not eligible..")


#lenght=int(input("Enter lenght :"))
#breath=int(input("Enter breath:"))

#if lenght==breath:
#    print("It's SQUARE.")
#    if lenght>=5 and lenght<=10:
#        print("Square of 5 CM")
#    else:
#        print("Square of some other value")
#else:
#    print("Its not SQUARE.")


for i in range(1,9):
    print(i)

for i in range(1,21):
    if i%2!=0:
        print("odd {0}".format(i))
    
for i in range(1,7):
    for j in range(1,i):
        print(j,end=' ')
    print("\n")

i=1
while i<=10:
    print(2*i)
    #i=i+1
    i+=1

myBook_Store=['7 Habits','Meluha','Python','You can win','Wining Digital Age']
myBook_Store.sort()
print(myBook_Store)

employeeDeatils={
        "Employeeid":"E001",
        "EmpName":"Sandeep Kumar",
        "EmpDesignation":"Data Analyst ",
        "EmpSalary":50000,
        "EmpAge":30,
    
}

print(employeeDeatils.keys())
print(employeeDeatils.values())

for i in employeeDeatils.values():
    print(i)


