import itertools as its
import string

def createDict(path,repeats,words):
	dict = its.product(words,repeat=repeats) 
	'''The words here are the strings to be iterated, the repeats are the generated password lengths, and the generated dict is an iterator that returns the tuples'''
	f = open(path,'a')
	for cipher in dict:
		f.write(''.join(cipher) + '\n')
	f.close()

def main():
	numbers = string.digits  # 0-9 string
	path = 'dictionary.txt'
	length =  4 #độ dài của passwword
	for i in range(1,length):
		createDict(path,i,numbers)

if __name__=="__main__":
	main()
