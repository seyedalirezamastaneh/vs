import numpy as np


digits = list("0372280481")
unique_digits = sorted(set(digits))  
unique_digits = list(map(int, unique_digits))

print(f"بردار بدون تکرار: {unique_digits}")



needed = 10 * 10
repeats = (needed // len(unique_digits)) + 1  

full_list = (unique_digits * repeats)[:needed]  
matrix = np.array(full_list).reshape((10, 10))

print("\nماتریس ۱۰x۱۰ ساخته شده:")
print(matrix)


product = np.prod(matrix)  
summation = np.sum(matrix)  

print(f"\nحاصل ضرب همه عناصر ماتریس: {product}")
print(f"حاصل جمع همه عناصر ماتریس: {summation}")