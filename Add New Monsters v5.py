"""more aave terms
made entirely by miya so-beer
"""
def add():
    new_monster_name = easygui.enterbox("Hey, baby sister! Tell me the name of the new monster, what he did, chile:", "Add Monster, Auntie Heigui Style")
    if new_monster_name:
        new_monster_stats = {}
        for stat in ["Strength", "Speed", "Stealth", "Cunning"]:
            new_value = easygui.enterbox(f"What {stat} he got, chile? Tell Auntie Heigui:", f"Add {stat}, Baby We Ain't Got Tyne!!!")
            if new_value:
                new_monster_stats[stat] = int(new_value)
        monster_dict[new_monster_name] = new_monster_stats
        easygui.msgbox(f"Chile, Auntie Heigui proud of you! {new_monster_name} now part of our Monster Card collection!")
    else:
        easygui.msgbox("What?!!?! Baby, you never tell Auntie Heigui the name of the new monster lah.")

    print(new_monster_name, new_monster_stats)
