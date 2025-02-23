def multiply(x, y):
    return x * y

def revenue_per_store(sale_data,product_data):

    store_sale_product_price = {}
    revenue_per_store={}
    for store, sell in sales_data.items():
        sale_product_price = {}
        for product, count in sell.items():
            if product in product_prices.keys():
                sale_product_price[product] = multiply(product_prices.get(product),
                                                       (sales_data.get(store).get(product)))
        store_sale_product_price[store] = sale_product_price
    for store,sell in store_sale_product_price.items():
        for product,price in sell.items():
            if store not in revenue_per_store.keys():
                revenue_per_store[store]=price
            else:
                revenue_per_store[store]+=price

    print(revenue_per_store)
    highest_sale_store={key:value for key,value in sorted(revenue_per_store.items(),key=lambda ele:ele[1],reverse=True)}
    highest_store=dict(list(highest_sale_store.items())[:1])
    print(highest_store)

sales_data = {
    "Store_A": {"Laptop": 15, "Phone": 30, "Tablet": 10},
    "Store_B": {"Laptop": 25, "Phone": 20, "Tablet": 15},
    "Store_C": {"Laptop": 10, "Phone": 35, "Tablet": 5}
}

product_prices = {
    "Laptop": 1000,
    "Phone": 500,
    "Tablet": 300
}

revenue_per_store(sales_data,product_prices)

