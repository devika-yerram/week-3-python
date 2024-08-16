sales = [200, 600, 150, 800, 300]

def generate_report(sales):
    for x in sales:
        if x > 500:
            print(f"Sale amount: {x} (Over $500)")
        else:
            print(f"Sale amount: {x}")

generate_report(sales)

total_sales = sum(sales)
print("Total sales for the month:", total_sales)