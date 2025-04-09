from itertools import product

def solution(users, emoticons):
    
    discounts = list(product([90, 80, 70, 60], repeat = len(emoticons))) # 할인율
    
    p, b = 0, 0
    for discount in discounts: 
        prices = []
        for i in range(len(emoticons)):
            prices.append((int(discount[i] * emoticons[i] / 100), 100 - discount[i]))
        
        plus, buy = 0, 0
        for user in users:
            per, money = user
            current = 0
            for price in prices:
                if price[1] >= per:
                    current += price[0]
            if current >= money:
                plus += 1
            else:
                buy += current
        
        if plus > p:
            p = plus
            b = buy
        elif plus == p and buy > b:
            b = buy
   
    return [p, b]