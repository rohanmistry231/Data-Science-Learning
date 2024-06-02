#lambda function
def add(a,b):
    return a+b

a_plus_b_whole_square = lambda x,y:x*x+2*x*y+y*y
a_minus_b_whole_square = lambda x,y:x*x-2*x*y+y*y

print(a_plus_b_whole_square(1,2))
print(a_minus_b_whole_square(1,2))