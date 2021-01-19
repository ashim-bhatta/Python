auctions_data = {}

auction_added = True

while auction_added:
    name = input("Enter Your Name: ")
    bid_amount = int(input("Enter Your Bid Amount: "))
    auctions_data[name] = bid_amount

    running = input("Are there any others Bidders? Type 'yes' or 'no'.")
    if running.lower() == 'no':
        auction_added = False

higest_bid_amount = 0
higest_bid_by = ''
for key in auctions_data:
    if auctions_data[key] > higest_bid_amount:
        higest_bid_amount = auctions_data[key]
        higest_bid_by = key

print(f'Higest Bid amount is {higest_bid_amount} by {higest_bid_by}.')