

largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break

    try:
        num = float(num)

    except:
        print("Enter a valid Number or just enter 'done' !!!")
        continue

    if largest == None and smallest == None:
        largest = num
        smallest = num

    if num > largest:
        largest = num

    if smallest > num:
        smallest = num

print("Maximum ", largest)
print("Minimum ", smallest)
