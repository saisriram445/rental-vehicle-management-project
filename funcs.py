from db import connection


# 1. VIEW ALL VEHICLES
def get_all_vehicles():
    c = connection()
    cursor = c.cursor()

    query = "SELECT * FROM vehicles"
    cursor.execute(query)

    res = cursor.fetchall()

    if len(res) == 0:
        print("No vehicles found.")
    else:
        print_vehicles(res)

    cursor.close()
    c.close()


# 2. VIEW PARTICULAR VEHICLE
def get_particular_vehicle():
    vehicle_id = int(input("Enter vehicle ID: "))

    c = connection()
    cursor = c.cursor()

    query = "SELECT * FROM vehicles WHERE id=%s"
    cursor.execute(query, (vehicle_id,))

    res = cursor.fetchone()

    if res:
        print_single_vehicle(res)
    else:
        print("Vehicle not found.")

    cursor.close()
    c.close()


# 3. ADD VEHICLE
def add_vehicle():
    vehicle_name = input("Enter vehicle name: ")
    vehicle_type = input("Enter vehicle type: ")
    price = int(input("Enter price per day: "))

    c = connection()
    cursor = c.cursor()

    query = """
    INSERT INTO vehicles
    (vehicle_name, vehicle_type, price_per_day, status)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(
        query,
        (vehicle_name, vehicle_type, price, "Available")
    )

    c.commit()

    print("Vehicle added successfully.")

    cursor.close()
    c.close()


# 4. DELETE VEHICLE
def delete_vehicle(vehicle_id):
    c = connection()
    cursor = c.cursor()

    query = "DELETE FROM vehicles WHERE id=%s"

    cursor.execute(query, (vehicle_id,))

    if cursor.rowcount > 0:
        c.commit()
        print("Vehicle deleted successfully.")
    else:
        print("Vehicle not found.")

    cursor.close()
    c.close()


# 5. UPDATE VEHICLE
def update_vehicle():
    vehicle_id = int(input("Enter vehicle ID to update: "))

    c = connection()
    cursor = c.cursor()

    check_query = "SELECT * FROM vehicles WHERE id=%s"
    cursor.execute(check_query, (vehicle_id,))

    vehicle = cursor.fetchone()

    if vehicle is None:
        print("Vehicle not found.")
        cursor.close()
        c.close()
        return

    vehicle_name = input("Enter new vehicle name: ")
    vehicle_type = input("Enter new vehicle type: ")
    price = int(input("Enter new price per day: "))

    query = """
    UPDATE vehicles
    SET vehicle_name=%s,
        vehicle_type=%s,
        price_per_day=%s
    WHERE id=%s
    """

    cursor.execute(
        query,
        (vehicle_name, vehicle_type, price, vehicle_id)
    )

    c.commit()

    print("Vehicle updated successfully.")

    cursor.close()
    c.close()


# 6. SEARCH VEHICLE
def search_vehicle():
    keyword = input("Enter vehicle name or type to search: ")

    c = connection()
    cursor = c.cursor()

    query = """
    SELECT * FROM vehicles
    WHERE vehicle_name LIKE %s
    OR vehicle_type LIKE %s
    """

    search_value = "%" + keyword + "%"

    cursor.execute(
        query,
        (search_value, search_value)
    )

    res = cursor.fetchall()

    if len(res) == 0:
        print("No matching vehicles found.")
    else:
        print_vehicles(res)

    cursor.close()
    c.close()


# 7. RENT VEHICLE
def rent_vehicle():
    vehicle_id = int(input("Enter vehicle ID to rent: "))

    c = connection()
    cursor = c.cursor()

    check_query = "SELECT * FROM vehicles WHERE id=%s"
    cursor.execute(check_query, (vehicle_id,))

    vehicle = cursor.fetchone()

    if vehicle is None:
        print("Vehicle not found.")

    elif vehicle[4] == "Rented":
        print("Vehicle is already rented.")

    else:
        update_query = """
        UPDATE vehicles
        SET status='Rented'
        WHERE id=%s
        """

        cursor.execute(update_query, (vehicle_id,))
        c.commit()

        print("Vehicle rented successfully.")

    cursor.close()
    c.close()


# 8. RETURN VEHICLE
def return_vehicle():
    vehicle_id = int(input("Enter vehicle ID to return: "))

    c = connection()
    cursor = c.cursor()

    check_query = "SELECT * FROM vehicles WHERE id=%s"
    cursor.execute(check_query, (vehicle_id,))

    vehicle = cursor.fetchone()

    if vehicle is None:
        print("Vehicle not found.")

    elif vehicle[4] == "Available":
        print("Vehicle is already available.")

    else:
        update_query = """
        UPDATE vehicles
        SET status='Available'
        WHERE id=%s
        """

        cursor.execute(update_query, (vehicle_id,))
        c.commit()

        print("Vehicle returned successfully.")

    cursor.close()
    c.close()


# PRINT ALL VEHICLES
def print_vehicles(vehicles):

    for vehicle in vehicles:

        print("ID:", vehicle[0])
        print("Vehicle Name:", vehicle[1])
        print("Vehicle Type:", vehicle[2])
        print("Price Per Day:", vehicle[3])
        print("Status:", vehicle[4])

        print("=====================================================")


# PRINT SINGLE VEHICLE
def print_single_vehicle(vehicle):

    print("ID:", vehicle[0])
    print("Vehicle Name:", vehicle[1])
    print("Vehicle Type:", vehicle[2])
    print("Price Per Day:", vehicle[3])
    print("Status:", vehicle[4])

    print("=====================================================")