# Name: ABDUL AIDIL SHAH BIN AJIBIR, Class: C02
# This program accepts 5 integer values from the user and is stored in a list.

def accept_five_integer():
    number = []
    
    for i in range(1, 6):
        integer = int(input(f"Enter number {i}: "))
        number.append(integer)

    ascending = sorted(number)
    sum_of_all_number = sum(number)
    largest = max(number)

    print("Numbers in ascending order:", ascending)
    print("Sum of all numbers:", sum_of_all_number)
    print("Largest number:", largest)
    print()
    print("=== Code Execution Successful ===")

accept_five_integer()
