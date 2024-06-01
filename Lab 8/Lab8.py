#Syed Yasoob Ali
#500953533
#Lab 8

#Some help recieved from friend at Laurier Computer Science Program


keys = [12,44,13,88,23,94,11,39,20,16,5]


def hash1(i):
    return (3*i+5)%11

def h2(i):
    return 7-i%7


#Seperate Chaining

sep_chain_hash = [[] for i in range(11)]

def insert_sep(k):
    sep_chain_hash[hash1(k)].append(k)

for k in keys:
    insert_sep(k)
    


#Linear Probing

lp_hash = [None]*11

def insert_lp(k):
    i = 0

    while lp_hash[(hash1(k)+i)%11] != None:
        i+= 1
        if i >= 11:
            print("Full hash table")
            return

    lp_hash[(hash1(k)+i)%11] = k

for k in keys:
    insert_lp(k)


#Double Hashing

d_hash = [None]*11

def insert_d(k):
    i = 0
    while d_hash[(hash1(k)+i*h2(k))%11] != None:
        i+= 1
        if i>= 11:
            print("Full hash table")
            return
    d_hash[(hash1(k)+i*h2(k))%11] = k

for k in keys:
    insert_d(k)


#Print statements

print("Seperate Chaining hash table")
print("Index\tList")

for i in range(11):
    print(i, "\t", sep_chain_hash[i])
print()

print("Linear Probing")
print("Index\tValue")

for i in range(11):
    print(i,"\t", lp_hash[i])
print()


print("Double Hashing:")
print("Index\tValue")
for i in range(11):
    print(i,"\t", d_hash[i])
print()


        
