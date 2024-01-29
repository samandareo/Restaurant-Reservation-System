class Menu:

    def __init__(self):
        self.menu_list = {"chik": [10, "Chicken with rice",
                                   "chicken, rice, meat, food, meal, dinner, lunch, chicken with rice, chic"], }

    def add(self, name, price, description, keywords):
        self.menu_list[name] = [price, description, keywords]

    def remove(self, name):
        if len(self.menu_list) == 0:
            print("Menu is empty")
            return
        elif name == None or name == "":
            print("Please enter a meal name")
            return
        elif name not in self.menu_list:
            print("There is no such meal in the menu")
            return
        else:
            self.menu_list.pop(name)

    def update(self, name, price=None, description=None, keywords=None):
        if len(self.menu_list) == 0:
            print("Menu is empty")
            return
        elif name == None or name == "":
            print("Please enter a meal name")
            return
        elif name not in self.menu_list:
            print("There is no such meal in the menu")
            return
        else:
            if price == None or price == "":
                price = self.menu_list[name][0]
            if description == None or description == "":
                description = self.menu_list[name][1]
            if keywords == None or keywords == "":
                keywords = self.menu_list[name][2]

            self.menu_list[name] = [price, description, keywords]

    def display_menu(self):
        if len(self.menu_list) == 0:
            print("Menu is empty")
            return

        cnt = 0
        for key, value in self.menu_list.items():
            cnt += 1
            print(f"({cnt}) {key}. {value[1]}. Price : {value[0]}$")

    def search(self, keyword):
        print(f"\nKEYWORD :  {keyword} ----------------------|")
        keyword = keyword.lower()
        found = False
        for key, value in self.menu_list.items():
            if keyword in value['keywords'].lower():
                found = True
                print(f"{key} | {value['description']} | Price is {value['price']}$")
        if not found:
            print(f"Meals are not found in relation to '{keyword}'")


menu = Menu()
