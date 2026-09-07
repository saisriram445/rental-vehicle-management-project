# 🚗 Rental Vehicle Management System

A **Rental Vehicle Management System** developed using **Python and MySQL** to manage vehicles and their rental availability.

The system provides a simple command-line interface that allows users to add, view, search, update, delete, rent, and return vehicles.

## 📌 Project Overview

The main objective of this project is to simplify vehicle rental management by maintaining vehicle details and availability status in a MySQL database.

The application uses Python for the application logic and **PyMySQL** to connect Python with MySQL.

## ✨ Features

The project contains the following 8 features:

1. **View All Vehicles**

   * Displays all vehicles stored in the database.

2. **View Particular Vehicle**

   * Searches for a vehicle using its ID.

3. **Add Vehicle**

   * Adds a new vehicle with its name, type, price per day, and availability status.

4. **Delete Vehicle**

   * Deletes a vehicle from the database using its ID.

5. **Update Vehicle**

   * Updates vehicle name, vehicle type, and rental price.

6. **Search Vehicle**

   * Searches vehicles by vehicle name or vehicle type.

7. **Rent Vehicle**

   * Changes the vehicle status from `Available` to `Rented`.

8. **Return Vehicle**

   * Changes the vehicle status from `Rented` back to `Available`.

## 🛠️ Technologies Used

* **Python**
* **MySQL**
* **PyMySQL**
* **Command Line Interface (CLI)**

## 📂 Project Structure

```text
Rental-Vehicle-Management-System/
│
├── app.py
├── db.py
├── funcs.py
└── README.md
```

### `app.py`

Contains the main menu and controls the user interaction.

It provides options for all 8 vehicle management operations.

### `db.py`

Contains the MySQL database connection configuration using PyMySQL.

### `funcs.py`

Contains the main functions for:

* Viewing vehicles
* Adding vehicles
* Deleting vehicles
* Updating vehicles
* Searching vehicles
* Renting vehicles
* Returning vehicles

## 🗄️ Database Structure

### Database

```sql
rental
```

### Table

```sql
vehicles
```

### Columns

| Column          | Data Type | Description          |
| --------------- | --------- | -------------------- |
| `id`            | INT       | Unique vehicle ID    |
| `vehicle_name`  | VARCHAR   | Name of the vehicle  |
| `vehicle_type`  | VARCHAR   | Type of vehicle      |
| `price_per_day` | INT       | Rental price per day |
| `status`        | VARCHAR   | Vehicle availability |

Example:

```text
ID: 1
Vehicle Name: Audi
Vehicle Type: Car
Price Per Day: 3000
Status: Available
```

## ⚙️ MySQL Setup

Create the database:

```sql
CREATE DATABASE rental;
```

Select the database:

```sql
USE rental;
```

Create the vehicles table:

```sql
CREATE TABLE vehicles (
    id INT PRIMARY KEY AUTO_INCREMENT,
    vehicle_name VARCHAR(100) NOT NULL,
    vehicle_type VARCHAR(50) NOT NULL,
    price_per_day INT NOT NULL,
    status VARCHAR(20) DEFAULT 'Available'
);
```

Add sample vehicles:

```sql
INSERT INTO vehicles
(vehicle_name, vehicle_type, price_per_day, status)
VALUES
('Audi', 'Car', 3000, 'Available'),
('BMW', 'Car', 3500, 'Available'),
('Royal Enfield', 'Bike', 1200, 'Available'),
('Toyota Innova', 'Car', 2500, 'Available');
```

## 📦 Installation

Install Python from the official Python website if it is not already installed.

Install PyMySQL:

```bash
pip install pymysql
```

## 🔧 Database Configuration

Open `db.py` and configure your MySQL credentials:

```python
from pymysql import connect

def connection():
    connection = connect(
        host="localhost",
        user="root",
        password="YOUR_PASSWORD",
        database="rental"
    )

    return connection
```

Replace `YOUR_PASSWORD` with your MySQL password.

**Do not upload your real database password to GitHub.**

## ▶️ How to Run

Open the project folder in the terminal:

```bash
cd Rental-Vehicle-Management-System
```

Run the application:

```bash
python app.py
```

The application displays:

```text
==================== RENTAL VEHICLE MANAGEMENT SYSTEM ====================

1. View All Vehicles
2. View Particular Vehicle
3. Add Vehicle
4. Delete Vehicle
5. Update Vehicle
6. Search Vehicle
7. Rent Vehicle
8. Return Vehicle
9. Exit

Enter your choice:
```

## 🔄 Vehicle Rental Flow

```text
Vehicle Added
     ↓
Available
     ↓
Rent Vehicle
     ↓
Rented
     ↓
Return Vehicle
     ↓
Available
```

## 🎯 Project Objective

The objective of this project is to develop a simple and efficient vehicle rental management system that can maintain vehicle information and track whether vehicles are available or rented.

## 🚀 Future Enhancements

The project can be further improved by adding:

* Customer management
* Rental history
* Customer details
* Rental date and return date
* Automatic rental cost calculation
* Login and authentication
* Graphical User Interface
* Online booking
* Payment integration

## 👨‍💻 Author

**Mettela Saisriram**

### Project

**Rental Vehicle Management System**

### Technologies

**Python | MySQL | PyMySQL**
