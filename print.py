print("Hello World") #this is comment and line for print python language 
print(f"Heloo world") 
"""This is the function that is used to print in python language and 
diffenece in this is the f-string in python language """

# there are diffrent types of printing in python 
# 1. print() function 
# 2. f-string 
# 3. formatted string 
# 4. raw string 
# 5. repr string 
# 6. print method (print("Hello World").)

# Sample variables for demonstration
name = "Alice"
age = 25
price = 19.99

# ----------------------------------------------------
# 1. Basic print() function
# ----------------------------------------------------
# Standard print
print("1. Basic print: Hello World")

# Printing multiple arguments (separated by space by default)
print("1. Multiple arguments:", name, "is", age, "years old.")

# Custom separator (sep) and ending (end)
print("1. Custom separator (sep=' | '):", end=" ")
print(name, age, price, sep=" | ")
print("1. Custom end (end=' -> '):", "Part 1", end=" -> ")
print("Part 2 (continued on same line)\n")

# ----------------------------------------------------
# 2. String Concatenation (+)
# ----------------------------------------------------
print("2. Concatenation: " + name + " is " + str(age) + " years old.")

# ----------------------------------------------------
# 3. Old-style / printf % Formatting
# ----------------------------------------------------
# %s for string, %d for integer, %.2f for float
print("3. %%-formatting: %s is %d years old and item costs $%.2f" % (name, age, price))

# ----------------------------------------------------
# 4. str.format() Method
# ----------------------------------------------------
# Positional / empty braces
print("4. str.format() positional: {} is {} years old.".format(name, age))

# Index-based braces
print("4. str.format() indices: {0} loves Python. Again, {0} is {1}.".format(name, age))

# Keyword / named arguments
print("4. str.format() keywords: {n} costs ${p:.2f}.".format(n=name, p=price))

# ----------------------------------------------------
# 5. f-Strings (Formatted String Literals - Python 3.6+)
# ----------------------------------------------------
# Direct variable interpolation
print(f"5. f-string basic: {name} is {age} years old.")

# Expressions inside f-strings
print(f"5. f-string expression: Next year {name} will be {age + 1}.")

# Float formatting / number precision
print(f"5. f-string precision: Price with 2 decimal places: ${price:.2f}")

# Debug / self-documenting expression (Python 3.8+)
print(f"5. f-string debug: {name=}, {age=}")

# ----------------------------------------------------
# 6. Raw String (r"...")
# ----------------------------------------------------
# Treats backslashes as literal characters without interpreting escape sequences (\n, \t, etc.)
print(r"6. Raw string: C:\Users\name\new_folder\test.txt (escape sequences like \n are not executed)")

# ----------------------------------------------------
# 7. repr() String / Debug Representation
# ----------------------------------------------------
# Shows the formal representation (quotes, escape sequences, object details)
text = "Hello\nWorld"
print("7. Regular print:\n" + text)
print("7. repr() function:", repr(text))
print(f"7. f-string with !r conversion: {text!r}")

# ----------------------------------------------------
# 8. Multi-line Strings (Triple Quotes """ or ''')
# ----------------------------------------------------
multiline = """8. Multi-line string:
   Line 1: Python
   Line 2: Printing
   Line 3: Styles"""
print(multiline)

# ----------------------------------------------------
# 9. Unpacking with * (Print items from list/tuple)
# ----------------------------------------------------
fruits = ["Apple", "Banana", "Cherry"]
print("9. Unpacking list elements (*):", end=" ")
print(*fruits, sep=", ")

# ----------------------------------------------------
# 10. Template Strings (string.Template)
# ----------------------------------------------------
from string import Template
template = Template("10. Template string: Hello, $name! You have $$100.")
print(template.substitute(name=name))

# ----------------------------------------------------
# 11. Low-level printing via sys.stdout.write()
# ----------------------------------------------------
import sys
sys.stdout.write("11. sys.stdout.write: Direct output without automatic newline.\n")

# ----------------------------------------------------
# 12. Pretty Print (pprint module)
# ----------------------------------------------------
from pprint import pprint
data = {
    "user": {"name": "Alice", "age": 25},
    "skills": ["Python", "Machine Learning", "Data Analysis"],
    "active": True
}
print("12. pprint (Pretty Print) for structured data:")
pprint(data)

# ----------------------------------------------------
# 13. ANSI Colored / Styled Output in Terminal
# ----------------------------------------------------
# \033[1m = Bold, \033[32m = Green, \033[31m = Red, \033[0m = Reset
print("\033[1;32m13. ANSI style: Bold Green Text\033[0m and \033[1;31mBold Red Text\033[0m")
