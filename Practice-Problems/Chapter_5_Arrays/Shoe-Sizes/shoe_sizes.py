from collections import Counter
# The first line contains X, the number of shoes
x = int(input())
#The second line contains the space separated list of all the shoe sizes in the shop.
shoe_sizes = [int(char) for char in input().split(" ")]

shoe_sizes = Counter(shoe_sizes)

# need a dict that has keys of shoe sizes and values of shoe count
# shoe_size_dict = dict([(shoe_size, shoe_sizes.count(shoe_size)) for shoe_size in set(shoe_sizes)])
# shoe_size_ct = Counter(shoe_sizes)
# print(sorted(shoe_size_dict.items()))
# print(sorted(shoe_size_ct.items()))

shoe_sizes_set = set(shoe_sizes)

# The third line contains n, the number of customers.
customers = int(input())

# The next n lines contain the space separated values of the shoe sizes desired by the customer and xi, the price of the shoe.
purchases = []
for i in range(customers):
    # every loop returns another line of str(input) 
    line = input()
    
    # we are splitting strings shoe_size and price by (space)
    shoe_size, price = line.split(" ")
    
    # changing strings to ints
    shoe_size, price = int(shoe_size), int(price)
    
    # purchases is (shoe_size, price) 
    purchases.append([shoe_size, price])


prices_paid = 0
orders = []
for shoe_size, price in purchases:
    if shoe_sizes[shoe_size]:
        prices_paid += price
        shoe_sizes[shoe_size] -= 1

print(prices_paid)

#Standard ouput
# 4645