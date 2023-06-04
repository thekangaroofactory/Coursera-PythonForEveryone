largest = None
smallest = None

while True:
    num = input("Enter a number: ")

    # -- check
    if num == "done":
        break

    # -- check
    try:
        num = int(num)
    except:
        print("Invalid input")
        continue

    # -- init
    if largest is None:
        largest = num
    else:
        if num > largest:
            largest = num
    if smallest is None:
        smallest = num
    else:
        if num < smallest:
            smallest = num


print("Maximum is", largest)
print("Minimum is", smallest)