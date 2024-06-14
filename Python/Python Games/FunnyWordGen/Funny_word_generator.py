consonants = 'bcdfghjklmnprstvwxz'
vowels = 'aeiou'
consonants = list(consonants)
vowels = list(vowels)



Nwords = int (input("How many funny words do you want to generate?: "))
word_length = int(input("And what's the length of each word: "))
seed = int(input("Please enter an integer for seeding random sequence: "))
total_rnd = Nwords*word_length
import random
A = random.randint(20,50)
C = random.randint(100,200)
#print consonants
#print vowels

def linear_congruential_generator(a,c,m,seed,N):
	random = [seed]
	for i in range(1,N):
		random.append((a*a*random[i-1]+c)%m)
	for i in range(len(random)):
		random[i] = (random[i])/(max(random))
	#random.remove(random[0])
	return random


random = linear_congruential_generator(A,71,371,seed,total_rnd)
dice = [int(d*99) for d in random]

dict = []
lex = []

for i in range(len(dice)):
	count = 0
	letters =''
	if i%2==0:
		letters= letters+(consonants[dice[i]%19])
	else:
		letters = letters+(vowels[dice[i]%5])
	#count+=1
	dict.append(letters)

for i in range(0,len(dict)-word_length+1,word_length):
    
    words = ''
    for j in range(word_length):
       words = words+dict[i+j]
    lex.append(words)
 

print ("\nSome random funny sounding words are as follows: \n ------------------------------------------------\n", end='')
for i in range(len(lex)):
    print (lex[i], end=' ')
#print len(dict)
