#Holly McClelland
#17/7/20
#data420 scalable data science
#excerise one Q2a.5


numbers = list(range(1,21))


lower = 2521
sucess = 0

if sucess != 20:
    for n in numbers:
    
        if lower % n == 0:
            sucess += 1                   

        else: 
            lower = lower * n
            sucess = 0

print("I found it! " + str(lower))    