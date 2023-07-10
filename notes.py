import time
import json

def add_note(title, text):
    try:
        with open("notes.json", "r", encoding='utf-8') as file:
            notes = json.load(file)

        if len(notes) == 0:
            id_note = 0
        else:
            id_note = len(notes)

        create_time = time.strftime("%H:%M | %d.%m.%Y", time.localtime())
        new_note = {'id': id_note, 'create': create_time, 'title': title, 'text': text, 'edit': None}
        notes.append(new_note)

        with open("notes.json", "w", encoding='utf-8') as file:
            json.dump(notes, file)
        print(f'Заметка с ID {id_note} создана!')

    except:
        print(f'Заметка не создана. Попробуйте снова!')

