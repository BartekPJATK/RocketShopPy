from db.core import with_db

# -----------------------------
# ROCKETS
# -----------------------------
@with_db
def insert_rocket(conn, name, manufacturer, range_km, payload_kg, price_usd):
    conn.execute('''
        INSERT INTO rockets (name, manufacturer, range, payload, price)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, manufacturer, range_km, payload_kg, price_usd))
    conn.commit()

@with_db
def get_all_rockets(conn):
    return conn.execute("SELECT * FROM rockets").fetchall()

@with_db
def get_available_rockets(conn):
    return conn.execute("SELECT * FROM rockets WHERE available = 1").fetchall()

@with_db
def get_rocket_by_id(conn, rocket_id):
    return conn.execute("SELECT * FROM rockets WHERE id = ?", (rocket_id,)).fetchone()

@with_db
def update_rocket_availability(conn, rocket_id, available):
    conn.execute("UPDATE rockets SET available = ? WHERE id = ?", (available, rocket_id))
    conn.commit()


# -----------------------------
# COMPANIES
# -----------------------------
@with_db
def get_company_by_id(conn, company_id):
    return conn.execute("SELECT * FROM companies WHERE id = ?", (company_id,)).fetchone()

@with_db
def insert_company(conn, name, budget):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO companies (name, budget)
        VALUES (?, ?)
    ''', (name, budget))
    conn.commit()
    return cursor.lastrowid


@with_db
def update_company_budget(conn, company_id, new_budget):
    conn.execute("UPDATE companies SET budget = ? WHERE id = ?", (new_budget, company_id))
    conn.commit()


# -----------------------------
# PURCHASES
# -----------------------------
@with_db
def insert_purchase(conn, rocket_id, company_id, price_usd, purchase_date):
    conn.execute('''
        INSERT INTO purchases (rocket_id, company_id, purchase_date, price)
        VALUES (?, ?, ?, ?)
    ''', (rocket_id, company_id, purchase_date, price_usd))
    conn.commit()

@with_db
def get_purchases_by_company(conn, company_id):
    return conn.execute('''
        SELECT rockets.name, purchases.price, purchases.purchase_date
        FROM purchases
        JOIN rockets ON purchases.rocket_id = rockets.id
        WHERE purchases.company_id = ?
    ''', (company_id,)).fetchall()


# -----------------------------
# COMPANY ACCOUNTS
# -----------------------------
@with_db
def insert_account(conn, company_id, username, password):
    conn.execute('''
        INSERT INTO company_accounts (company_id, username, password)
        VALUES (?, ?, ?)
    ''', (company_id, username, password))
    conn.commit()

@with_db
def get_account_by_username(conn, username):
    return conn.execute('''
        SELECT ca.*, c.name, c.budget
        FROM company_accounts ca
        JOIN companies c ON ca.company_id = c.id
        WHERE ca.username = ?
    ''', (username,)).fetchone()