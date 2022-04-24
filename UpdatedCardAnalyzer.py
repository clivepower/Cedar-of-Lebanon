def hand(l0, l1):
    if max(l1) - min(l1) == 4:
        result = 'Straight'
    else:
        l3 = l0 + []
        s = [i for i in l0 if l0.count(i) == 1]
        for i in range(len(s)):
            while s[i] in l3:
                l3.remove(s[i])
        if len(s) == 0:
            result = 'Full house'
        elif len(s) == 5:
            result = f'Highest card is {l0[l1.index(max(l1))]}'
        elif len(s) == 3:
            result = f'2 {l3[0]}s'
        elif len(s) == 2:
            result = f'3 {l3[0]}s'
        else:
            if len(set(l3)) == 1:
                result = f'4 {l3[0]}s'
            else:
                result = f'Two pairs'
    return result

def numeric(l0):
    l1 = l0 + []
    for i in range(len(l0)):
        if l1[i] == 'Jack':
            l1[i] = 11
        if l1[i] == 'Queen':
            l1[i] = 12
        if l1[i] == 'King':
            l1[i] = 13
        if l1[i] == 'Ace':
            l1[i] = 14
    return l1

def l_to_l0(l):
    l0 = l + []
    for i in range(len(l)):
        if l[i] == 0:
            l0[i] = 2
        elif l[i] == 1:
            l0[i] = 'Ace'
        elif l[i] == 2:
            l0[i] = 'Queen'
    return l0

