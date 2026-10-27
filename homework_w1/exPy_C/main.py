name = input("Enter your name: ")
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

print("+++++ Screen +++++")
sum = n1 + n2
print(f"Hello {name}: \nthe sum of {n1} and {n2} is: {sum}")
dif = n1 - n2;
print(f"the difference of {n1} and {n2} is: {dif}")
multi = n1 * n2;
print(f"the multiplication of {n1} and {n2} is: {multi}")
if n2 != 0:
    div = n1 / n2
    print(f"the division of {n1} and {n2} is: {div}")
else:
    print("Cannot divide by zero.")
