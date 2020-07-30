#Holly McClelland
#17/7/20
#data420 scalable data science
#excerise one Q2a.1

from math import isclose

numbers = list(range(1, 101))
multiples = []

for number in numbers:
    if number % 3 == 0:
        multiples.append(number)
    if number % 5 == 0:
        multiples.append(number)    
        

print(sum(multiples))
