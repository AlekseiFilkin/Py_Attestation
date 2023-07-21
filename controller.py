import function as func
import ui


def run():
    userChoice = ''
    while userChoice != '7':
        ui.menu()
        userChoice = input().strip()
        if userChoice == '1':
            func.showNote('all')
        if userChoice == '2':
            func.addNote()
        if userChoice == '3':
            func.showNote('all')
            func.refactorNote('del')
        if userChoice == '4':
            func.showNote('all')
            func.refactorNote('edit')
        if userChoice == '5':
            func.showNote('date')
        if userChoice == '6':
            func.showNote('id')
            func.refactorNote('showNote')
        if userChoice == '7':
            ui.close()
            break