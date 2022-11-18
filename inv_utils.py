from datetime import date
from colorama import Fore


class Inventory:
    def __init__(self, model, serial_number, category, location, status, description,  date) -> None:
        self.model = model
        self.serial_number = serial_number
        self.category = category
        self.location = location
        self.status = status
        self.description = description
        self.date = date


def get_date(prompt: str) -> str:
    while True:
        d = input(prompt)
        if verify_date(d):
            return d
        else:
            continue


def verify_date(d: str) -> str:
    try:
        y, m, d = d.split("-")
        date_of_birth = date(int(y), int(m), int(d))
        return str(date_of_birth)
    except:
        try:
            y, m, d = d.split("/")
            date_of_birth = date(int(y), int(m), int(d))
            return str(date_of_birth)
        except:
            try:
                y, m, d = d.split(".")
                date_of_birth = date(int(y), int(m), int(d))
                return str(date_of_birth)
            except:
                return ""


def get_status() -> str:
    while True:
        print(Fore.GREEN + "1️⃣  Deployed and Working\n2️⃣  Not Deplopyed But Working\n3️⃣  Not Working\n4️⃣  Under Repair\n")
        try:
            user_choice = int(input("Select Status: "))
            if ch := verify_status(user_choice):
                return str(ch)
            else:
                continue
        except ValueError:
            pass


def verify_status(n: int) -> str:
    status = {
        1: "Deployed and Working",
        2: "Not Deplopyed But Working",
        3: "Not Working",
        4: "Under Repair",
    }
    return status.get(n, "")


def get_category() -> str:
    while True:
        print(Fore.GREEN + "1️⃣  CPU\n2️⃣  Monitor\n3️⃣  Peripheral\n4️⃣  Laptop\n")
        try:
            user_choice = int(input("Select Category: "))
            if ch := verify_category(user_choice):
                return str(ch)
            else:
                continue
        except ValueError:
            pass


def verify_category(n: int) -> str:
    category = {
        1: "CPU",
        2: "Monitor",
        3: "Peripheral",
        4: "Laptop",
    }
    return category.get(n, "")
