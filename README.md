# Python: Handling ZeroDivisionError when calculating the average of an empty list

This repository demonstrates a common error in Python: dividing by zero when calculating the average of an empty list. The solution involves adding a check to handle the case where the input list is empty. 

## Bug
The provided code `bug.py` attempts to calculate the average of a list of numbers. However, it fails when the input list is empty because it tries to divide by zero.

## Solution
The solution in `bugSolution.py` addresses this by first checking if the list is empty. If it's empty, the function returns 0; otherwise, it calculates the average as usual.