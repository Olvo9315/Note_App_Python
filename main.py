from note import Note
from note_manager import NoteManager

def print_menu():
    print("1. Read notes")
    print("2. Get note by Id")
    print("3. Add note")
    print("4. Update note")
    print("5. Delete note")
    print("6. Exit")

def read_note_input():
    title = input("Enter title: ")
    body = input("Enter body: ")
    return title, body

def read_note_update():
    id = input("Enter Id: ")
    title = input("Enter title: ")
    body = input("Enter body: ")
    return id, title, body

def main():
    note_manager = NoteManager("notes.json")

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            sort_date = input("Enter 'Y' to sort notes by date ('N' or leave blank to display notes by ID)")
            if sort_date.upper() == 'Y':
                notes = note_manager.filter_notes_by_date()
            else: notes = note_manager.notes
            for note in notes:
                print(note)
        elif choice == "2":
            note_id = input("Enter note ID to get: ")
            note = note_manager.get_note_by_id(note_id)
            if note:
                print(note)
            else:
                print("Note with the given ID does not exist.")
        elif choice == "3":
            title, body = read_note_input()
            note = Note(title, body)
            note_manager.add_note(note)
        elif choice == "4":
            note_id, title, body = read_note_update()
            note_manager.update_note_by_id(note_id, title, body)
        elif choice == "5":
            note_id = input("Enter note ID to delete: ")
            note_manager.delete_note_by_id(note_id)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
