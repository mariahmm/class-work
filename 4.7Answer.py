def computegrade(score):
    if score >= 0.9:
        print("A") 
    elif score >= 0.8:
        print("B") 
    elif score >= 0.7:
        print("C") 
    elif score >= 0.6:
        print("D") 
    else:
        print("F") 	

try:
    entry = float(input('Enter 0.0 to 1.0: '))
    if entry >= 0.0 and entry <= 1.0:
        computegrade(entry)
    else:
        print("Bad score")
except:
    print("Bad score") 
    quit()
    