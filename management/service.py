import datetime
import management.repository as repository
from management.helper import pretty_print

def show_all_rockets():
    print("============== All Rockets! ==============")
    for rocket in repository.get_all_rockets():
        print(str(rocket["id"]) + " " + rocket["name"])
    print("==========================================")

def show_available_rockets():
    print("========== Available Rockets! ============")
    for rocket in repository.get_available_rockets():
        print(str(rocket["id"]) + " " + rocket["name"])
    print("==========================================")

def select_rocket():
    rocket_id = input("Insert rocket id: ")
    rocket = repository.get_rocket_by_id(rocket_id)
    if rocket is not None:
        print("============== {} INFO ==============".format(rocket["name"]))
        print("Manufacturer: " + rocket["manufacturer"])
        print("Range(KM): " + str(rocket["range"]))
        print("Payload(KG): " + str(rocket["payload"]))
        print("Price(USD): " + str(rocket["price"]))
        print("Available: " + ("Yes" if rocket["available"] else "No"))
        print("==========================================")
    else:
        pretty_print("Rocket not found!")

def purchase_rocket(company_id):
    rocket_id = input("Insert rocket ID to purchase: ")

    rocket = repository.get_rocket_by_id(rocket_id)
    if rocket is None:
        pretty_print("Rocket not found.")
        return

    if not rocket["available"]:
        pretty_print("Rocket is not available.")
        return

    company = repository.get_company_by_id(company_id)
    if company is None:
        pretty_print("Company not found.", tag="ERROR")
        return

    if company["budget"] < rocket["price"]:
        pretty_print("Not enough budget.")
        return

    new_budget = company["budget"] - rocket["price"]
    repository.update_company_budget(company_id, new_budget)

    repository.update_rocket_availability(rocket["id"], 0)

    today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    repository.insert_purchase(rocket["id"], company_id, rocket["price"], today)

    message = "Rocket " + rocket["name"] + " purchased successfully!"
    pretty_print(message, tag="SUCCESS")


def show_history(company_id):
    history = repository.get_purchases_by_company(company_id)
    if not history:
        pretty_print("No purchases found.", tag="INFO")
        return

    pretty_print("Purchase History:", tag="INFO")
    for item in history:
        print(f"- Rocket: {item['name']} | Price: {item['price']}$ | Date: {item['purchase_date']}")