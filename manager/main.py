import numpy as np
import random
import time

def case(original,now):
    if (now-original) / original == 0:
        return ['IT IS A COMMON DAY! UNCHANGED', (now-original) / original]
    if (now-original) / original > 0 and (now-original) / original <= 0.05:
        return ['JUST SO SO! LITTLE INCREASE', (now-original) / original]
    if (now-original) / original > 0.05 and (now-original) / original <= 0.2:
        return ['THAT IS NICE! MEDIUM INCREASE', (now-original) / original]
    if (now-original) / original > 0.2 and (now-original) / original <= 0.4:
        return ['AWESOME! BIG INCREASE', (now-original) / original]
    if (now-original) / original > 0.4:
        return ['YOU GOT LUCK! LARGE INCREASE', (now-original) / original]
    if (now-original) / original >= -0.05 and (now-original) / original < 0:
        return ['NOT GOOD! LITTLE DECREASE', (now-original) / original]
    if (now-original) / original >= -0.2 and (now-original) / original < -0.05:
        return ['OH NO! MEDIUM DECREASE', (now-original) / original]
    if (now-original) / original >= -0.4 and (now-original) / original < -0.2:
        return ['IT IS SO SORRY! BIG DECREASE', (now-original) / original]
    if (now-original) / original <= -0.4:
        return ['DAMN IT! LARGE DECREASE', (now-original) / original]

original_money = 100
original_price1 = 1
original_price2 = 5
original_price3 = 10
original_price4 = 20
n1 = 0
n2 = 0
n3 = 0
n4 = 0
step = 0
storage = '1'
sum_number = 0
price1 = original_price1
price2 = original_price2
price3 = original_price3
price4 = original_price4
pocket_money = original_money
sum_money_old = original_money
storage_level = {'1': [10, 2], '2': [25, 5], '3': [50, 10], '4': [100, 20], 'INF': ['INF', 100], 'inf':['inf', 100]}
lamda = 2
condition = 10

while step<11:

    while True:

        if step == 0:
            print '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ \n' \
                  'WELCOME TO THE GAME - BATTLE OF GAO YI WEN \n' \
                  'AT THIS GAME, YOU MUST BUY THE GOODS WITHIN THE LIMIT OF STORAGE LEVEL \n' \
                  'YOU CAN INCREASE OR DECREASE THE STORAGE LEVEL EVERY TURN \n' \
                  'LEVEL    NUMBER OF MAXIMUM GOODS           COST PER DAY  \n' \
                  '1                 10                             2       \n' \
                  '2                 25                             5      \n' \
                  '3                 50                             10      \n' \
                  '4                 100                            20      \n' \
                  'INF               INF                            100     \n' \
                  'CONDITION OF WIN: \n' \
                  'AFTER %d TURNS, MONEY IN YOUR POCKET + THE VALUE OF STORAGE >= %.1f \n' \
                  '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n' \
                  'PRICE AND NUMBER AT TURN %d: \n ' \
                  '\n' \
                  ' GaoYiWen $%.1f \n' \
                  '  The number you have %d \n' \
                  '\n' \
                  ' XiaoSao $%.1f \n' \
                  '  The number you have %d \n ' \
                  '\n' \
                  ' YiWenSheShou $%.1f \n' \
                  '  The number you have %d \n' \
                  '\n' \
                  ' GaoZong $%.1f \n' \
                  '  The number you have %d \n' \
                  % (condition, original_money * lamda, step,
                     original_price1, n1,
                     original_price2, n2,
                     original_price3, n3,
                     original_price4, n4)

            print '************************************************ \n' \
                  'THE LEVEL OF YOUR STORAGE: LV.%s' % (storage)

            sum_number = n1 + n2 + n3 + n4
            print '************************************************ \n' \
                  'THE GOODS ON STORAGE: %d, AND REMAIN STORAGE: %d' % (
                  sum_number, storage_level[storage][0] - sum_number)

            print '************************************************ \n' \
                  'MONEY ON YOUR POCKET: $%.1f' % (pocket_money)

            market_money = price1 * n1 + price2 * n2 + price3 * n3 + price4 * n4
            print '************************************************ \n' \
                  'MONEY ON MARKET: $%.1f' % (market_money)

            print '************************************************ \n' \
                  'MONEY ON POCKET AND MARKET: $%.1f' % (market_money + pocket_money)

        else:
            print '\n' \
                  '\n' \
                  '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n' \
                  'PRICE AND NUMBER AT TURN %d: \n ' \
                  '\n' \
                  ' GaoYiWen $%.1f \n' \
                  '  %s ~ Amount of Increase %.2f %%\n' \
                  '   The number you have %d \n' \
                  '\n' \
                  % (step,
                     price1, compare1[0], 100 * round(compare1[1], 4), n1)
            time.sleep(1)

            print ' XiaoSao $%.1f \n' \
                  '  %s ~ Amount of Increase %.2f %%\n' \
                  '   The number you have %d \n' \
                  '\n' \
                  % (price2, compare2[0], 100 * round(compare2[1], 4), n2,)
            time.sleep(1)

            print ' YiWenSheShou $%.1f\n' \
                  '  %s ~ Amount of Increase %.2f %%\n' \
                  '   The number you have %d \n' \
                  '\n' \
                  % (price3, compare3[0], 100 * round(compare3[1], 4), n3,)
            time.sleep(1)

            print ' GaoZong $%.1f \n' \
                  '  %s ~ Amount of Increase %.2f %% \n' \
                  '   The number you have %d \n' \
                  '\n' \
                  % (price4, compare4[0], 100 * round(compare4[1], 4), n4)

            print '************************************************ \n' \
                  'THE LEVEL OF YOUR STORAGE: LV.%s' % (storage)

            print '************************************************ \n' \
                  'THE GOODS ON STORAGE: %d, AND REMAIN STORAGE: %d' % (
                  sum_number, storage_level[storage][0] - sum_number)

            pocket_money = pocket_money
            print '************************************************ \n' \
                  'MONEY ON YOUR POCKET: $%.1f' % (pocket_money)

            market_money = price1 * n1 + price2 * n2 + price3 * n3 + price4 * n4
            print '************************************************ \n' \
                  'MONEY ON MARKET: $%.1f' % (market_money)

            print '************************************************ \n' \
                  'MONEY ON POCKET AND MARKET: $%.1f  AMOUNT OF INCREASE: %.2f%%' \
                  % (market_money + pocket_money,
                     100 * round(((market_money + pocket_money) / sum_money_old - 1), 4))

        do_or_not = raw_input('\nDO YOU WANT TO SKIP THIS TURN ? Y/N ')
        if do_or_not == 'Y' or do_or_not == 'y':
            if pocket_money < storage_level[storage][1] and pocket_money >= 0:
                print '************************************************ \n' \
                      'CAN NOT PAY THE STORAGE FEE THIS TURN! PLEASE CHOOSE BUY AND SELL AGAIN \n'
                time.sleep(1)
                continue
            else:
                market_money_old = market_money
                pocket_money_old = pocket_money
                sum_money_old = market_money_old + pocket_money_old
                pocket_money = pocket_money - storage_level[storage][1]
                storage_new = storage
                break

        else:
            resp = raw_input('\nDO YOU WANT TO EXPAND YOUR STORAGE ? Y/N ')
            if resp == 'Y' or resp == 'y':
                level = raw_input('INPUT THE LEVEL NUMBER YOU WANT TO REACH ')
                print 'IT CAN STORE %d GOODS AND THAT WILL COST $%.1f PER DAY' % \
                      (storage_level[level][0], storage_level[level][1])
                respp = raw_input('ARE YOU SURE ? Y/N ')
                if respp == 'Y' or resp == 'y':
                    storage_new = level

            print '\n' \
                  '************************************************ \n' \
                  'CHOOSE HOW TO BUY AND SELL \n' \
                  'CHOOSE ONLY ONE FROM BUY OR SELL (CAN NOT BUY AND SELL AT THE SAME TIME)'
            buy1 = raw_input('The number of GaoYiWen you want to BUY: ')
            sell1 = raw_input('The number of GaoYiWen you want to SELL: ')
            print ''
            buy2 = raw_input('The number of XiaoSao you want to BUY: ')
            sell2 = raw_input('The number of XiaoSao you want to SELL: ')
            print ''
            buy3 = raw_input('The number of YiWenSheShou you want to BUY: ')
            sell3 = raw_input('The number of YiWenSheShou you want to SELL: ')
            print ''
            buy4 = raw_input('The number of GaoZong you want to BUY: ')
            sell4 = raw_input('The number of GaoZong you want to SELL: ')
            print ''

            if int(sell1) > n1 or int(sell2) > n2 or int(sell3) > n3 or int(sell4) > n4:
                print '************************************************ \n' \
                      'NOT ENOUGH GOODS TO SELL! PLEASE CHOOSE BUY AND SELL AGAIN'
                time.sleep(1)
                continue


            if storage_new == 'INF' or storage_new =='inf':
                print '************************************************ \n' \
                      'YOU ARE THE VIP! CAN STORE INFINITE GOODS'
            else:
                sum_number_new = n1 + int(buy1) - int(sell1) + n2 + int(buy2) - int(sell2) + \
                             n3 + int(buy3) - int(sell3) + n4 + int(buy4) - int(sell4)
                print '************************************************ \n' \
                      'EMPTY PLACE ON YOUR STORAGE AFTER BUY AND SELL: %d' \
                      % (storage_level[storage_new][0] - sum_number_new)
                if sum_number_new > (storage_level[storage_new][0]):
                    print '************************************************ \n' \
                          'NOT ENOUGH PLACE TO STORE! PLEASE CHOOSE BUY AND SELL AGAIN \n'
                    time.sleep(1)
                    continue

            pocket_money_new = pocket_money - price1 * int(buy1) + price1 * int(sell1) + \
                                      - price2 * int(buy2) + price2 * int(sell2) + \
                                      - price3 * int(buy3) + price3 * int(sell3) + \
                                      - price4 * int(buy4) + price4 * int(sell4)
            print '************************************************ \n' \
                  'MONEY ON YOUR POCKET AFTER BUY AND SELL: $%.1f' % (pocket_money_new)
            if pocket_money_new >= storage_level[storage_new][1]:
                resp = raw_input('************************************************ \n'
                                 'ARE YOU SURE ? Y/N ')
                if resp == 'Y' or resp == 'y':
                    market_money_old = market_money
                    pocket_money_old = pocket_money
                    sum_money_old = market_money_old + pocket_money_old
                    pocket_money = pocket_money_new - storage_level[storage][1]
                    sum_number = sum_number_new
                    n1 = n1 + int(buy1) - int(sell1)
                    n2 = n2 + int(buy2) - int(sell2)
                    n3 = n3 + int(buy3) - int(sell3)
                    n4 = n4 + int(buy4) - int(sell4)
                    storage = storage_new
                    break
                else:
                    print '************************************************ \n' \
                          'CHOOSE AGAIN \n'
                    time.sleep(1)
                    continue
            elif pocket_money_new < storage_level[storage_new][1] and pocket_money_new >= 0:
                print '************************************************ \n' \
                      'CAN NOT PAY THE STORAGE FEE THIS TURN! PLEASE CHOOSE BUY AND SELL AGAIN \n'
                time.sleep(1)
                continue
            else:
                print '************************************************ \n' \
                      'NO MONEY! PLEASE CHOOSE BUY AND SELL AGAIN \n'
                time.sleep(1)
                continue

    print '\n' \
          '************************************************ \n' \
          'WAITING .........'
    time.sleep(3)

    seed1 = random.randint(0, 99)
    np.random.seed(seed1)
    price1_old = price1
    while True:
        price1 = round(np.random.normal(original_price1, 0.5),1)
        if price1 > 0 and price1 < 2 * original_price1:
            break

    seed2 = random.randint(0, 99)
    np.random.seed(seed2)
    price2_old = price2
    while True:
        price2 = round(np.random.normal(original_price2, 1), 1)
        if price2 > 0 and price2 < 2 * original_price2:
            break

    seed3 = random.randint(0, 99)
    np.random.seed(seed3)
    price3_old = price3
    while True:
        price3 = round(np.random.normal(original_price3, 2), 1)
        if price3 > 0 and price3 < 2 * original_price3:
            break

    seed4 = random.randint(0, 99)
    np.random.seed(seed4)
    price4_old = price4
    while True:
        price4 = round(np.random.normal(original_price4, 5), 1)
        if price4 > 0 and price4 < 2 * original_price4:
            break

    compare1 = case(price1_old, price1)
    compare2 = case(price2_old, price2)
    compare3 = case(price3_old, price3)
    compare4 = case(price4_old, price4)

    step = step + 1



if (market_money + pocket_money) >= (original_money * 2):
    print '\n' \
          '\n' \
          '\n' \
          '************************************************ \n' \
          '********************* WIN ********************** \n' \
          '************************************************'
else:
    print '\n' \
          '\n' \
          '\n' \
          '************************************************ \n' \
          '********************* LOSE ********************* \n' \
          '************************************************'



