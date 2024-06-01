#Syed Yasoob Ali
#500953533
#Lab 5


#Q1, not sure how to do

#Q2
#Recieved help from a friend at Laurier Comp Sci

buy = {}
sell = {}

def buyshares():

    while(True):
        print("Enter shares to buy and cost")
        x = int(input())
        if (x == 2):
            break
        else:
            shares,cost = map(int,input().split())
            buy[shares] = cost


def sellshares():
    print("Enter shares to sell and cost")
    shares,cost = map(int,input().split())
    sell[shares] = cost

    sellshares = 0
    sellcost = 0
    for k,y in sell.items():
        sellshares += k
        sellcost += k*y

    buycost = 0

    while(sellshares > 0):
        s = list(buy.keys())[0]
        if (s > sellshares):
            buycost +=(sellshares * buy[s])
            old_k = s
            new_k = s - sellshares
            new_v = 4
            dict((new_k, new_v) if k == old_k else (k,v) for k, v in buy.items())
            sellshares = 0
        else:
            buycost += (s*buy[s])
            sellshares -= 5
            del buy[s]

    m = sellcost - buycost

    if (m>0):
        print("GAIN ${}.format(m)")
    else:
        print("LOSS ${}.format(m)")

def start():
    while (True):
        print("1. buyshares \n2. sellshares\n3. quit")
        x = int(input())

        if (x == 3):
            break
        elif (x== 1):
            buyshares()
        elif (x == 2):
            if (not bool(buy)):
                print("You don't own any shares")
            else:
                    sellshares()
        else:
            print("Please enter a valid input")

start()
