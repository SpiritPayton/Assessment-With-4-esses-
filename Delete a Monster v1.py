def delete():
    delete_monster = easygui.choicebox("Select a monster to ELIMINATE:", "Delete", monster_list)
    if delete_monster:
        monster_dict.pop(delete_monster)
        easygui.msgbox(f"Baby what?!?!?! you eliminated that ho i know that's right baby chile we ain't got tyne...")
    else:
        easygui.msgbox("What?!!?! Baby, you never tell Auntie Heigui the name of the monster "
                       "Auntie will assassinate lah.")
