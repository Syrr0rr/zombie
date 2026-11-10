import json
import os
from datetime import datetime

starting_stats = {
    "shelter_name": "Last Hope",
    "leader": "Alex",
    "survivors": 8,
    "food": 40,
    "water": 30,
    "barricade_health": 75,
    "radio_working": True
}

def get_int_within_range(num, min, max, message):
    '''gets valid int'''
    while True:
        try:
            num = int(num)
            if min <= num <= max:
                return num
        except ValueError:
            pass
        num = input(message)
   
def getvalid_int(num,message):
    '''gets valid int '''
    while not num.isdigit:
        num = input(message)
    return num

# --------------------------------------------

def load_folder(folder_location):
    """Load shelter data from JSON file"""
    with open(folder_location, "r", encoding="utf-8") as file:
        return json.load(file)

def save_shelter(data):
    """Save the shelter dictionary to JSON with indentation"""
    with open("shelter.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def reset_data():
    """Resets the file to starting stats"""
    with open("shelter.json", "w", encoding="utf-8") as file:
        json.dump(starting_stats, file, indent=4)

#--------------------

def view_changelog():
    data = load_folder("shelter_change_log.json")

    print("Field changed | Old value | New value | Date")
    print("-" * 90)

    for log in data:
        field_changed = log.get("field_changed", "not found")
        old_value = log.get("old_value", "not found")
        new_value = log.get("new_value", "not found")
        date = log.get("date", "not found")

        print(f"{field_changed} | {old_value} | {new_value} | {date}")

def view_shelterinfo():
    data = load_folder("shelter.json")
    shelter_name = data.get("shelter_name", "not found")
    leader = data.get("leader", "not found")
    survivors = data.get("survivors", "not found")
    food = data.get("food", "not found")
    water = data.get("water", "not found")
    barricade_health = data.get("barricade_health", "not found")
    radio_working = data.get("radio_working", "not found")
    print(f"""
    Shelter Name : {shelter_name}
    Leader : {leader}
    Survivors : {survivors}
    Food : {food}
    Water : {water}
    Barricade Health : {barricade_health}
    Radio Working? : {radio_working}""")

def log_shelter_change(field, old_value, new_value):
    '''Adds shelter changes to the change log'''
    try:
        with open("shelter_change_log.json", "r") as file:
            change_log = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        change_log = []
    change = {
        "field_changed": field,
        "old_value": old_value,
        "new_value": new_value,
        "date": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }
    change_log.append(change)
    with open("shelter_change_log.json", "w") as file:
        json.dump(change_log, file, indent=4)
   
#Change shelter value functions---------------------------------------------

def change_shelter_name(shelter_dict):
    new_name = input("Enter new shelter name: ")
    shelter_dict["shelter_name"] = new_name
    save_shelter(shelter_dict)

def change_leader(shelter_dict):
    new_leader = input("Enter new leader: ")
    shelter_dict["leader"] = new_leader
    save_shelter(shelter_dict)

def change_survivors(shelter_dict):
    new_survivors = input("Enter survivor count: ")
    new_survivors = getvalid_int(new_survivors, "Enter a valid number: ")
    shelter_dict["survivors"] = new_survivors
    save_shelter(shelter_dict)

def change_food(shelter_dict):
    new_food = input("Enter food amount: ")
    new_food = getvalid_int(new_food, "Enter a valid number: ")
    shelter_dict["food"] = new_food
    save_shelter(shelter_dict)

def change_water(shelter_dict):
    new_water = input("Enter water amount: ")
    new_water = getvalid_int(new_water, "Enter a valid number: ")
    shelter_dict["water"] = new_water
    save_shelter(shelter_dict)

def change_barricade_health(shelter_dict):
    new_health = input("Enter barricade health: ")
    new_health = getvalid_int(new_health, "Enter a valid number: ")
    shelter_dict["barricade_health"] = new_health
    save_shelter(shelter_dict)

def change_radio(shelter_dict):
    new_radio = input("Is the radio working? (yes/no): ").lower()
    if new_radio == "yes":
        shelter_dict["radio_working"] = True
        save_shelter(shelter_dict)
    elif new_radio == "no":
        shelter_dict["radio_working"] = False
        save_shelter(shelter_dict)
    else:
        print("Please enter yes or no.")

#---------------------------------------------------------------------------

def change_shelter_val():
    '''Changes shelter values and records changes'''
    shelter_dict = load_folder("shelter.json")
    options = {
        "1": ("shelter_name", change_shelter_name),
        "2": ("leader", change_leader),
        "3": ("survivors", change_survivors),
        "4": ("food", change_food),
        "5": ("water", change_water),
        "6": ("barricade_health", change_barricade_health),
        "7": ("radio_working", change_radio)
    }
    choice = input("Choose field to change (1-7): ")
    if choice not in options:
        print("Invalid choice.")
        return
    field, function = options[choice]
    old_value = shelter_dict[field]
    function(shelter_dict)
    new_value = shelter_dict[field]
    if old_value != new_value:
        log_shelter_change(field, old_value, new_value)

def view_changelog():
    data = load_folder("shelter_change_log.json")

    print("Field changed | Old value | New value | Date")
    print("-" * 90)

    for log in data:
        field_changed = log.get("field_changed", "not found")
        old_value = log.get("old_value", "not found")
        new_value = log.get("new_value", "not found")
        date = log.get("date", "not found")

        print(f"{field_changed} | {old_value} | {new_value} | {date}")

# Initialize JSON file if it doesn't exist or is empty
if not os.path.exists("shelter.json") or os.path.getsize("shelter.json") == 0:
    reset_data()

# Main program
def main_print():
    print("""
1. View shelter information
2. Change a shelter value
3. View change log
4. Quit
""")
while True:
    main_print()
    choice = input("Enter choice:")
    answer = get_int_within_range(choice,1,4,"Enter choice:")
    if answer == 1:
        view_shelterinfo()
    elif answer == 2:
        change_shelter_val()
    elif answer == 3:
        view_changelog()# add function to view the change log
    else:
        break