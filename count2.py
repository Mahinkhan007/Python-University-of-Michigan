fname = input('Enter file name: ')
handle = open(fname)

counts = {}
for line in handle :
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
        
        
bigcounts = None
bigwords = None

for word, count in counts.items():
    if bigcounts is None or count> bigcounts :
        bigcounts = count
        bigwords = word
        
print(bigwords,bigcounts)
