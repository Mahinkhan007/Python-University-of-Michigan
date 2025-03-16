num = 0;
total = 0.0;

while True: 
    sval = input("Enter a number: ");
    if sval == 'Done' or sval == 'done':
        break;
    try:
        fval = float(sval);
    except:
        print("Invalid input");
        continue;
    num = num + 1;
    total += fval;
    

print(total, num, total/num);



# to process a file

# opentxt = open("file.txt", 'r')

# for line in opentxt:
#     line = line.rstrip(); #this is to avoid double line
#     if line.startswith('From: '):
#         print (line);
        
        