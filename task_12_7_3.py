def deposit_income_per_year(money):
    per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
    deposits = []
    for percent in per_cent.values():
        deposits.append(int((money * percent) / 100))
    print("deposits =    ", deposits)
    print("max deposit = ", max(deposits))

deposit_income_per_year(100000)
