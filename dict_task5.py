def percentage(a,t):
    return f"{(a/t)*100}%"
def complaints_data(data):
    highest_complaints={key:value for key,value in sorted(complaints.items(),key=lambda ele:ele[1],reverse=True)}
    highest_complaints_name=dict(list(highest_complaints.items())[:1])
    print(highest_complaints_name)
    total=0
    for value in complaints.values():
        total+=value
    percentage_complaints_data={}
    for complaint,count in complaints.items():
        if complaint not in percentage_complaints_data:
            percentage_complaints_data[complaint]=percentage(count,total)
    print(percentage_complaints_data)

complaints = {
    "Late Delivery": 120,
    "Damaged Product": 95,
    "Wrong Item": 60,
    "Customer Service": 75,
    "Billing Issues": 50
}
complaints_data(complaints)