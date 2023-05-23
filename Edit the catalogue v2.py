"""Version 2 of the Edit the catalogue function
for the Monster Card game
"""

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

# chile
