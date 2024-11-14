def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}.")

while True:
    bid = {}
    name = input("What is your name?: ")
    price = int(input("What is the bid?: $"))
    bid[name] = price
    should_continue = input("Are they any other bidders? Type 'yes' or 'no'. \n").lower()
    if should_continue == "no":
        find_highest_bidder(bid)
        break
    elif should_continue == "yes":
        print("\n" * 20 )




