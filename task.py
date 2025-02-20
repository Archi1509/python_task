from reportlab.lib.randomtext import subjects

marks_dict={
    'nilesh-geography': 89,
    'alpesh-history': 77,
    'shital-math': 93,
    'dimpal-hindi': 68,
    'nilesh-english': 74,
    'alpesh-sci': 85,
    'shital-history': 91,
    'dimpal-geography': 87,
    'nilesh-sci': 83,
    'alpesh-math': 92,
    'dimpal-english': 78,
    'shital-hindi': 81,
    'nilesh-history': 90,
    'alpesh-geography': 79,
    'dimpal-math': 84,
    'shital-sci': 88,
    'nilesh-hindi': 71,
    'alpesh-english': 80,
    'dimpal-sci': 89,
    'shital-geography': 82,
    'nilesh-math': 93,
    'alpesh-hindi': 75,
    'dimpal-history': 90,
    'shital-english': 87
}

total_marks={}
subject_count={}
for key,value in marks_dict.items():
    name,subject=key.split("-")
    if name in total_marks:
        total_marks[name]+=value
        subject_count[name]+=1
    else:
        total_marks[name]=value
        subject_count[name]=1


print(total_marks)
avg={name: total/subject_count[name] for name,total in total_marks.items()}
print(avg)

#for highest total marks
m=0
for key,value in total_marks.items():
    m=max(value,m)
    if m==value:
        name=key
print(f"highest marks are {m} of student {name}")

#subjectwise highest marks



subject_marks={}

for key,value in marks_dict.items():
    name,subject=key.split("-")
    current_max = value
    if subject in subject_marks:
        subject_marks[subject] = max(subject_marks[subject], current_max)

    else:
        subject_marks[subject]=value

print(subject_marks)
# subjects=[]
# subject_mark={}
# for key,value in marks_dict.items():#we get list of all subjetcs
#     name, subject = key.split("-")
#     if subject in subjects:
#         pass
#     else:
#         subjects.append(subject)
#
# new_dict=marks_dict.fromkeys(subjects,[]) #created dict of subject and empty list
#
# print(new_dict)
# # Group marks by subject
# for k, v in marks_dict.items():
#     name, subject = k.split("-")
#     if subject in new_dict:
#         if isinstance(v, list):
#             new_dict[subject].extend(v)  # Add marks to subject's list
#         else:
#             new_dict[subject].append(v)  # If it's not a list, append the single mark





#sorting
sorted_total_marks={key: value for key,value in sorted(total_marks.items(),key=lambda ele:ele[1],reverse=True)}
print(sorted_total_marks)




