print("**********************************************")
print("Welcome Silent Auction System \n")
print("********************************************** \n")
bid_register = {}
isAnyParticipantRemaining = "yes"

def isAnyMoreParticipant():
    participant = input("Is there any other participant to participate in bid - type 'yes' or 'no' : ").lower()
    return participant


def add_your_bid():
    name = input("Enter Your Name: ")
    bid = float(input("Enter Bid Value: $"))
    bid_register[name] = bid

def declare_winner():
    maxbid = 0
    maxBidder = ""
    for key in bid_register:
        if bid_register[key] > maxbid:
            maxbid = bid_register[key]
            maxBidder = key
    return maxbid,maxBidder

while isAnyParticipantRemaining == "yes":
    isAnyParticipantRemaining = isAnyMoreParticipant()
    if isAnyParticipantRemaining == "yes":
        add_your_bid()
    elif isAnyParticipantRemaining == "no":
        maxbid,maxBidder = declare_winner()
        if maxbid != 0:
            print(f"Winner of today's bid is {maxBidder} and bid value is ${maxbid}.")
        else:
            print("Thanks for participation. We have not received any bid as of now.")
        break
    else:
        print("Incorrect Value entered. Please Try Again.")
        isAnyMoreParticipant = "yes"

