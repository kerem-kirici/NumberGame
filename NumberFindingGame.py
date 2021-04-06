from collections import defaultdict
import random

def setup(i=1, s=""):
    global N, l
    if i == N+1:
        l.append(s)
        return
    for j in range(int(i==1), 10):
        if str(j) not in s:
            setup(i+1, s+str(j))
    return

def make_guess():
    global N, l
    d = defaultdict(int)
    for i in l:
        for j in range(N):
            d[i[j]] += 1
    m = -1
    ll = []
    for i in l:
        nm = sum([d[k] for k in i])
        if m < nm:
            ll = [i]
            m = nm
        elif m == nm:
            ll.append(i)

    return "%s    (selected from a list of %d \"better\" numbers from a list(%d) of all possible numbers)" % (random.choice(ll), len(ll), len(l))

def crop_l(positive, negative):
    global guess, N, l
    nl = []
    for j in l:
        if calc_positive(j, guess) == positive and calc_negative(j, guess) == negative:
            nl.append(j)
    l = nl

if __name__ == '__main__':
    N = 4
    l = []
    guess = None
    guess_number = 1

    calc_positive = lambda x, y: sum([int(x[i] == y[i]) for i in range(N)])
    calc_negative = lambda x, y: sum([int(y[i] in x and x[i] != y[i]) for i in range(N)])

    setup()

    my_number = random.choice(l)
    while True:
        guess = make_guess()
        print(" %d: " % guess_number + guess)
        positive = int(input(" +"))
        negative = int(input(" -"))
        
        crop_l(positive, negative)
        their_guess = input(" %d: Your guess: " % guess_number)
        their_positive = calc_positive(my_number, their_guess)
        their_negative = calc_negative(my_number, their_guess)
        print(" +" + str(their_positive))
        print(" -" + str(their_negative))

        if their_positive == N and positive == N:
            print(" Tie")
            break
        elif their_positive == N:
            print(" Congrats!")
            break
        elif positive == N:
            print(" Loseeer!", "my number was %s" % my_number)
            break

        guess_number += 1
    input(" Press enter to quit.")
