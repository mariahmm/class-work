fname = input('Enter the file name: ')
count = 0
try:
    fhand = open(fname)
except:
    if fname == "NA NA BOO BOO":
        print("NA NA BOO BOO TO YOU - You've been punked!")
    else:
        print("File cannot be opened: ", fname)
    quit()    
for line in fhand:
    if line.startswith('Subject:') :
        count = count + 1
output = "There were {0} subject lines in {1}.".format(str(count), fname )
print(output)
