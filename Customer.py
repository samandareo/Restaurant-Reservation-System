import os
from Menu import menu
from Reservation import Reservation



class Customer:
    def clear(self):
        if os.name == "nt":
            os.system("cls")

    def __init__ (self,login,password):
        self.login = login
        self.password = password
        self.reservation_list = []

    def meal_menu(self):
        from Manager import menu
        menu.display_menu()

    def main_menu(self):
        print("# ------------------- HOME ------------------- #")
        print("[1] Book table")
        print("[2] Reservations list")
        print("[3] Menu")
        print("[4] Restaurant details")
        print("[5] Exit\n")

    def sub_menu(self):
        print("# -------------- BOOK TABLE MENU -------------- #")
        print("[1] Add meal to the order")
        print("[2] Remove meal from the order")
        print("[3] Display order")
        print("[4] Confirm order")
        print("[5] Back\n")


    def check_reservation_conflicts(self, date, time):
        for i in self.reservation_list:
            if date == i.date and time == i.time:
                self.clear()
                print("This date and time is already reserved\n")
                print("Please enter again date and time\n")
                return False
        return True
    
    def book_table(self):
        print("# ------ Please enter your information ----- #")
        if len(self.reservation_list) >0:
            name = customer.reservation_list[-1].customer_name
            phone_number = customer.reservation_list[-1].number
            while True:
                date = input("Date (dd-mm-yyyy) : ")
                time = input("Time (hh:mm) : ")
                if(self.check_reservation_conflicts(date,time)):
                    break
            number_of_guests = input("Number of guests : ")
        else:
            name = input("Name : ")
            phone_number = input("Phone number : ")
            while True:
                date = input("Date (dd-mm-yyyy) : ")
                time = input("Time (hh:mm) : ")
                if(self.check_reservation_conflicts(date,time)):
                    break
            number_of_guests = input("Number of guests : ")
        
        while True:
            if number_of_guests.isdigit() == False:
                print("Invalid price\n")
                number_of_guests = input("Enter again number of guests : ")
            else:
                number_of_guests = int(number_of_guests)
                break
        
        global reservation
        reservation = Reservation(name,phone_number,date,time,number_of_guests,menu)
    def choose_meal(self):
        if os.name == "nt":
            os.system("cls")

        print("# ------ Please choose meal from menu ----- #")
        menu.display_menu()
        print("-"*45+"\n")
        stop = True
        while stop:
            meal_name = input("Enter meal name (Exit - 0): ")
            if meal_name == "0":
                break
            if meal_name in menu.menu_list:
                while True:
                    meal_quantity = input("Enter meal quantity : ")
                    if meal_quantity.isdigit() == False:
                        print("Please enter number\n")
                        continue
                    else:
                        meal_quantity = int(meal_quantity)

                    if meal_quantity == 1:
                        reservation.add_meal_choice(meal_name)
                        print(f"{meal_name} is added to your order\n")
                        break
                    elif meal_quantity > 1:
                        reservation.add_meal_choice(meal_name,meal_quantity)
                        print(f"{meal_name} is added to your order\n")
                        break
                    else:
                        print("Invalid quantity\n")
                        continue
            else:
                print("There is no such meal in the menu\n")
                continue

            choice = input("Do you want to add more meals? (y/n) : ")
            if choice == 'y':
                continue
            elif choice == 'n':
                customer.clear()
                stop = False
            else:
                print("Invalid choice\n")
                continue

    def display_order(self):
        print("# ------ Your order ----- #")
        print(reservation)
        print("-"*45+"\n")

    def remove_meal(self):

        print("# ------ Please choose meal from list ----- #")
        #display only meals in the order
        print()
        self.display_order()

        print("-"*45+"\n")
        stop = True
        while stop:
            meal_name = input("Enter meal name (Exit - 0): ")
            if meal_name == "0":
                break
            
            if meal_name in menu.menu_list:
                while True:
                    meal_quantity = input("Enter meal quantity : ")
                    if meal_quantity.isdigit() == False:
                        print("Please enter number\n")
                        continue
                    else:
                        meal_quantity = int(meal_quantity)
                        
                    if meal_quantity > reservation.meal_choices.get(meal_name):
                        print("You don't have such quantity in your order\n")
                        continue
                    if meal_quantity == 1:
                        reservation.remove_meal_choice(meal_name)
                        break
                    elif meal_quantity > 1:
                        reservation.remove_meal_choice(meal_name,meal_quantity)
                        break
                    else:
                        print("Invalid quantity\n")
                        continue
            else:
                print("There is no such meal in the menu\n")
                continue

            choice = input("Do you want to remove more meals? (y/n) : ")
            if choice == 'y':
                continue
            elif choice == 'n':
                stop = False
            else:
                print("Invalid choice\n")
                continue

    def confirm_reservation(self):
        self.clear()

        print("# ------ Confirm reservation ----- #")
        print(reservation)
        print("-"*45+"\n")
        choice = input("Do you want to confirm reservation? (y/n) : ")

        global resrv_confirm
        resrv_confirm = False
        if choice == 'y':
            self.reservation_list.append(reservation)
            customer.clear()
            print("Your reservation is confirmed\n")
            resrv_confirm = True
            print(reservation)
            return
        elif choice == 'n':
            print("Your reservation is canceled\n")
            return
        else:
            print("Invalid choice\n")
            return

    def edit_reservation(self):
        while True:
            print("# ------ Reservation list ----- #")
            for i in self.reservation_list:
                print(i)
                print()
            print()
            print("[1] Edit reservation")
            print("[2] Cancel reservation")
            print("[3] Back\n")
            choice = int(input("Enter your choice : "))
            print()
            if choice == 1:
                print("# ------ Edit reservation ----- #")
                print()
                if len(self.reservation_list) == 0:
                    print("Reservation list is empty\n")
                    return
                else:
                    for i in range(len(self.reservation_list)):
                        print(f"({i+1}) {self.reservation_list[i].customer_name} | {self.reservation_list[i].date} | {self.reservation_list[i].time} | {self.reservation_list[i].number_of_guests} guests")
                    print()
                    index = int(input("Enter index of reservation : "))
                    print()
                    if index > len(self.reservation_list) or index < 1:
                        print("Invalid index\n")
                        return
                    else:
                        while True:
                            customer.clear()
                            print("# ------ Update Reservation ----- #")
                            print()
                            print(self.reservation_list[index-1])
                            print()
                            print("[1] Edit reservation infromation")
                            print("[2] Edit order")
                            print("[3] Back\n")
                            choice = int(input("Enter your choice : "))
                            print()
                            if choice == 1:
                                while True:
                                    print("# ------ Edit reservation information ----- #")
                                    print()
                                    print("[1] Edit name")
                                    print("[2] Edit phone number")
                                    print("[3] Edit date")
                                    print("[4] Edit time")
                                    print("[5] Edit number of guests")
                                    print("[6] Back\n")
                                    choice = int(input("Enter your choice : "))
                                    print()
                                    if choice == 1:
                                        name = input("Enter name : ")
                                        self.reservation_list[index-1].customer_name = name
                                        customer.clear()
                                        print("Name is updated\n")
                                        continue
                                    elif choice == 2:
                                        phone_number = input("Enter phone number : ")
                                        self.reservation_list[index-1].number = phone_number
                                        customer.clear()
                                        print("Phone number is updated\n")
                                        continue
                                    elif choice == 3:
                                        date = input("Enter date (dd-mm-yyyy) : ")
                                        self.reservation_list[index-1].date = date
                                        customer.clear()
                                        print("Date is updated\n")
                                        continue
                                    elif choice == 4:
                                        time = input("Enter time (hh:mm) : ")
                                        self.reservation_list[index-1].time = time
                                        customer.clear()
                                        print("Time is updated\n")
                                        continue
                                    elif choice == 5:
                                        number_of_guests = input("Enter number of guests : ")
                                        while True:
                                            if number_of_guests.isdigit() == False:
                                                print("Invalid price\n")
                                                number_of_guests = input("Enter again number of guests : ")
                                            else:
                                                number_of_guests = int(number_of_guests)
                                                break
                                        self.reservation_list[index-1].number_of_guests = number_of_guests
                                        customer.clear()
                                        print("Number of guests is updated\n")
                                    elif choice == 6:
                                        break
                                    else:
                                        print("Invalid choice\n")
                                        customer.clear()
                                        continue
                            elif choice == 2:
                                while True:
                                    customer.clear()
                                    customer.display_order()
                                    print()
                                    print("[1] Add meal to the order")
                                    print("[2] Remove meal from the order")
                                    print("[3] Back\n")
                                    choice = int(input("Enter your choice : "))
                                    print()
                                    if choice == 1:
                                        customer.clear()
                                        customer.choose_meal()
                                        continue
                                    elif choice == 2:
                                        customer.clear()
                                        customer.remove_meal()
                                        continue
                                    elif choice == 3:
                                        customer.clear()
                                        break
                                    else:
                                        print("Invalid choice\n")
                                        continue
                            elif choice == 3:
                                customer.clear()
                                break
                            else:
                                print("Invalid choice\n")
                                continue
                            
            elif choice == 2:
                print("# ------ Cancel reservation ----- #")
                print()
                if len(self.reservation_list) == 0:
                    print("Reservation list is empty\n")
                    return
                else:
                    for i in range(len(self.reservation_list)):
                        print(f"({i+1}) {self.reservation_list[i].customer_name} | {self.reservation_list[i].date} | {self.reservation_list[i].time} | {self.reservation_list[i].number_of_guests} guests")
                    print()
                    index = int(input("Enter index of reservation : "))
                    print()
                    if index > len(self.reservation_list) or index < 1:
                        print("Invalid index\n")
                        return
                    else:
                        self.reservation_list.pop(index-1)
                        resrv_confirm = False
                        print("Reservation is canceled\n")
            elif choice == 3:
                return
            else:
                print("Invalid choice\n")
                return


customer = Customer("admin","admin")

def main():
    print("#"+"-#"*25+"\n"+"#                                                 #\n"+"#     Welcome to the restaurant booking system    #\n"+"#                                                 #\n"+"#"+"-#"*25+"\n")
    while True:
        customer.main_menu()
        choice = int(input("Enter your choice : "))
        print()


        if choice == 1:
            customer.clear()
            print("# ------------------- BOOK TABLE ------------------- #")
            print()
            customer.book_table()
            
            customer.clear()
            while True:
                customer.sub_menu()
                choice = int(input("Enter your choice : "))
                print()
                if choice == 1:
                    customer.clear()

                    customer.choose_meal()
                elif choice == 2:
                    customer.clear()
                    customer.remove_meal()
                elif choice == 3:
                    customer.clear()
                    customer.display_order()
                elif choice == 4:
                    customer.clear()
                    if len(reservation.meal_choices) == 0:
                        print(reservation)
                        print()
                        print("You didn't add any meal\n")
                        continue
                    customer.confirm_reservation()
                    break
                elif choice == 5:
                    customer.clear()
                    break
                else:
                    print("Invalid choice\n")
                    continue
        elif choice == 2:
            customer.clear()
            print("# ------------------- RESERVATION LIST ------------------- #")
            print()
            if len(customer.reservation_list) == 0:
                print("Reservation list is empty\n")
                continue
            print()
            customer.edit_reservation()
        elif choice == 3:
            customer.clear()
            print("# ------------------- MENU ------------------- #")
            menu.display_menu()
            print("\n")
        elif choice == 4:
            customer.clear()
            print("# ------------------- RESTAURANT DETAILS ------------------- #")
            print()
            print("Restaurant name : Restaurant")
            print("Address : 1234 Street")
            print("Phone number : 123456789")
            print("Email : restaurantGM@gmail.com")
            print("Website : www.restaurant.com")
            print("\n")
            continue
        elif choice == 5:
            print("Good bye")
            customer.clear()
            break
        else:
            print("Invalid choice\n")
            continue

if __name__ == "__main__":
    main()