
def check_payment(input_file):
    # Parse the customer orders file
    data_file = open(input_file)
    for line in data_file:
        line = line.rstrip()
        data = line.split('|')
        record, full_name, melons_qty, amt_paid = data
    
        amt_due = int(melons_qty) * melon_cost
        print(f"{full_name} paid ${amt_paid}. The cost of the melons is {amt_due}")
        if float(amt_paid) < amt_due:
            print(f"{full_name} has under paid for their melons")
        elif float(amt_paid) > amt_due:
            print(f"{full_name} has over paid for their melons")

# Call the function:
melon_cost = 1.0
check_payment("customer-orders.txt")