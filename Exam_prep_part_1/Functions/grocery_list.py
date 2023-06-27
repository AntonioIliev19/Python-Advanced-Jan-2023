def shop_from_grocery_list(budget, grocery_list, *products_prices):
    bought_products = []
    for product, price in products_prices:
        if product not in grocery_list:
            continue
        if price > budget:
            break
        else:
            bought_products.append(product)
            budget -= price
            grocery_list.remove(product)
    if not grocery_list:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(grocery_list)}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))

print(shop_from_grocery_list(
 100,
 ["tomato", "cola", "chips", "meat"],
 ("cola", 5.8),
 ("tomato", 10.0),
 ("meat", 22),
))

print(shop_from_grocery_list(
 100,
 ["tomato", "cola", "chips", "meat", "chocolate"],
 ("cola", 15.8),
 ("chocolate", 30),
 ("tomato", 15.85),
 ("chips", 50),
 ("meat", 22.99),
))
