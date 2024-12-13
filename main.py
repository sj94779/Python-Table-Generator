from tabulate import tabulate
data = [["Name", "Place", "Gender"], ["Aman", "New Delhi", "Male"], ["Hritika", "New Delhi", "Female"], ["Krishna", "UP", "Male"]]
print(tabulate(data))

print(tabulate(data, headers='firstrow'))

print(tabulate(data, headers='firstrow', tablefmt='grid'))

print(tabulate(data, headers='firstrow', tablefmt='fancy_grid'))




