from management.repository import insert_rocket, insert_company, insert_account
from db.auth import hash_password


def seed_rockets():
    rakiety = [
        ("Falcon 9", "SpaceX", 200000, 22800, 70000000),
        ("Starship", "SpaceX", 500000, 150000, 200000000),
        ("Soyuz", "Roscosmos", 180000, 7200, 50000000),
        ("Ariane 5", "ESA", 200000, 21000, 140000000),
        ("Long March 5", "CNSA", 300000, 25000, 90000000),
        ("H3", "JAXA", 250000, 18000, 80000000),
        ("GSLV Mk III", "ISRO", 300000, 10000, 60000000)
    ]

    for r in rakiety:
        insert_rocket(*r)


def seed_companies():
    companies = [
        ("CosmoCorp", "cosmoboss", "orbital", 5_000_000_000),
        ("Budget Launch Systems", "cheapshot", "launchme", 70_000_000),
        ("PJATK", "s27612", "bartek123", 1_000_000_000),
        ("PoorCorp", 'poor', 'megabieda', 0)
    ]

    for name, username, password, budget in companies:
        company_id = insert_company(name, budget)
        insert_account(company_id, username, hash_password(password))


if __name__ == "__main__":
    seed_rockets()
