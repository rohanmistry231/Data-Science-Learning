# list.append(element)::
print("list.append(element) ::")
my_list = ['darshan','institute','rajkot']
my_list.append('gujarat')
print(my_list)
print("")
# list.insert() ::
print("list.insert() ::")
my_list = ['darshan','institute','rajkot']
my_list.insert(2,'of')
my_list.insert(3,'engineering')
print(my_list)
print("")
# list.extend() ::
print("list.extend() ::")
my_list1 = ['darshan','institute']
my_list2 = ['rajkot','gujarat']
my_list1.extend(my_list2)
print(my_list1)
print("")
# list.pop() ::
print("list.pop ::")
my_list = ['darshan','institute','rajkot']
print(my_list.pop())
print(my_list)
print("")
# list.remove() ::
print("list.remove() ::")
my_list = ['darshan','institute','darshan','rajkot']
my_list.remove('darshan')
print(my_list)
print("")
# list.clear() ::
print("list.clear() ::")
my_list = ['darshan','institute','darshan','rajkot']
my_list.clear()
print(my_list)
print("")
# list.index() ::
print("list.index() ::")
my_list = ['darshan','institute','darshan','rajkot']
print(my_list.index('institute'))
print("")
# list.count() ::
print("list.count() ::")
my_list = ['darshan','institute','darshan','rajkot']
print(my_list.count('darshan'))
print("")
# list.reverse() ::
print("list.reverse() ::")
my_list = ['darshan','institute','darshan','rajkot']
my_list.reverse()
print(my_list)
print("")
# list.sort() ::
print("list.sort() ::")
my_list = ['darshan','collage', 'of' , 'engineering','rajkot']
my_list.sort()
print(my_list)
my_list.sort(reverse=True)
print(my_list)
print("")