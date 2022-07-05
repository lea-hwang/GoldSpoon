# import sys
# sys.stdin = open('../input.txt', 'r')

N = int(input())
coins = [500,100,50,10,5,1]
cost = 1000-N

res = 0
for coin in coins:
    res += cost // coin
    cost %= coin

print(res)