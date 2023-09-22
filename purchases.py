number_of_purchases = int(input("Number of purchases: "))
sales_tax = float(input("Sales tax: "))
customers = []
purchase_cost = []

# This section of code will loop the amount of times you put as a value 
for i in range(number_of_purchases):
    customer = input("Customer: ")
    cost = int(input("Cost: "))
    customers.append(customer)
    purchase_cost.append(cost)

def add_tax(list, tax):
    new_list = []
    for cost in list:
        new_cost = cost + (cost * tax)
        new_list.append(new_cost)
    return new_list

purchase_list = add_tax(purchase_cost, sales_tax)

transaction = {}

for i in range(number_of_purchases):
    if customers[i] in transaction:
        transaction[customers[i]] += purchase_list[i]
    else:
        transaction[customers[i]] = purchase_list[i]

print(transaction)