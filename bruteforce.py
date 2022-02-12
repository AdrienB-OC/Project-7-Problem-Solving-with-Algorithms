import csv
import itertools


def get_keys_from_value(d, val):
    return [a for a, v in d.items() if v == val]


def find_optimal_bruteforce(stock_price, value_after):
    prices = value_after.keys()
    prices_list = list(prices)

    target = 500
    optimal_buy = []
    initial_investment = 0
    optimal_return = 0

    for i in range(1, len(prices_list)):
        for s in itertools.combinations(prices_list, i):
            if sum(s) <= target:
                keys_list = []
                for j in s:
                    keys_list.append(value_after[j])

                optimal_temp = 0
                for key in keys_list:
                    optimal_temp += key

                if optimal_temp - sum(s) > optimal_return - initial_investment:
                    optimal_return = optimal_temp
                    optimal_buy = s
                    initial_investment = sum(s)

    stocks = []
    for val in optimal_buy:
        stocks += (get_keys_from_value(stock_price, val))

    print("Bought :")
    for stock in stocks:
        print(stock)

    print(f"Total Cost : {initial_investment}€\n"
          f"Value after 2 years : {optimal_return}€\n"
          f"Gain : {'%.2f' % (optimal_return - initial_investment)}€")


with open("data.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    investment = {rows[0]: int(rows[1]) for rows in reader}
    file.seek(0)
    next(reader)
    return_on_inv = {int(rows[1]): int(rows[1])+int(rows[1])*int(rows[2])/100
                     for rows in reader}

find_optimal_bruteforce(investment, return_on_inv)



