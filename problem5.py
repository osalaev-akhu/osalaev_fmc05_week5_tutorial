"""
A student measures a plant’s height each day.

Write a program that:

Reads the number of days, n.
Reads n heights in centimetres, one at a time,
 and stores them in a list.
Prints each recorded height with its day number,
 starting from Day 1.
Prints the first height, the last height, and 
the change from the first to the last height.
Assume n is at least 1 and all heights are
 non-negative whole numbers.

Example 1
Input:

4
12
14
14
17

Output:

Day 1: 12 cm
Day 2: 14 cm
Day 3: 14 cm
Day 4: 17 cm
First height: 12 cm
Last height: 17 cm
Change: 5 cm
"""
n = int(input("enter the number of days: "))
measures = []
for i in range(n):
    m = int(input("Enter the measurement for next day:"))
    measures.append(m)

for i in range(n):
    print(f"Day {i+1}: {measures[i]} cm")

print(f"First height: {measures[0]} cm")
print(f"Last height: {measures[-1]} cm")
print(f"Change: {measures[-1] - measures[0]} cm")
