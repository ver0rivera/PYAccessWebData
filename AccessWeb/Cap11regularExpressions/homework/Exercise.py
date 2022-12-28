import re

hand = open("GoodText.txt")

numbersList = []
for line in hand:
    line = line.rstrip()
    numbersToSum = re.findall("([0-9]+)", line)
    if len(numbersToSum) < 1:
        continue
    for i in range(len(numbersToSum)):
        totalNumbers = numbersToSum[i]
        numbersINT = int(totalNumbers)
        numbersList.append(numbersINT)
total = sum(numbersList)
print(total)
