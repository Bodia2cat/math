import random

print("----------Simple--Math--test----------")
print("So, we start.....")
start = input("Press any button please......")
st = 0
mark = 0
while st < 12:
    a = random.randint(0, 20)
    b = random.randint(0, 10)
    print("So, ")
    print(str(a) + "*" + str(b))
    d = a * b
    c = input("Your answer: ")
    if str(d) == str(c):
        print("You are good")
        mark += 1
    else:
        print("You have mistace,  " + str(d) + " " + "Its correct answer")
        mark -= 1
    st += 1
print("Your mark is " + str(mark))
