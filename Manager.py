import os
from Menu import menu
from Customer import customer

class Manager:
    def __init__ (self,login,password):
        self.login = login
        self.password = password

if os.name == "nt":
    os.system("cls")

def main():
    print("#"+"-#"*25+"\n"+"#                                                 #\n"+"#   Welcome to the restaurant management system   #\n"+"#                                                 #\n"+"#"+"-#"*25+"\n")

    def clear():
        if os.name == "nt":
            os.system("cls")

    manager = Manager("sam","1234")
    while True:
        print("\nPlease enter your login and password\n")
        login = input("Enter login : ")
        password = input("Enter password : ")
        print()
        if login == manager.login and password == manager.password:
            clear()

            print("Welcome to the system\n")

            def show_menu():
                print("# ------------------- HOME ------------------- #")
                print("[1] Add meal to the menu")
                print("[2] Remove meal from the menu")
                print("[3] Update meal in the menu")
                print("[4] Display menu")
                print("[5] Search meal in the menu")
                print("[6] Reservations")
                print("[7] Exit\n")

            while True:
                show_menu()
                choice = int(input("Enter your choice : "))
                print()

                if choice == 1:
                    clear()
                    print("# ------ Please enter meal information ----- #")

                    if len(menu.menu_list) == 10:
                        print("You can't add more than 10 meals\n")
                        continue
                    else:
                        menu.display_menu()
                    print("-"*45+"\n")
                    
                    global cancel
                    cancel = False
                    stop = True
                    while stop:
                        name = input("Enter meal name :(Cancel - 0) ")

                        if name == "0":
                            cancel = True
                            break

                        if name in menu.menu_list:
                            print("There is such meal in the menu\n")
                            continue
                        
                        price = input("Enter meal price : ")
                        while True:
                            if price.isdigit() == False:
                                print("Invalid price\n")
                                price = input("Enter meal price : ")
                            else:
                                price = float(price)
                                break


                        description = input("Enter meal description : ")
                        while True:
                            if description == "":
                                print("Invalid description\n")
                                description = input("Enter meal description : ")
                            else:
                                break

                        keywords = input("Enter meal keywords : ")
                        while True:
                            if keywords == "":
                                print("Invalid keywords\n")
                                keywords = input("Enter meal keywords : ")
                            else:
                                break
                        stop = False

                    if cancel == True:
                        clear()
                        continue

                    menu.add(name,price,description,keywords)
                    print(f"{name} is added to the menu\n")
                    clear()
                elif choice == 2:
                    clear()
                    print("# --------------- Remove meal ---------------- #")
                    if len(menu.menu_list) == 0:
                        print("Menu is empty\n")
                        continue
                    else:
                        menu.display_menu()

                    print()
                    name = input("Enter meal name : ")
                    menu.remove(name)
                    print(f"{name} is removed from the menu\n")
                    clear()
                elif choice == 3:
                    clear()
                    print("# --------------- Update meal ---------------- #")
                    if len(menu.menu_list) == 0:
                        print("Menu is empty\n")
                        continue
                    else:
                        menu.display_menu()
                    print()

                    while True:
                        name = input("Enter meal name(match with list) (Cancel - 0): ")

                        if name == "0":
                            break

                        if name not in menu.menu_list:
                            print("There is no such meal in the menu\n")
                            continue
                        else:
                            while True:
                                price = input("Enter meal price : ")
                                if price.isdigit() == False:
                                    print("Invalid price\n")
                                    continue
                                else:
                                    price = float(price)
                                    break

                            description = input("Enter meal description : ")
                            keywords = input("Enter meal keywords : ")
                            menu.update(name,price,description,keywords)
                            print(f"{name} is updated in the menu\n")
                            break
                    clear()
                elif choice == 4:
                    clear()
                    print("# ------------------- MENU ------------------- #")
                    menu.display_menu()
                    print()
                elif choice == 5:
                    clear()
                    print("# ------------------- SEARCH ------------------- #")
                    keyword = input("Enter keyword (Cancel - 0): ")
                    if keyword == "0":
                        continue
                    menu.search(keyword)
                    print("\n")
                elif choice == 6:
                    clear()
                    print("# ------------------- RESERVATION LIST ------------------- #")
                    print()
                    if len(customer.reservation_list) == 0:
                        print("Reservation list is empty\n")
                        continue
                    print()
                    customer.edit_reservation()
                elif choice == 7:
                    break
                else:
                    print("Invalid choice\n")
        else:
            clear()
            print("Invalid login or password")
            continue

if __name__ == "__main__":
    main()