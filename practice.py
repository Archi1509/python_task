# from collections import Counter
#
# def duplicate_characters(Word):
#     char=[]
#     char_count=Counter(Word)
#     for k,v in char_count.items():
#         if v>1:
#             char.append(k)
#     return char
# s="geeksofgeeks"
# characters=duplicate_characters(s)
# print(characters)



# from collections import Counter
# def group_similar_items(a):
#     count=Counter(a)
#     grouped = {key: [key] * value for key, value in count.items()}
#     return grouped
# a=['apple','banana','apple','orange','banana']
# c=group_similar_items(a)
# print(c)


test_dict = {'Gfg': {'a': [1, 3], 'b': [3, 6], 'c': [6, 7, 8]},
             'Best': {'a': [7, 9], 'b': [5, 3, 2], 'd': [0, 1, 0]}}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Swapping Hierarchy in Nested Dictionaries
# Using loop + items()
res = dict()
for key, val in test_dict.items():
    for key_in, val_in in val.items():
        if key_in not in res:
            temp = dict()
        else:
            temp = res[key_in]
        temp[key] = val_in
        res[key_in] = temp

# printing result
print("The rearranged dictionary : " + str(res))
