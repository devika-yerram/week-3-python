order_amount = 150

def apply_discount(order_amount):
    if order_amount > 100:
        final_price = order_amount - (order_amount / 10)
        print("Final price after applying the discount is $", final_price)
    else:
        print("Final price is $", order_amount)

apply_discount(order_amount)