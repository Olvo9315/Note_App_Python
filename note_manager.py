import json
import collections
from note import Note

class NoteManager:
    def __init__(self, filename):
        self.filename = filename
        self.notes = self._read_notes()

    def _read_notes(self):
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                return [Note.from_string(note_str) for note_str in data]
        except FileNotFoundError:
            print("No notes found.")
            return []
        except json.JSONDecodeError:
            print("Error decoding JSON. Notes file might be corrupted.")
            return []

    def add_note(self, note):
        if self.notes:
            last_note_id = int(self.notes[-1].note_id)
        else:
            last_note_id = 0
        note.note_id = str(last_note_id + 1)
        self.notes.append(note)
        self.save_notes()

    def note_exists(self, note_id):
        return any(note.note_id == note_id for note in self.notes)

    def delete_note_by_id(self, note_id):
        if not self.note_exists(note_id):
            print("Note with the given ID does not exist. Please enter a valid ID.")
            return

        self.notes = collections.deque(self.notes)
        for i, note in enumerate(self.notes):
            if note.note_id == note_id:
                self.notes.remove(note)
                print("Note deleted successfully.")
                break
        self.save_notes()

    def update_note_by_id(self, note_id, title, body):
        if not self.note_exists(note_id):
            print("Note with the given ID does not exist. Please enter a valid ID.")
            return
        
        for note in self.notes:
            if note.note_id == note_id:
                if title.strip() and body.strip():
                    note.update(title, body)
                    print("Note updated successfully.")
                else:
                    print("Title and body cannot be empty. Note not updated.")
                break
        self.save_notes()

    def filter_notes_by_date(self):
        return sorted(self.notes, key=lambda x: x.created_at, reverse=True)

    def get_note_by_id(self, note_id):
        for note in self.notes:
            if note.note_id == note_id:
                return note
        return None

    def save_notes(self):
        data = [note.to_file_format() for note in self.notes]
        try:
            with open(self.filename, 'w') as f:
                json.dump(data, f)
        except Exception as e:
            print(f"Error saving notes: {e}")