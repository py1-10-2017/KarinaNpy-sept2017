import random
def coin_toss(tosses):
    attempts = 1
    heads = 0
    tails = 0
    result = ''

    for i in range(1, tosses):
        new = random.randint(0,1)
        if new == 1:
            heads +=1
            result = 'head'
            print "Attempt #", attempts, ": Throwing a coin... It's a ", result, "!Got ", heads, " heads so far and ", tails, " tails so far"
        else:
            tails +=1
            result = 'tail'
            print "Attempt #", attempts, ": Throwing a coin... It's a ", result, "!Got ", heads, " heads so far and ", tails, " tails so far"
        attempts += 1
coin_toss(5001)
