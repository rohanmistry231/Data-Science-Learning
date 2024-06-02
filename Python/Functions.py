# Syntax ::
print("Syntax ::")
def seperator():
    print('=======================')

print("Hello world")
seperator()
print("from darshan collage")
seperator()
print("rajkot\n")

# Passing parameter ::

print("Passing parameter ::")
def seperators(type):
    if (type=='='):
        print("=======================")
    elif (type=='*'):
        print("***********************")
    else :
        print('&&&&&&&&&&&&&&&&&&&&&&&')

print("Hello world")
seperators('=')
print("from darshan collage")
seperators('*')
print("rajkot\n")

# List later in this chapter ::

print("List later in this chapter ::")
def setName(name) :
    name[0] = 'arjun bala'

name = ["Default"]
setName(name)
print(name)
print("")
# keyword arguments ::

print('Keyword arguments ::')
def collageDetails(collageName , state):
    print(collageName + " is located in " + state)

collageDetails(state='Gujarat', collageName='Darshan')
print("")
# Default value ::

print("Default value ::")
def collageDetail(_collageName , _state='Gujarat'):
    print(_collageName + " is located in " + _state)

collageDetail(_collageName='Darshan')
print("")
# Arbitery arguments :: 

print("Arbitery arguments ::")
def collageList(*collages):
    print(collages[0])
    # we can also loop through all the arguments
    # for c in collages :
    #   print(c)

collageList('darshan','nirma','vvp')
print("")

# Arbitery keyword arguments ::

print("Arbitery keyword arguments ::")
def collageDetailss(**collage):
    print('collage name is ' + collage['name'])

collageDetailss(city='rajkot',state='Gujarat',name='Darshan')
print("")
# return statement ::

print("return statement ::")
def addition(n1,n2):
    return n1 + n2

ans = addition(10,5)
print(ans)
