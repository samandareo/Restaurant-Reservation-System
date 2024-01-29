class Reservation:
    def __init__(self, customer_name, number, date, time, number_of_guests, menu):
        self.customer_name = customer_name
        self.number = number
        self.date = date
        self.time = time
        self.number_of_guests = number_of_guests
        self.menu = menu
        self.meal_choices = {}
        self.total_cost = 0


    def add_meal_choice(self, meal_name, quantity=1):
        if meal_name in self.menu.menu_list:
            self.meal_choices[meal_name] = self.meal_choices.get(meal_name, 0) + quantity
        else:
            print("There is no such meal in the menu")

    def remove_meal_choice(self, meal_name, quantity=1):
        if meal_name in (self.meal_choices):
            self.meal_choices[meal_name] = self.meal_choices.get(meal_name) - quantity
            if self.meal_choices[meal_name] <= 0:
                del self.meal_choices[meal_name]
            print(f"{meal_name} x {quantity} is removed from your order")
        else:
            print("There is no such meal in your order")

    def calculate_total_cost(self):
        self.total_cost = sum(self.menu.menu_list[meal][0] * quantity 
                              for meal, quantity in self.meal_choices.items())

    def __str__(self):
        self.calculate_total_cost()
        meal_choices_str = ', '.join([f"{meal} (x{quantity})" 
                                      for meal, quantity in self.meal_choices.items()])
        return (f"Customer name: {self.customer_name}\nPhone number: {self.number}\nDate: {self.date}\n"
                f"Time: {self.time}\nNumber of guests: {self.number_of_guests}\n"
                f"Meal choices: {meal_choices_str}\nTotal cost: {self.total_cost}$")

