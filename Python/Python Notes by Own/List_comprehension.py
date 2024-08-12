mystr = 'darshan'
mylist = []
for c in mystr:
    mylist.append(c)

print(mylist)
print("")
# Syntax ::
print("Syntax ::")
mylist = [c for c in 'darshan']
print(mylist)
print("")
# list of square from 1 to 10 ::
print("list of square from 1 to 10 ::")
mylist = []
for i in range(1,11):
    mylist.append(i**2)

print(mylist)
print("")
# list of square from 1 to 10 
print("list of square from 1 to 10 ::")
mylist = [i**2 for i in range(1,11)]
print(mylist)
print("")
# leapYears ::
print("leapYears ::")
leapYears = [i for i in range(1980,2021) if i%4==0]
print(leapYears)
