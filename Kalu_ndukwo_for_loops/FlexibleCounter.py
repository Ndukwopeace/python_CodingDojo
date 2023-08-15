# flexible counter
multiple = []
lownum = 0
highnum = 50
mult = 3
# num = [lownum, highnum , mult]

for i in range (lownum,highnum-1):
    if i % mult == 0:
        multiple.append(i)
print (multiple)