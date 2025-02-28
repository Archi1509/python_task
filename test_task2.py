from collections import Counter
from re import split

numbers = [4, 5, 6, 4, 7, 8, 5, 9, 4, 7, 6, 10]
duplicate_dict=dict(Counter(numbers))
for number,repeat in duplicate_dict.items():
    print(f"{number} appears {repeat} times")
print(duplicate_dict)

