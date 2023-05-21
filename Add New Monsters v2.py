def add(self):
    new_monster_name = easygui.enterbox("Enter the name of the new monster:", "Add")
    if new_monster_name:
        new_monster_stats = {}
        for stat in MonsterCard.stats:
            new_value = easygui.enterbox(f"Enter the value for {stat}: ", f"Add {stat}")
            if new_value:
                new_monster_stats[stat] = int(new_value)

        new_monster = MonsterCard(new_monster_name, new_monster_stats)
        monster_dict[new_monster.name] = new_monster.stats
        easygui.msgbox(f"Successfully added {new_monster.name} to the Monster Card collection!")
    else:
        easygui.msgbox("No name entered for the new monster.")
