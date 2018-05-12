count = 0
total = 0
while True:
    test = input("Enter a number: ")
    if test == "done" : 
        break
    try:
        num = float(test)
    except:
        print("Invalid input")
        continue
    count = count + 1
    total = total + num
print("")
print("Sum is", total)
print("Count is", count)
print("Average is", total/count)
largest = None
smallest = None
while True:
    test = input("Enter a number: ")
    if test == "done" : break
    try:
        num = float(test)
    except:
        print("Invalid input")
        continue
    if smallest is None or num < smallest:
	    smallest = num
    if largest is None or num > largest:
	    largest = num    

print("Maximum is", largest)
print("Minimum is", smallest)