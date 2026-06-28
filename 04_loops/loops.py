"""
04 - Loops (for / while)
------------------------
Loops let you repeat actions without rewriting code.
"""

# --- for loop over a range ---
for i in range(5):          # 0,1,2,3,4
    print("for-range:", i)

for i in range(2, 10, 2):   # start, stop, step -> 2,4,6,8
    print("stepped:", i)

# --- for loop over a list ---
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print("fruit:", fruit)

# --- for loop with index using enumerate ---
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# --- while loop ---
count = 0
while count < 5:
    print("while count:", count)
    count += 1

# --- break ---
for num in range(10):
    if num == 5:
        break
    print("break demo:", num)

# --- continue ---
for num in range(10):
    if num % 2 == 0:
        continue
    print("odd number:", num)

# --- else clause on loops (runs if loop completes without break) ---
for num in range(5):
    print("checking:", num)
else:
    print("Loop finished without break.")

# --- nested loops ---
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")

# --- while with else ---
n = 0
while n < 3:
    print("n is", n)
    n += 1
else:
    print("while loop done")

# --- Mini pattern: multiplication table ---
number = 5
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# --- Mini pattern: sum of list using a loop ---
numbers = [10, 20, 30, 40]
total = 0
for n in numbers:
    total += n
print("Total:", total)
