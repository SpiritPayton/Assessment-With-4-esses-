"""Final version of the Monster Card Catalogue program
allows the user to search, add, edit, and delete monsters.
upon 'exploding' the program,
exits and prints the updated monster catalogue
to the python console for printing
made by miya so-beer for patrick baker
"""

import easygui

# dictionary to store monster details
monster_dict = {
    "Stoneling": {"Strength": 7, "Speed": 1, "Stealth": 25, "Cunning": 15},
    "Vexscream": {"Strength": 1, "Speed": 6, "Stealth": 21, "Cunning": 19},
    "Dawnmirage": {"Strength": 5, "Speed": 15, "Stealth": 18, "Cunning": 22},
    "Blazegolem": {"Strength": 15, "Speed": 20, "Stealth": 23, "Cunning": 6},
    "Websnake": {"Strength": 7, "Speed": 15, "Stealth": 10, "Cunning": 5},
    "Moldvine": {"Strength": 21, "Speed": 18, "Stealth": 14, "Cunning": 5},
    "Vortexwing": {"Strength": 19, "Speed": 13, "Stealth": 19, "Cunning": 2},
    "Rotthing": {"Strength": 16, "Speed": 7, "Stealth": 4, "Cunning": 12},
    "Froststep": {"Strength": 17, "Speed": 19, "Stealth": 3, "Cunning": 2}
}

# list of monsters
monster_list = list(monster_dict.keys())


def search():
    # Function to search for a specific monster
    search_term = easygui.enterbox("What monster are you searching for?", "Search")
    if search_term:
        # Find matches based on the search term
        matches = [monster for monster in monster_list if search_term.lower() in monster.lower()]
        if matches:
            # Let the user select a monster from the matches
            selected_monster = easygui.choicebox("Select a monster:", "Search Results", matches)
            if selected_monster:
                # Retrieve and display the details of the selected monster
                monster_details = monster_dict[selected_monster]
                return selected_monster, monster_details
            else:
                easygui.msgbox("No monster selected.")
        else:
            easygui.msgbox(f"No matches found for '{search_term}'.")


def edit():
    # Function to edit the details of a monster
    edit_monster = easygui.choicebox("Select a monster to edit:", "Edit", monster_list)
    if edit_monster:
        new_stats = {}
        for stat in monster_dict[edit_monster]:
            # Prompt the user to enter new values for each stat
            new_value = easygui.enterbox(f"Enter new value for {stat}: ", f"Edit {stat}")
            if new_value:
                new_stats[stat] = int(new_value)
        # Update the monster's details with the new values
        monster_dict[edit_monster].update(new_stats)
        easygui.msgbox("Monster details updated!")
    else:
        easygui.msgbox("No monster selected for editing.")


def add():
    # Function to add a new monster to the collection
    new_monster_name = easygui.enterbox("Hey, baby sister! Tell me the name of the new monster,"
                                        " what he did, chile:", "Add Monster, Auntie Heigui Style")
    if new_monster_name:
        new_monster_stats = {}
        for stat in ["Strength", "Speed", "Stealth", "Cunning"]:
            # Prompt the user to enter values for each stat
            new_value = easygui.enterbox(f"What {stat} he got, chile? Tell Auntie Heigui:",
                                         f"Add {stat}, Baby We Ain't Got Tyne!!!")
            if new_value:
                new_monster_stats[stat] = int(new_value)
        # Add the new monster and its details to the collection
        monster_dict[new_monster_name] = new_monster_stats
        easygui.msgbox(f"Chile, Auntie Heigui proud of you! "
                       f"{new_monster_name} now part of our Monster Card collection!")
    else:
        easygui.msgbox("What?!!?! "
                       "Baby, you never tell Auntie Heigui the name of the new monster lah.")


def delete():
    # Function to delete a monster from the collection
    delete_monster = easygui.choicebox("Select a monster to ELIMINATE:", "Delete", monster_list)
    if delete_monster:
        # Remove the selected monster from the collection
        monster_dict.pop(delete_monster)
        easygui.msgbox(f"Baby what?!?!?! you eliminated that monsta "
                       f"i know that's right baby chile we ain't got tyne...")
    else:
        easygui.msgbox("What?!!?! Baby, you never tell Auntie Heigui"
                       " the name of the monster Auntie will assassinate lah.")


def explode():
    # Function to end the program and print the monster dictionary
    print("Monster Dictionary:")
    for monster, details in monster_dict.items():
        details_str = "\n".join([f"{k}: {v}" for k, v in details.items()])
        print(f"- {monster}:")
        print(details_str)
        print("")
    easygui.msgbox("Boom! The Monster Card collection exploded. Game over! Ur trash. 你没有朋友。")
    raise SystemExit


while True:
    # Main menu loop
    option = easygui.buttonbox("Grrrrr! How can I help you with your Monster Card collection?",
                               "Monster Card Menu", choices=["Search", "Edit", "Add", "Delete", "Explode"])

    if option == "Search":
        monster = search()
        if monster:
            monster_name, monster_details = monster
            details_str = "\n".join([f"{k}: {v}" for k, v in monster_details.items()])
            easygui.msgbox(details_str, title=monster_name)

    elif option == "Edit":
        edit()

    elif option == "Add":
        add()

    elif option == "Explode":
        explode()

    elif option == "Delete":
        delete()

    else:
        break
