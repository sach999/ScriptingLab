#a) Read a list of inputs and create a new list having all the elements minus the duplicates . Use one line comprehension to create a new list of even numbers . Create another list reversing the elements.



def removeDuplicates(list1):

	for number in list1:
		if number not in list2:
			list2.append(number)
		


list1 = ["hello", "world", "hello", 8 , 8, 7, 7, 3]

list2 = []

removeDuplicates(list1)

print(list2)



s = [x**2 for x in range(10)] #Read elements to list , square of the number is saved in the list
print("Elements of s: ",s)

m = [x for x in s if x % 2 == 0] #Save the even number in list
print("Elements of m: ", m)

m.reverse()
print("Reversed elements of m: ", m)


#Frequency of words in a given file
from collections import Counter

def wordCount(fname):
	with open(fname) as f:
		return Counter(f.read().split())

print("Number of words in the file: ",wordCount("test.txt"))

