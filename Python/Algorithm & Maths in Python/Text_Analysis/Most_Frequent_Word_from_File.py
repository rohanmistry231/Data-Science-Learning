name = input('Enter the name of file to be read: ')
fhandle = open(name,'r')

# Initialize a dictionary
counts = dict()

for line in fhandle:
	words = line.split()
	for word in words:
		counts[word.lower()]=counts.get(word.lower(),0)+1

# Set initial counter variables
bigcount = None
bigword = None
# Common words' list
common_words = ['i','in','the','a','an','to','is','are','on','yes','no',
				'not','he','she','you','I','my','me','at','of','so','but',
				'it','as','if','for','oh','him','her','them','and','all',
				'this','that','those','these','his','her','was','had','get',
				'have','has','with','up','down','out','when','where','how',
				'then','now']

"""
Loop through the items of the dictionary with Tuple Unpacking. Ignore the common words (if you like)
If the word count is higher than the running count, set it to the count and set the word to the 'bigword' variable 
"""
for word,count in counts.items():
	if word not in common_words :
		if bigcount is None or count > bigcount:
			bigword = word
			bigcount = count

print(f"Most frequent word is '{bigword.upper()}', with frequency of {bigcount}")

# Now prints the most frequenct N words

top_N = int(input("How many most freqently used owrds do you want to display: "))

tmplst = []
for key,val in counts.items():
	if key not in common_words:
		# Store the value first and then key (later used for sorting)
		newtup = (val,key)
		tmplst.append(newtup)

# Sort the list by 'value' i.e. word count
tmplst=sorted(tmplst,reverse=True)

for val,key in tmplst[:top_N]:
	print(f"{key}:{val}")