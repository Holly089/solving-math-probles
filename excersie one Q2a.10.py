#Holly McClelland
#17/7/20
#data420 scalable data science
#excerise one Q2a.10

primes = [2,3]

numbers = list(range(1,2000001))

for num in numbers:
    dividers = list(range(2,num-1))
    count = 0
    for divider in dividers:
        if num % divider != 0:
            count += 1
            if count == len(dividers):
                primes.append(num)

            
print(sum(primes))