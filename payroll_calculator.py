number_of_hours = 40
hourly_rate = 15
def calculate_pay(hours, rate):
    pay = hours * rate
    return pay
total_pay = calculate_pay(number_of_hours, hourly_rate)
print("The total pay for the employee is Rs.", total_pay)