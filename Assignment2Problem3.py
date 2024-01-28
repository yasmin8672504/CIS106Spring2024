# Problem #3
net_price_per_copy = float(input("Enter the net price of each copy of the novel: "))
estimated_copies_sold = int(input("Enter the estimated number of copies to be sold: "))

FIXED_ROYALTY_OPTION1_DELIVERY = 5000
FIXED_ROYALTY_OPTION1_PUBLISHED = 20000
ROYALTY_RATE_OPTION2 = 0.125
ROYALTY_RATE_OPTION3_FIRST_4000 = 0.10
ROYALTY_RATE_OPTION3_OVER_4000 = 0.14

royalties_option1 = FIXED_ROYALTY_OPTION1_DELIVERY + FIXED_ROYALTY_OPTION1_PUBLISHED
royalties_option2 = ROYALTY_RATE_OPTION2 * net_price_per_copy * estimated_copies_sold
if estimated_copies_sold <= 4000:
    royalties_option3 = ROYALTY_RATE_OPTION3_FIRST_4000 * net_price_per_copy * estimated_copies_sold
else:
    royalties_option3 = (ROYALTY_RATE_OPTION3_FIRST_4000 * net_price_per_copy * 4000) + \
                        (ROYALTY_RATE_OPTION3_OVER_4000 * net_price_per_copy * (estimated_copies_sold - 4000))

best_option = max(royalties_option1, royalties_option2, royalties_option3)

print("\nRoyalties:")
print("Option 1: $", royalties_option1)
print("Option 2: $", royalties_option2)
print("Option 3: $", royalties_option3)

print("\nBest option is:")
if best_option == royalties_option1:
    print("Option 1")
elif best_option == royalties_option2:
    print("Option 2")
else:
    print("Option 3")
