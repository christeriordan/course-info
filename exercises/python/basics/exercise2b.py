d = {"Adam": 95, "Lisa": 85, "Bart": 59, "Paul": 74}

sum = 0
for i in d.values():
    sum += i

avarage = sum / len(d)
print("The avarage score is : ", avarage)

maximum = max(d.values())
print("The highest score is : ", maximum)

minimum = min(d.values())
print("The lowest score is: ", minimum)




