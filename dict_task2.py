def total_sales(data):
    total_sales = {}
    for store, sell in sales_data.items():
        for item, count in sell.items():
            if item in total_sales:
                total_sales[item] += count
            else:
                total_sales[item] = count

    print(total_sales)
    return total_sales


def desending_order_store(data):
    highest_sale = {}
    for store, sell in sales_data.items():
        for item, count in sell.items():
            if store in highest_sale:
                highest_sale[store] += count
            else:
                highest_sale[store] = count
    highest_sale = {key: value for key, value in sorted(highest_sale.items(), key=lambda ele: ele[1], reverse=True)}
    print(highest_sale)
    return highest_sale


def highest_selling_store(highest_sale):
    highest_sale = {key: value for key, value in sorted(highest_sale.items(), key=lambda ele: ele[1], reverse=True)}
    highest_store = dict(list(highest_sale.items())[:1])
    print("Store with Highest Total Sales:",highest_store)


def best_selling_product(best_sell):
    best_selling_product=dict(list(best_sell.items())[:1])
    print("Best-Selling Product:",best_selling_product)


sales_data = {
    "Store_A": {
        "Laptop": 15,
        "Phone": 30,
        "Tablet": 10
    },
    "Store_B": {
        "Laptop": 25,
        "Phone": 20,
        "Tablet": 15
    },
    "Store_C": {
        "Laptop": 10,
        "Phone": 35,
        "Tablet": 5
    }
}

t=total_sales(sales_data)

best_selling_product(t)
d=desending_order_store(sales_data)
highest_selling_store(d)












