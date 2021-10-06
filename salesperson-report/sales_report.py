"""Generate sales report showing total melons each salesperson sold."""

# Lists to track salespeopl and melons_sold
salespeople = []
melons_sold = []

f = open('sales-report.txt')
for line in f:
    line = line.rstrip()
    entries = line.split('|')
    # Get the sale person and melon sold
    salesperson = entries[0]
    melons = int(entries[2])
    # if person in the list, get the index to record the melon sold in the other list 
    if salesperson in salespeople:
        position = salespeople.index(salesperson)

        melons_sold[position] += melons
    # If this is a new sale person, add person and melon sold to the appropriate list
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)

# create index from range and loop through the two lists pwd

for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
