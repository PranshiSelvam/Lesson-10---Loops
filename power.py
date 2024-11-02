
def calculate_power(base, exponent):
    result = base ** exponent
    return result

base = float(input("Enter the base number: "))
exponent = int(input("Enter the exponent (power): "))

result = calculate_power(base, exponent)
print(f"{base} raised to the power of {exponent} is: {result}")
