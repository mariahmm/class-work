def computepay(hours,rate):
    if hours > 40:
        pay = hours * rate + (hours - 40) * rate * 0.5
    else:
        pay = hours * rate
    return pay

try:
    hours = float(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))
except:
    print("")
    print("Both entries must be numbers")
    quit()

total = computepay(hours,rate)
print("")
print("Pay $",total)
