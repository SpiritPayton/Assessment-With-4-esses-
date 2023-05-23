"""The basics of the Monster Card program without the functions
"""

import easygui


monster_dict = {
    "Stoneling": {"Strength": 7, "Speed": 1, "Stealth": 25, "Cunning": 15},
    "Vexscream": {"Strength": 1, "Speed": 6, "Stealth": 21, "Cunning": 19},
    "Dawnmirage": {"Strength": 5, "Speed": 15, "Stealth": 18, "Cunning": 22},
    "Blazegolem": {"Strength": 15, "Speed": 20, "Stealth": 23, "Cunning": 6},
    "Websnake": {"Strength": 7, "Speed": 15, "Stealth": 10, "Cunning": 5},
    "Moldvine": {"Strength": 21, "Speed": 18, "Stealth": 14, "Cunning": 5},
    "Vortexwing": {"Strength": 19, "Speed": 13, "Stealth": 19, "Cunning": 2},
    "Rotthing": {"Strength": 16, "Speed": 7, "Stealth": 4, "Cunning": 12},
    "Froststep": {"Strength": 14, "Speed": 14, "Stealth": 17, "Cunning": 4},
    "Wispghoul": {"Strength": 17, "Speed": 19, "Stealth": 3, "Cunning": 2}
}

monster_list = list(monster_dict.keys())

# chile
class MonsterCard:
    def __init__(self, name, stats):
        self.name = name
        self.stats = stats

    def __str__(self):
        return f"{self.name}: {self.stats}"

    def search(self):
        search_term = easygui.enterbox("What monster are you searching for?", "Search")
        if search_term:
            matches = [monster for monster in monster_list if search_term.lower() in monster.lower()]
            if matches:
                selected_monster = easygui.choicebox("Select a monster:", "Search Results", matches)
                if selected_monster:
                    monster_details = monster_dict[selected_monster]
                    return selected_monster, monster_details
                else:
                    easygui.msgbox("No monster selected.")
            else:
                easygui.msgbox(f"No matches found for '{search_term}'.")

    def edit(self):
        edit_monster = easygui.choicebox("Select a monster to edit:", "Edit", monster_list)
        if edit_monster:
            new_stats = {}
            for stat in monster_dict[edit_monster]:
                new_value = easygui.enterbox(f"Enter new value for {stat}: ", f"Edit {stat}")
                if new_value:
                    new_stats[stat] = int(new_value)
            monster_dict[edit_monster].update(new_stats)
            easygui.msgbox("Monster details updated!")
        else:
            easygui.msgbox("No monster selected for editing.")

    def add(self):
        new_monster_name = easygui.enterbox("Enter the name of the new monster:", "Add Monster")
        if new_monster_name:
            new_monster_stats = {}
            for stat in ["Strength", "Speed", "Stealth", "Cunning"]:
                new_value = easygui.enterbox(f"Enter the value for {stat}: ", f"Add {stat}")
                if new_value:
                    new_monster_stats[stat] = int(new_value)
            monster_dict[new_monster_name] = new_monster_stats
            easygui.msgbox(f"Successfully added {new_monster_name} to the Monster Card collection!")

        else:
            easygui.msgbox("No name entered for the new monster.")


while True:
    option = easygui.buttonbox("Grrrrr! How can I help you with your Monster Card collection?",
                               "Monster Card Menu", choices=["Search", "Edit", "Add", "Explode"])
    # if they wanna search
    if option == "Search":
        # create a MonsterCard object and call its search method to find a monster
        monster = MonsterCard("", {}).search()
        # if a monster is found, show its details
        if monster:
            monster_name, monster_details = monster
            details_str = "\n".join([f"{k}: {v}" for k, v in monster_details.items()])
            easygui.msgbox(details_str, title=monster_name)

    # if they wanna edit
    elif option == "Edit":
        # create a MonsterCard object and call its edit method to modify a monster
        monster = MonsterCard("", {}).edit()

    # i'll add code for "Add" and "Explode" options
    # if they wanna add
    elif option == "Add":
        # create a MonsterCard object and call its add method to add a new monster
        monster = MonsterCard("", {}).add()

    # if they wanna explode
    elif option == "Explode":
        easygui.msgbox("Boom! The Monster Card collection exploded. Game over!")
        break

    # if they wanna quit
    else:
        break
