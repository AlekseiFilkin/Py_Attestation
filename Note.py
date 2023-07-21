from datetime import datetime
import uuid


class Note:
    def __init__(self, id = str(uuid.uuid1())[0:3],  title = "текст", body = "текст", date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))):
        self.id = id
        self.title = title
        self.body = body
        self.date = date

    def getId(note):
        return note.id

    def getTitle(note):
        return note.title

    def getBody(note):
        return note.body

    def getDate(note):
        return note.date

    def setId(note):
        note.id = str(uuid.uuid1())[0:3]

    def setTiitle(note, title):
        note.title = title

    def setBody(note, body):
        note.body = body

    def setDate(note):
        note.date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

    def toString(note):
        return note.id + ';' + note.title + ';' + note.body + ';' + note.date

    def mapNote(note):
        return '\nID: ' + note.id + '\n' + 'Название: ' + note.title + '\n' + 'Описание: ' + note.body + '\n' + 'Дата публикации: ' + note.date