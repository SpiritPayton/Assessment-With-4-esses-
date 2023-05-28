"""version 3 of the add function made entirely by miya so-beer
"""
def add():
    new_monster_name = easygui.enterbox("Hey, baby sister! Enter the name of the new monster you wanna add:", "Add Monster")
    if new_monster_name:
        new_monster_stats = {}
        for stat in ["Strength", "Speed", "Stealth", "Cunning"]:
            new_value = easygui.enterbox(f"What {stat} do they have, chile? ", f"Add {stat}")
            if new_value:
                new_monster_stats[stat] = int(new_value)
        monster_dict[new_monster_name] = new_monster_stats
        easygui.msgbox(f"You did it, child! {new_monster_name} is now part of our Monster Card collection!")
    else:
        easygui.msgbox("What?!!?! Child, you didn't enter a name for the new monster.")

    print(new_monster_name, new_monster_stats)
