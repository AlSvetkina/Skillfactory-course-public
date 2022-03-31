def tickets_price():
    number_of_tickets = int(input("enter ticket numbers: "))
    total = 0

    #print('number_of_tickets:', number_of_tickets)
    for ticket in range(1, number_of_tickets + 1):
        price_per_ticket = 0
        #print("  ticket", ticket)

        age = int(input("    enter age: "))
        if age >= 18 and age < 25:
            price_per_ticket = 990
        elif age >= 25:
            price_per_ticket = 1390

        #print("    price:", price_per_ticket)
        total += price_per_ticket

    if number_of_tickets > 3:
        #print('number_of_tickets more then 3, apply 10% discount')
        total *= 0.9

    print('total:', total)


tickets_price()
