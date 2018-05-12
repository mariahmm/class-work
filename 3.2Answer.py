try:
    hours = float(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))
except:
    print("")
    print("Both entries must be numbers")
    quit()
if hours > 40:
    pay = hours * rate + (hours - 40) * rate * 0.5
else:
    pay = hours * rate
print("")
print("Pay $",pay)
