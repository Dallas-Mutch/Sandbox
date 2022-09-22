MIN = 3

password = input("> ")
while len(password) < MIN:
    print("Password wrong")
    password = input("> ")
for i in range(len(password)):
    print("*", end='')
print()

