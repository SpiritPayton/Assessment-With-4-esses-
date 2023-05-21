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

    # if they wanna add
elif option == "Add":
    # create a MonsterCard object and call its add method to add a new monster
        monster = MonsterCard("", {}).add()

    # if they wanna explode
    elif option == "Explode":
        easygui.msgbox("Boom! The Monster Card collection exploded. Game over!")
        break
# This completes the code, adding the functionality for the "Add" option.
# The user will be prompted to enter the name and stats of a new monster,
# which will then be added to the monster_dict dictionary.





