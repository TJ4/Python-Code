from random import shuffle #Because making a random number generator from scratch is hard
suits = ["D","C","H","S"]
numbers = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
cards = [i+j for i in suits for j in numbers]

def refresh():
    global hand
    newdeck()
    hand = newhand()
    print(hand)

def newdeck():
    global deck, cards
    deck = list(cards)
    shuffle(deck)

def newhand():
    global deck
    hand = []
    for i in range(1, 6):
        hand.append(deck.pop())
    return hand

def orderer(n):
    for i in range(0, 5):
        if n[0][i] == "0":
            n[0][i] = "10"
        if n[0][i] == "J":
            n[0][i] = "11"
        if n[0][i] == "Q":
            n[0][i] = "12"
        if n[0][i] == "K":
            n[0][i] = "13"
        if n[0][i] == "A":
            n[0][i] = "14"
    return n

def cardrank(n):
    if straightcheck(n) == 1 and flushcheck(n) == 1 and n[0][0] == "10":
        return 9 
    elif straightcheck(n) == 1 and flushcheck(n) == 1:
        return 8
    elif quadcheck(n) == 1:
        return 7
    elif triplecheck(n) == 1 and paircheck(n) == 1:
        return 6
    elif flushcheck(n) == 1:
        return 5
    elif straightcheck(n) == 1:
        return 4
    elif triplecheck(n) == 1:
        return 3
    elif paircheck(n) == 2:
        return 2
    elif paircheck(n) == 1:
        return 1
    else:
        return 0

def cardrankname(n):
    names = ["Garbage","1 Pair","2 Pairs","Three of a Kind","Straight","Flush","House","4 of a Kind","Straight Flush","Royal Flush"]
    return names[n]

def flushcheck(n):
    if n[1].count(n[1][0]) == 5:
        return 1
    else:
        return 0

def straightcheck(n):
    straight = 1
    l = list(n[0])
    for i in range(0, len(l)):
        l[i] = int(l[i])
    l.sort()
    for i in range(0, len(l)-1):
        if l[i]+1 == l[i+1]:
            ...
        else:
            straight = 0
    if straight == 0:
        for i in range(0, len(l)-2):
            if l[4]-12 == l[0] and l[i]+1 == l[i+1]:
                ...
            else:
                return 0
    return 1

def quadcheck(n):
    if n[0].count(n[0][0]) ==  4:
        return 1

def triplecheck(n):
    for i in n[0]:
        if n[0].count(i) == 3:
            return 1

def paircheck(n):
    counter = 0
    for i in n[0]:
        if n[0].count(i) == 2:
            counter += 0.5
    if counter == 1:
        return 1
    elif counter == 2:
        return 2

def cardorganizer(hand):
    org_hand = []
    part1 = []
    part2 = []
    for i in hand:
        if "10" in i:
            i = i[0] + "0"
        for j in i:
            org_hand.append(j)
    for f in range(0, 10):
        if f%2 == 1:
            part1.append(org_hand[f])
        else:
            part2.append(org_hand[f])
    org_hand = [part1, part2]
    return org_hand

def play_game_2(n):
    counter = [0 for i in range(0, 10)]
    for i in range(0, n):
        newdeck()
        hand = newhand()
        a = cardorganizer(hand)
        a = orderer(a)
        b = cardrank(a)
        c = cardrankname(b)
        counter[b] += 1
    print("There were:")
    print(counter[0],"garbage hand(s).")
    print(counter[1],"hand(s) of 1 Pair.")
    print(counter[2],"hand(s) of 2 Pairs.")
    print(counter[3],"Three of a kind(s).")
    print(counter[4],"Straight(s)")
    print(counter[5],"Flushes(s)")
    print(counter[6],"House(s)")
    print(counter[7],"4 of a Kind(s)")
    print(counter[8],"Straight Flush(es)")
    print(counter[9],"Royal Flush(es)")
        
        

def play_game_1():
    newdeck()
    hand = newhand()
    a = cardorganizer(hand)
    a = orderer(a)
    b = cardrank(a)
    c = cardrankname(b)
    print(hand," - "+c)
