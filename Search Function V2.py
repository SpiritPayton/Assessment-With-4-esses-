"""This is the search function to search for existing monster cards on the catalogue
version 2 displays all available monster cards which the user can pick from
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

while True:
    option = easygui.buttonbox("Grrrrr! How can I help you with your Monster Card collection?",
                               "Monster Card Menu", choices=["Search", "Add", "Combos", "Explode"])
    # if they wanna search
    if option == "Search":
        # ask the user to select a monster to search for
        monster_choice = easygui.choicebox("What monster are you searching for?",
                                           "Monster Card Search", choices=monster_list)
        # if the user selects a monster, show its details
        if monster_choice:
            monster_details = monster_dict[monster_choice]
            details_str = "\n".join([f"{k}: {v}" for k, v in monster_details.items()])
            easygui.msgbox(details_str)
            #
        if details:
            monster_name = details[0]
            monster_details = details[1]
            details_str = "\n".join([f"{k}: {v}" for k, v in monster_details.items()])
            easygui.msgbox(details_str, title=monster_name)
