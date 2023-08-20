def sum(f1,f2):
    result = {}
    result['s'] = (f1['s'] * f2['m']) + (f2['s'] * f1['m'])
    result['m'] = f1['m'] * f2['m']
    return result

def multiply(f1,f2):
    result = {}
    result['s'] = f1['s'] * f2['s']
    result['m'] = f1['m'] * f2['m']
    return result

def differentiation(f1,f2):
    result = {}
    result['s'] = (f1['s'] * f2['m']) - (f2['s']*f1['m'])
    result['m'] = f1['m'] * f2['m']
    return result

def division(f1,f2):
    result = {}
    result['s'] = f1['s'] * f2['m']
    result['m'] = f1['m'] * f2['s']
    return result

def show(r):
    print(f"The answer is: {r['s']}/{r['m']}")

print("*Menu*")
print("1- Sum")
print("2 - Multiply")
print("3- Differentiation")
print("4- Division")
choice = int(input("Choose operation:"))

s1 = int(input("Enter s of f1:"))
m1 = int(input("Enter m of f1:"))
s2 = int(input("Enter s of f2:"))
m2 = int(input("Enter m of f2:"))

f1 = {'s':s1 , 'm':m1}
f2 = {'s':s2, 'm':m2}

if choice == 1:
    result_s = sum(f1, f2)
    show(result_s)
    
elif choice == 2:
    result_m = multiply(f1,f2)
    show(result_m)
    
elif choice ==3:
    result_diff = differentiation(f1,f2)
    show(result_diff)

elif choice ==4:
    result_div = division(f1,f2)
    show(result_div)
