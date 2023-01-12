import replit



import art
print(art.logo)

bids = {}
bidding_finished = False

def highest_bidder(bidingl):
    highest_bid = 0
    winner = ""
    for bidder in bidingl:
        bid_amount = bidingl[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with ${highest_bid}")

while not bidding_finished:
    name = input("What is your name?\n")
    price = input("What is your bid? $\n")
    if price.isdigit():
       price = int.price
    else:
        price = int(input("Please use numbers only!\n What is your bid? $\n"))

    bids[name] = price
    keep_going = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
    if keep_going == 'no':
        bidding_finished = True
        highest_bidder(bids)
    elif keep_going == 'yes':
        replit.clear()
