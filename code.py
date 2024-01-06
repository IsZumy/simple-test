import math

values = [41, 18, 21, 63, 2, 53, 5, 57, 60, 93, 28, 3, 90, 39, 80, 88, 49, 60, 26, 28]

print("{:<8} {:<8}".format("Index #", "Value"))
print("-" * 16)

# Use a loop to print rows in the table
for i, value in enumerate(values, start=1):
    print("{:<8} {:<8}".format(f"A{i}", value))

print()

categories = ["Alpha", "Beta", "Charlie"]
operations = [
    lambda x:  x[4] +  x[19],         # Operation for (A5 + A20)
    lambda x:  x[14] /  x[8],          # Operation for (A15/A7)
    lambda x:  x[12] * x[11]         # Operation for (A13*A12)
]

print("{:<12} {:<12}".format("Category", "Values"))
print("-" * 24)

for category, operation in zip(categories, operations):
    result_value = operation(values)
    print("{:<12} {:<12}".format(category, int(result_value)))
