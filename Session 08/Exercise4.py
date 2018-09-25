# Function to get price based off name
def price_value(input_string):    
    total = 0
    # Loop through each character and get the corresponding value, then add to running total
    for c in input_string:
        total += (ord(c)-96)
    # Format output as dollar amount
    return total

def price_string(total):
    return '${:,.2f}'.format(total)

# Define list of groceries
groceries = ['bananas', 'rice', 'paprika', 'potato chips']

# Define total receipt
total_receipt = 0 

# Define padding for output alignment
padding_base = len(max(groceries, key = len)) + 10

# Print each of the groveries in dollar format on their own line
for item in groceries:
    # Define padding for text alignment
    padding = padding_base - len(item)
    # Print the item, align the price with appropriate padding
    print(item + ' ' +  ('{:>' + str(padding) + '}').format(price_string(price_value(item))))
    # Add item to total
    total_receipt += price_value(item)

print('-' * (padding_base + 2))

padding = padding_base - len('tota')
print('Total'+  ('{:>' + str(padding) + '}').format(price_string(total_receipt)))