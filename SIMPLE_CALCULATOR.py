total_numbers = int(input("ENTER HOW MANY NUMBERS ARE THERE: "))
numbers = []

for i in range(total_numbers):
    num = float(input(f"ENTER NUMBER {i + 1}: "))
    numbers.append(num)


def add(nums):
    result = 0
    for n in nums:
        result += n
    return result


def subtract(nums):
    result = nums[0]
    for n in nums[1:]:
        result -= n
    return result


def multiply(nums):
    result = 1
    for n in nums:
        result *= n
    return result


def divide(nums):
    result = nums[0]
    for n in nums[1:]:
        if n == 0:
            return "ERROR: Division by zero"
        result /= n
    return result


print("\n1) Addition")
print("2) Subtraction")
print("3) Multiplication")
print("4) Division")
print("5) Do All")

command = input("ENTER WHAT YOU WANT TO DO: ")

if command == '1':
    print("RESULT:", add(numbers))
elif command == '2':
    print("RESULT:", subtract(numbers))
elif command == '3':
    print("RESULT:", multiply(numbers))
elif command == '4':
    print("RESULT:", divide(numbers))
elif command == '5':
    print("ADD:", add(numbers))
    print("SUB:", subtract(numbers))
    print("MUL:", multiply(numbers))
    print("DIV:", divide(numbers))
else:
    print("INVALID INPUT")
