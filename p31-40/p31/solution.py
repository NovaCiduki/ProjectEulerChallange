coins_opt = {1: 1, 2: 2, 3: 5, 4: 10, 5: 20, 6: 50, 7: 100}
coins_tot = [0, 0, 0, 0, 0, 0, 0]  # 1,2,5,10,20,50,100
what_is_the_sum = 200


def tot_val(coins):
    re = 0
    for index in range(1, 8):
        re += coins[index - 1] * coins_opt[index]
    return re


def update_coins(coins):
    if tot_val(coins) < what_is_the_sum:
        coins[0] += 1
        return
    else:
        for index in range(len(coins)):
            if index == len(coins) - 1:
                coins[index] += 1
                return
            elif tot_val(coins) >= what_is_the_sum:
                coins[index] = 0
            elif tot_val(coins) < what_is_the_sum:
                coins[index] += 1
                return


tot = 0
while coins_tot[len(coins_tot) - 1] * coins_opt[len(coins_tot)] <= what_is_the_sum:
    # once the last cell will add more than the wanted sum we can stop
    if tot_val(coins_tot) == what_is_the_sum:
        tot += 1
    update_coins(coins_tot)
print(tot + 1)  # +1 because we should remember that 0*1p+0*2p+...+0*1£+1*2£ = 2£
