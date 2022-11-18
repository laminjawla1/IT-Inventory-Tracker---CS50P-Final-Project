import os
import time
import sys
import sqlite3
import pandas as pd  # type: ignore
from cs50 import get_int, get_string  # type: ignore
from colorama import Fore
from inv_utils import Inventory, get_date, get_status, get_category
from tabulate import tabulate


def main() -> None:
    clear()
    while True:
        menu()
        user_choice = get_int(Fore.CYAN + "Choose: ")

        match user_choice:
            case 1:
                clear()
                dashboard()
                input(Fore.CYAN + "Press any key to continue: ")
                clear()

            case 2:
                if add_item():
                    print(Fore.GREEN + "Item added successfully")
                else:
                    print(Fore.RED + "An error occured! Could not save data")

                input(Fore.CYAN + "Press any key to continue: ")
                clear()

            case 3:
                clear()
                results = view_items()
                if results:
                    print(f"{Fore.GREEN}{results}")
                else:
                    print(Fore.RED + "No Mathces were found")
                input(Fore.CYAN + "Press any key to continue: ")
                clear()

            case 4:
                results = search_item()
                if results:
                    print(f"{Fore.GREEN}{results}")
                else:
                    print(Fore.RED + "No Mathces were found")
                input(Fore.CYAN + "Press any key to continue: ")
                clear()
            case 5:
                if edit_item():
                    print(Fore.GREEN + "Done")
                else:
                    print(Fore.RED + "No Mathces were found")
                input(Fore.CYAN + "Press any key to continue: ")
                clear()

            case 6:
                if delete_item():
                    print(Fore.GREEN + "Item deleted successfully")
                else:
                    print(Fore.RED + "No Mathces were found")
                input(Fore.CYAN + "Press any key to continue: ")
                clear()

            case 7:
                if export_items():
                    print(Fore.GREEN + "Items exported successfully")
                else:
                    print(Fore.RED + "No items to export")
                input(Fore.CYAN + "Press any key to continue: ")
                clear()

            case 0:
                quit()

            case _:
                clear()
                print(Fore.RED + "Invalid Command")
                time.sleep(1)


def menu() -> None:
    """
        Print a menu
    """

    print(Fore.YELLOW + "\t\t\tIT INVENTORY TRACKER. DEVELOPED BY LAMIN JAWLA\n")
    print(Fore.GREEN + "1️⃣  Dashboard\n2️⃣  Add Item\n3️⃣  View Items\n4️⃣  Search Item\n5️⃣  Edit Item\n6️⃣  Delete Item\n7️⃣  Export Items\n0️⃣  Quit\n")


def dashboard() -> None:
    """
    Print a formated dashboard after reading the database

    """

    print(Fore.YELLOW + "\t\t\t\tDASHBOARD\n")
    con = sqlite3.connect('inventory50.db')
    cur = con.cursor()

    with con:
        cur.execute("SELECT * FROM inventory")
        result = cur.fetchall()
    total_items = len(result)

    with con:
        cur.execute("SELECT * FROM inventory WHERE category=:category",
                    {"category": 'CPU'})
        result = cur.fetchall()
    cpus = len(result)

    with con:
        cur.execute("SELECT * FROM inventory WHERE category=:category",
                    {"category": 'Monitor'})
        result = cur.fetchall()
    monitors = len(result)

    with con:
        cur.execute("SELECT * FROM inventory WHERE category=:category",
                    {"category": 'Peripheral'})
        result = cur.fetchall()
    peripherals = len(result)

    with con:
        cur.execute("SELECT * FROM inventory WHERE category=:category",
                    {"category": 'Laptop'})
        result = cur.fetchall()
    laptops = len(result)

    print(f"{Fore.RED}CPUs: {Fore.YELLOW}{cpus}\t\t\t{Fore.RED}MONITORS: {Fore.YELLOW}{monitors}")
    print(f"{Fore.RED}PERIPHERALS: {Fore.YELLOW}{peripherals}\t\t{Fore.RED}LAPTOPS: {Fore.YELLOW}{laptops}\n")
    print(Fore.RED + "\t\tTOTAL ITEMS:", Fore.YELLOW + str(total_items) + "\n")


def add_item() -> bool:
    """
        Add an item to the database

        :return: True if successful and False if unsuccessful
        :rtype: bool

    """

    clear()
    print(Fore.YELLOW + "\t\t\tADD ITEM\n")
    con = sqlite3.connect('inventory50.db')
    cur = con.cursor()

    try:
        cur.execute(
            "CREATE TABLE inventory(model text, serial_number text, category text, location text, status text, description text, date text)")
    except sqlite3.OperationalError:
        pass

    model = get_string(Fore.CYAN + "Model: ")
    serial_number = get_string("Serial Number: ")
    category = get_category()
    location = get_string("Location: ")
    status = get_status()
    description = get_string("Description: ")
    date = get_date("Enter date in YYYY-MM-DD format: ")

    item = Inventory(model, serial_number, category,
                     location, status, description, date)

    try:
        with con:
            cur.execute("INSERT INTO inventory VALUES (:model, :serial_number, :category, :location, :status, :description, :date)", {
                        "model": item.model, "serial_number": item.serial_number, "category": item.category, "location": item.location, "status": item.status, "description": item.description, "date": item.date})
            return True
    except:
        return False


def view_items() -> str:
    """
        Tabulate and return the items in the database

        :return: None
        :rtype: None

    """

    print(Fore.YELLOW + "\t\t\t\tITEMS IN THE DATABASE\n")
    con = sqlite3.connect('inventory50.db')
    cur = con.cursor()

    with con:
        cur.execute("SELECT * FROM inventory")
        result = cur.fetchall()

    if result:
        result.insert(0, ["MODEL", "SERIAL NUMBER", "CATEGORY",
                      "LOCATION", "STATUS", "DESCRIPTION", "DATE"])
        return tabulate(result[1:], headers=result[0], tablefmt="grid")
    else:
        return ""


def search_item() -> str:
    """
        Search an item in the database

        The item can only be searched if the model is known before hand

        :return: list if successful and False if unsuccessful
        :rtype: bool

    """

    clear()
    print(Fore.YELLOW + "\t\t\tSEARCH ITEM\n")
    key = get_string(Fore.RED + "Type the model of the item to search: ")
    con = sqlite3.connect('inventory50.db')
    cur = con.cursor()

    with con:
        cur.execute("SELECT * FROM inventory WHERE model=:model",
                    {"model": key})
        result = cur.fetchall()

    if result:
        result.insert(0, ["MODEL", "SERIAL NUMBER", "CATEGORY",
                      "LOCATION", "STATUS", "DESCRIPTION", "DATE"])
        return tabulate(result[1:], headers=result[0], tablefmt="grid")
    else:
        return ""


def edit_item() -> bool:
    """
        Edit the properties of an item in the database

        The item can only be edited if the serial number is known before hand

        :return: True if successful and False if unsuccessful
        :rtype: bool

    """

    print(Fore.YELLOW + "\t\t\tEDIT ITEM\n")
    con = sqlite3.connect('inventory50.db')
    cur = con.cursor()
    clear()
    key = get_string(
        "Search the serial number of the device you want to edit: ")

    clear()
    with con:
        cur.execute(
            "SELECT * FROM inventory WHERE serial_number=:serial_number", {"serial_number": key})
        result = cur.fetchall()
    if result:
        print(Fore.GREEN + "1️⃣  Model\n2️⃣  Serial Number\n3️⃣  Location\n4️⃣  Status\n5️⃣  Description\n6️⃣  Date\n0️⃣  Return to main menu\n")
        user_choice = get_int("Select the information you want to modify: ")
        match user_choice:
            case 1:
                model = get_string("Model: ")
                with con:
                    cur.execute("UPDATE inventory SET model = :model WHERE serial_number = :serial_number", {
                                "serial_number": key, "model": model})
                return True
            case 2:
                serial_number = get_string("Serial Number: ")
                with con:
                    cur.execute("UPDATE inventory SET serial_number = :serial_number WHERE serial_number = :serial_number", {
                                "serial_number": key, "serial_number": serial_number})
                return True

            case 3:
                location = get_string("Location: ")
                with con:
                    cur.execute("UPDATE inventory SET location = :location WHERE serial_number = :serial_number", {
                                "serial_number": key, "location": location})
                return True

            case 4:
                status = get_status()
                with con:
                    cur.execute("UPDATE inventory SET status = :status WHERE serial_number = :serial_number", {
                                "serial_number": key, "status": status})
                return True

            case 5:
                description = get_string("Description: ")
                with con:
                    cur.execute("UPDATE inventory SET description = :description WHERE serial_number = :serial_number", {
                                "serial_number": key, "description": description})
                return True

            case 6:
                date = get_date("Enter date in YYYY-MM-DD format: ")
                with con:
                    cur.execute("UPDATE inventory SET date = :date WHERE serial_number = :serial_number", {
                                "serial_number": key, "date": date})
                return True

            case 0:
                main()

            case _:
                main()

    else:
        return False
    return False


def delete_item() -> bool:
    """
        Delete an item in the database

        The item can only be deleted if the serial number is known before hand

        :return: True if successful and False if unsuccessful
        :rtype: bool

    """

    print(Fore.YELLOW + "\t\t\tDELETE ITEM\n")
    con = sqlite3.connect('inventory50.db')
    cur = con.cursor()

    serial_number = get_string(
        "Search the serial number of the device you want to edit: ")

    with con:
        cur.execute("SELECT * FROM inventory WHERE serial_number=:serial_number",
                    {"serial_number": serial_number})
        result = cur.fetchone()
        if result:
            with con:
                cur.execute("DELETE from inventory WHERE serial_number = :serial_number", {
                            "serial_number": serial_number})
            return True
        else:
            return False


def export_items() -> bool:
    """
        Export items in the database to a csv file

        :return: True if successful and False if unsuccessful
        :rtype: bool

    """
    con = sqlite3.connect('inventory50.db')
    cur = con.cursor()

    with con:
        cur.execute("SELECT * FROM inventory")
        result = cur.fetchall()

    if result:
        df = pd.DataFrame(result)
        df.to_csv('inventory50.csv', index=False, header=["MODEL", "SERIAL NUMBER", "CATEGORY",
                                                          "LOCATION", "STATUS", "DESCRIPTION", "DATE"])
        return True
    else:
        return False


def quit() -> None:
    """
        Quit the program

        :return: None
        :rtype: None

    """
    clear()
    print(Fore.GREEN + "Quiting...")
    time.sleep(2)
    sys.exit(Fore.RED + "Exited")


def clear() -> None:
    """
        Clears the screen for a better user experience

        :return: None
        :rtype: None

    """

    os.system('cls')


# main entry into the program
if __name__ == "__main__":
    main()
