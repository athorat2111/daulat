import random


def print_grid(l):
    for i in range(9):
        print(l[i], end=' ')
        if((i+1) % 3 == 0):
            print()


def mark_pos(l, dummy):
    u = int(input("On which position do you want to mark "+str(user)+"?"))
    while u not in dummy:
        print("That position is already marked or not in range 1-9.")
        u = int(input("Enter some other position:"))
    l[u-1] = user
    for j in range(len(dummy)):
        if(dummy[j] == u):
            del(dummy[j])
            break


def mark_pos_comp(l, dummy, comp):
    l[comp-1] = com
    for j in range(len(dummy)):
        if(dummy[j] == comp):
            del(dummy[j])
            break


l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
user = 'x'
com = 0
result = 0
cnt = 1
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mark_pos(l, l1)
print_grid(l)
for i in range(4):
    comp = random.choice(l1)
    mark_pos_comp(l, l1, comp)
    print("Computer has marked at position "+str(comp))
    print_grid(l)
    if(l[0] == l[1] == l[2] or l[0] == l[3] == l[6] or l[0] == l[4] == l[8] or l[3] == l[4] == l[5] or l[6] == l[7] == l[8] or l[1] == l[4] == l[7] or l[2] == l[5] == l[8] or l[2] == l[4] == l[6]):
        result = 1
        print("You lost")
        break
    mark_pos(l, l1)
    print_grid(l)
    if(l[0] == l[1] == l[2] or l[0] == l[3] == l[6] or l[0] == l[4] == l[8] or l[3] == l[4] == l[5] or l[6] == l[7] == l[8] or l[1] == l[4] == l[7] or l[2] == l[5] == l[8] or l[2] == l[4] == l[6]):
        result = 1
        print("You won")
        break
if(result == 0):
    print("Match is draw")
