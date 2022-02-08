import csv
from tkinter import Tk, filedialog


def find_optimal(stock_data, budget):
    budget *= 100
    table = [[0 for w in range(budget + 1)] for j in range(len(stock_data) +
                                                           1)]

    for j in range(1, len(stock_data) + 1):
        item, price, val = stock_data[j - 1]
        for w in range(1, budget + 1):
            if price > w:
                table[j][w] = table[j - 1][w]
            else:
                table[j][w] = max(table[j - 1][w],
                                  table[j - 1][w - price] + val - price)

    result = []
    for j in range(len(stock_data), 0, -1):
        was_added = table[j][budget] != table[j - 1][budget]

        if was_added:
            item, price, val = stock_data[j - 1]
            result.append(stock_data[j - 1])
            budget -= price

    return result


root = Tk()
root.withdraw()
root.attributes('-topmost', True)
file_name = filedialog.askopenfilename()


with open(file_name, "r") as file:
    reader = csv.reader(file)
    next(reader)
    items = ((name, int(float(amount)*100), int((float(amount) + float(
        amount) * float(value) / 100) * 100))
                    for name, amount, value in reader
                    if float(amount) > 0)
    items = tuple(items)

budget_available = 500

bought = find_optimal(items, budget_available)
print("Bought :\n  " +
      '\n  '.join(item for item, _, _ in bought))
val = 0
total_price = 0
for item, price, gain in bought:
    total_price += price
    val += gain

total_price /= 100
val /= 100
print(f"Total cost : {total_price}€\n"
      f"Value after 2 years : {val}€\n"
      f"Profit : {'%.2f' % (val - total_price)}€")



