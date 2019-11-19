#
# https://www.hackerrank.com/challenges/the-hurdle-race/problem  
#
def hurdleRace(k, height):
    return 0 if max(height) < k else max(height) - k