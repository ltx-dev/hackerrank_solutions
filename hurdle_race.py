def hurdleRace(k, height):
    max = 0
    for n in height:
        if n > max:
            max = n

    if k > max:
        return 0
    else:
        return abs(k - max)       
