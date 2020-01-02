filePath = "q20data.txt"
wordList = []
wordCount = 0

# Read lines into a list
file = open(filePath, 'r')
for line in file:
    for word in line.split():
        wordList.append(word)
        wordCount += 1
x = 3
filePath1 = "q20text.txt"
wordList1 = []
wordCount1 = 0
# Read lines into a list
file1 = open(filePath1, 'r')
for line in file1:
    for word in line.split(','):
        wordList1.append(word)
        wordCount1 += 1
y = 3
for x in range(3, 4):
    print("\n{}".format(wordList1[y]) + "{} ".format(wordList[x]))
    print(
        "{}".format(wordList1[y + 1]) + "{} ".format(wordList[x + 1]) + "{} ".format(wordList1[y + 2]) + "{} ".format(
            wordList[x + 2]))

for x in range(6, 7):
    print("\n{}".format(wordList1[y]) + "{} ".format(wordList[x]))
    print(
        "{}".format(wordList1[y + 1]) + "{} ".format(wordList[x + 1]) + "{} ".format(wordList1[y + 2]) + "{} ".format(
            wordList[x + 2]))

for x in range(9, 10):
    print("\n{}".format(wordList1[y]) + "{} ".format(wordList[x]))
    print(
        "{}".format(wordList1[y + 1]) + "{} ".format(wordList[x + 1]) + "{} ".format(wordList1[y + 2]) + "{} ".format(
            wordList[x + 2]))
