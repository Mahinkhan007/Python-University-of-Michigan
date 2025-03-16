import re

# hand = open('mbox-short.txt')


# if hand is not None:
#     for line in hand:
#         line = line.rstrip()
#         if re.search(r'^X.*: ', line):
#             print(line)
            
            
x = 'From I am a multimple: word A of 12 jd 45: ms das 0324 lorel d'

y = re.findall('[0-9]+', x)
print(y)

z = re.findall('[AEIOU]+', x)

print(z)

a = re.findall('^F.+:', x)  #be greedy take all  . is any character 
print(a)

b= re.findall('^F.+?:', x) #? is not greedy
print(b)
c = 'From abc@xxxxxxxx.com 5:34 PM adfdff'
d= re.findall('^From (\S+@\S+)', c)
print(d)


