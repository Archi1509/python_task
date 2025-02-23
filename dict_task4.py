def employee_sales(data):
    highest_sale = {name: sale for name, sale in sorted(employee_sales_data.items(), key=lambda ele: ele[1], reverse=True)}
    highest_sale_employee = (list(highest_sale.keys())[:1])
    top_three_employee = dict(list(highest_sale.items())[:3])
    print(highest_sale_employee)
    print(top_three_employee)


employee_sales_data = {
    "Alice": 5000,
    "Bob": 7500,
    "Charlie": 4200,
    "Diana": 9100,
    "Ethan": 6200
}
employee_sales(employee_sales_data)

