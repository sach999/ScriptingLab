import operator
from functools import reduce
from collections import Counter

counts = []


def wordCount(fname):
    with open(fname) as f:
        # word count
        s = Counter(f.read().split())
        print(s)

        # Ascending order
        arr = sorted(s.items(), key=operator.itemgetter(1), reverse=True)
        print(arr)
        for i in range(0, 10):
            print(arr[i])

        #Storing in array
        for j in s:
            counts.append(s[j])
        print(counts)

        # Average using lambda function
        print("Average: ", reduce(lambda a, b: a+b, counts)/len(counts))

        # One line comprehension to find square
        m = [x*x for x in counts if x % 2 != 0]
        print(m)


wordCount("sample.txt")
