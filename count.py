count = dict()

names = ['mk', 'mahin', 'khan', 'Abdulla']

for name in names:
    count[name] = count.get(name, 0) +1;
    
print(count)