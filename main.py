from db.auth import login, register
import management.service as service
from management.helper import pretty_print

# ========================================================
#                   🔑 DOSTĘP DO KONT 🔑
# ========================================================
# Nazwa firmy              | Username     | Hasło
# --------------------------------------------------------
# CosmoCorp                | cosmoboss    | orbital
# Budget Launch Systems    | cheapshot    | launchme
# PJATK                    | s27612       | bartek123
# ========================================================

current_user = None # fake sesja

def main_menu():
    global current_user
    while True:
        if not current_user:
            print("Welcome to RocketDealer.pl🚀")
            print("1. Register ➕\n2. Login 🔑\n3. Exit ⁉️")
            choice = input("Select: ")
            if choice == "1":
                username = input("Username: ")
                password = input("Password: ")
                name = input("Company name: ")
                budget = int(input("Initial budget: "))
                register(username, password, name, budget)
            elif choice == "2":
                username = input("Username: ")
                password = input("Password: ")
                user = login(username, password)
                if user:
                    current_user = user
            elif choice == "3":
                pretty_print("Application closed! See you soon!", tag="SUCCESS")
                break
        else:
            print(f"\nWelcome {current_user['name']}! Budget: {current_user['budget']} USD")
            print("1. Logout\n"
                  "2. Show rockets\n"
                  "3. Show available rockets\n"
                  "4. Show rocket details\n"
                  "5. Purchase rocket\n"
                  "6. Show purchase history\n"
                  )
            choice = input("Select: ")
            if choice == "1":
                pretty_print("Logout successful!", tag="SUCCESS")
                current_user = None
            elif choice == "2":
                service.show_all_rockets()
            elif choice == "3":
                service.show_available_rockets()
            elif choice == "4":
                service.select_rocket()
            elif choice == "5":
                service.purchase_rocket(current_user["company_id"])
            elif choice == "6":
                service.show_history(current_user["company_id"])

if __name__ == "__main__":
    main_menu()
