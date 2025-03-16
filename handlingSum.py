import re
filename = input("Enter file name: ")
t_sum=0
if filename:
    handle = open(filename)
else:
    handle =open("regex_sum_2155928.txt")
    
    
for l in handle:
    line = l.rstrip()
    x =re.findall('[0-9]+',line)
    t_sum += sum(int(num) for num in x)
    
    
print("The sum is ", t_sum)    
    