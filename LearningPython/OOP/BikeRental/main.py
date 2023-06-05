import sys

import bike_rental as br

system = br.BikeRental(100)
customer = br.Customer()
while True:
    print("""
    ======== Bike Rental App ========
    1. Display available bikes.
    2. Request a bike on hourly basis - 5$
    3. Request a bike on daily basis - 20$
    4. Request a bike on weekly basis - 60$
    5. Return a bike(s).
    6. Exit.""")

    choice = input("Enter choice: ")

    try:
        choice = input(choice)
    except ValueError:
        print("Choice has to be from available choices.")
        continue

    if choice == 1:
        system.display_stock()
    elif choice == 2:
        customer.rental_time = system.rent_bike_on_hourly_basis(customer.request_bike())
        customer.rental_basis = 2
    elif choice == 3:
        customer.rental_time = system.rent_bike_on_daily_basis(customer.request_bike())
        customer.rental_basis = 3
    elif choice == 4:
        customer.rental_time = system.rent_bike_on_weekly_basis(customer.request_bike())
        customer.rental_basis = 4
    elif choice == 5:
        request_tuple = customer.return_bike()
        bill = system.return_bike(request_tuple)
        customer.bill = bill
        customer.rental_basis, customer.rental_time, customer.bikes = 0, 0, 0
    elif choice == 6:
        break
    else:
        print("Choice has to be from available choices.")