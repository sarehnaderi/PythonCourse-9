def sum(d1,d2):
    result = {}
    result['h'] = day_1['h'] + day_2['h']
    result['m'] = day_1['m'] + day_2['m']
    result['s'] = day_1['s'] + day_2['s']
    
    if result['s'] >= 60:
        result['s'] -= 60
        result['m'] += 1

    if result['m'] >= 60:
        result['m'] -= 60
        result['h'] += 1
    return result

def differentiation(d1,d2):
    result = {}
    result['h'] = day_1['h'] - day_2['h']
    result['m'] = day_1['m'] - day_2['m']
    result['s'] = day_1['s'] - day_2['s']

    if result['s'] < 0:
        result['s'] += 60
        result['m'] -= 1
        if result['m'] <= 0:
            result['m'] += 60
            result['h'] -= 1

    if result['m'] < 0:
        result['m'] += 60
        result['h'] -= 1
    return result

def show(result):
    print(f"Result : {result['h']} : {result['m']} : {result['s']}")

print("*Menu*")
print("1- Total time")
print("2- Time difference")
choice = input("Enter your required operation:")

hour_1 = int(input("Enter hour'1':"))
minute_1 = int(input("Enter minute'1':"))
second_1 = int(input("Enter second '1':"))
hour_2 = int(input("Enter hour'2':"))
minute_2 = int(input("Enter minute'2':"))
second_2 = int(input("Enter second '2':"))

day_1 = {'h':hour_1, 'm':minute_1, 's':second_1}
day_2 = {'h':hour_2, 'm':minute_2, 's':second_2}


if choice =='1':
    total = sum(day_1, day_2)
    show(total)
elif choice =='2':
    difference = differentiation(day_1,day_2)
    show(difference)
