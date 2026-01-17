import time
t = time.strftime('%h:%M:%S')
hour = int(time.strftime('%H'))
hour = int(input("enter hour: "))
print(hour)

if (hour>=0 and hour<12):
    print("Good Morning")
elif (hour>=12 and hour<16):
    print("Good Afternoon")
elif (hour>=16 and hour<21):
    print("Good night")