"while loop"

i, num = 0, []

while i < 6:
    print(f"At the top i is {i}")
    num.append(i)

    i += 1
    print("Numbers now: ", num)
    print(f"At the bottom i {i}")

print("The numbers: ")
for n in num:
    print(n)
