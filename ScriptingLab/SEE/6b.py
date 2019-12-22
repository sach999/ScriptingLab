from operator import itemgetter

sentences = []


class rev:
    def __init__(self, sentence):
        self.sentence = sentence

    def reverse(self):
        temp = ""
        temparr = []
        temparr = self.sentence.split(" ")
        temparr.reverse()

        for i in temparr:
            temp = temp+i+" "

        count = 0
        for i in range(0, len(temp)):
            ch = temp[i]
            if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
                count = count + 1
        sentences.append({"count": count, "sentence": temp})


s1 = rev(input("Enter string 1: "))
s1.reverse()

s2 = rev(input("Enter string 2: "))
s2.reverse()

s3 = rev(input("Enter string 3: "))
s3.reverse()

sortedArr = sorted(sentences, key=itemgetter('count'), reverse=True)

print(sortedArr)

for s in sortedArr:
    print(s["sentence"])
