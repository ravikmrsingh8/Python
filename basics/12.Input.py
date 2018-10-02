name = input("Name:")
age = int(input("Age:"))
salary = float(input("Salary:"))

print("Hello: ", name)
print("Age: ", age)
print("Salary: ", salary)


#pass input as 1 2 3 4
x = map(int, input().split())
print("[", end="")
for item in x:
    print(item, end=", ")
print("]")

