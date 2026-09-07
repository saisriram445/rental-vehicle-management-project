from funcs import (
    get_all_vehicles,
    get_particular_vehicle,
    add_vehicle,
    delete_vehicle,
    update_vehicle,
    search_vehicle,
    rent_vehicle,
    return_vehicle
)


print("==================== RENTAL VEHICLE MANAGEMENT SYSTEM ====================")

while True:

    print()
    print("1. View All Vehicles")
    print("2. View Particular Vehicle")
    print("3. Add Vehicle")
    print("4. Delete Vehicle")
    print("5. Update Vehicle")
    print("6. Search Vehicle")
    print("7. Rent Vehicle")
    print("8. Return Vehicle")
    print("9. Exit")

    print()

    choice = int(input("Enter your choice: "))

    if choice == 1:
        get_all_vehicles()

    elif choice == 2:
        get_particular_vehicle()

    elif choice == 3:
        add_vehicle()

    elif choice == 4:
        vehicle_id = int(input("Enter vehicle ID to delete: "))
        delete_vehicle(vehicle_id)

    elif choice == 5:
        update_vehicle()

    elif choice == 6:
        search_vehicle()

    elif choice == 7:
        rent_vehicle()

    elif choice == 8:
        return_vehicle()

    elif choice == 9:
        print("Thank you for using Rental Vehicle Management System.")
        break

    else:
        print("Invalid choice. Please try again.")