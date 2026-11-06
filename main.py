import json
start_data = { 
        "shelter_name": "Last Hope", 
        "leader": "Alex", 
        "survivors": 8, 
        "food": 40, 
        "water": 30, 
        "barricade_health": 75, 
        "radio_working": True 
    }


#--------------------------------------------
def load_shelter():
    """Load shelter data from JSON file"""
    with open("shelter.json", "r", encoding="utf-8") as file:
        return json.load(file)

def save_shelter(data):
    """Save the shelter dictionary to JSON with indentation"""
    with open("shelter.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
#---------------------------------------------

def start_data(): #resets the file to starting stats
    with open("shelter.json", "w") as file: #NOTE add try code and error handling
        json.dump(start_data,file,indent=4)
def view_shelterinfo():
    with open("shelter.json", "r") as file:
        data = json.load(file)
        shelter_name = data.get("shelter_name", "not found")
        leader = data.get("leader", "not found")
        survivors = data.get("survivors", "not found")
        food = data.get("food", "not found")
        water = data.get("water", "not found")
        barricade_health = data.get("barricade_health", "not found")
        radio_working = data.get("radio_working", "not found")
        print(
        f"""
Shelter Name : {shelter_name}
Leader : {leader}
Survivors : {survivors}
Food : {food}
Water : {water}
Barricade Health : {barricade_health}
Radio Working? : {radio_working}""")
    
def change_shelter_val():
    #make sure is vaild 
    user_choice_change = input("""Choose feild to change:
1. Shelter Name
2. Leader
3. Survivors
4. Food
5. Water
6. Barricade health
7. Radio Working """) 
    if user_choice_change == 1: #change name 
        pass
    elif user_choice_change == 2: #leader
        pass
    elif user_choice_change == 3: #survivors
        pass
    elif user_choice_change == 4: #food
        pass
    elif user_choice_change == 5: #water
        pass
    elif user_choice_change == 6: #barricade health
        pass
    elif user_choice_change == 7: #radio working status
        pass
    
def view_changelog():
    pass
view_shelterinfo()

change_shelter_val()

with open("shelter.json", "r") as file:
    shelter_dict = load_shelter()
    shelter_dict["shelter_name"] = "lala"
    save_shelter(shelter_dict)
    print("done")