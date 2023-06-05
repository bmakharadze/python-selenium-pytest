import datetime as dt


class BikeRental:
    def __init__(self, stock):
        self.stock = stock

    def display_stock(self):
        print(f"There is {self.stock} currently in the stock.")
        return self.stock

    def rent_bike_on_hourly_basis(self, n):
        if n < 0:
            print("Number of bikes must be positive.")
            return None
        elif n > self.stock:
            print(f"Sorry, We have only {self.stock} bikes available.")
            return None
        else:
            now = dt.datetime.now()
            print(f"You have rented {n} bike(s) on hourly basis. Today at {now.hour}:{now.minute}:{now.second}\n"
                  f"You will be charged 5$ for each bike per hour.")
            self.stock -= n
            return now

    def rent_bike_on_daily_basis(self, n):
        if n < 0:
            print("Number of bikes must be positive.")
            return None
        elif n > self.stock:
            print(f"Sorry, We have {self.stock} bikes available.")
            return None
        else:
            now = dt.date.today()
            print(f"You have rented {n} bike(s) on daily basis. Today on {now}\n"
                  f"You will be charged 20$ for each bike daily.")
            self.stock -= n
            return now

    def rent_bike_on_weekly_basis(self, n):
        if n < 0:
            print("Number of bikes must be positive.")
            return None
        elif n > self.stock:
            print(f"Sorry, We have {self.stock} bikes available.")
            return None
        else:
            now = dt.date.today()
            print(f"You have rented {n} bike(s) on daily basis. Today on {now}\n"
                  f"You will be charged 60$ for each bike weekly.")
            self.stock -= n
            return now

    def return_bike(self, request):
        rental_time, rental_basis, num_of_bikes = request
        bill = 0
        if rental_time and rental_basis and num_of_bikes:
            self.stock += num_of_bikes
            now = dt.datetime.now()
            rental_period = now - rental_time
            if rental_basis == 1:
                bill = round(rental_period.seconds / 3600) * 5 * num_of_bikes
            elif rental_basis == 2:
                bill = round(rental_period.days) * 20 * num_of_bikes
            elif rental_basis == 3:
                bill = round(rental_period.days / 7) * 60 * num_of_bikes
            if 3 <= num_of_bikes <= 6:
                print("You are eligible for family rental promotion which 30%.")
                bill = bill * 0.7
            print(f"Thanks for renting bike. \n The total bill is {bill}")
            return bill
        else:
            print("Are you sure you rented bike?")
            return None


class Customer:
    def __init__(self):
        self.bikes = 0
        self.rental_basis = 0
        self.rental_time = 0
        self.bill = 0

    def request_bike(self):
        bikes = input("How many bikes would you like to rent? ")
        try:
            bikes = int(bikes)
        except ValueError:
            print("Number should be positive.")
            return -1
        if bikes < 1:
            print("Number should be positive.")
            return -1
        else:
            self.bikes = bikes
        return self.bikes

    def return_bike(self):
        if self.rental_basis and self.rental_time and self.bikes:
            return self.rental_basis, self.rental_time, self.bikes
        else:
            return 0, 0, 0


