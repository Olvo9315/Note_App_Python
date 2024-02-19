import datetime

class Note:
    def __init__(self, title, body):
        self.note_id = None  # инициализируем note_id как None
        self.title = title
        self.body = body
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def update(self, title, body):
        self.title = title
        self.body = body
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        created_at_str = self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        updated_at_str = self.updated_at.strftime("%Y-%m-%d %H:%M:%S")
        return f" Id: {self.note_id} \nTitle: {self.title} \nBody: {self.body} \nCreated at: {created_at_str} \nUpdated at: {updated_at_str} \n----------"

    
    def to_file_format(self):
        created_at_str = self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        updated_at_str = self.updated_at.strftime("%Y-%m-%d %H:%M:%S")
        return f"{self.note_id};{self.title};{self.body};{created_at_str};{updated_at_str}"

    @staticmethod
    def from_string(s):
        note_id, title, body, created_at, updated_at = s.split(';')
        created_at = datetime.datetime.strptime(created_at, '%Y-%m-%d %H:%M:%S')
        updated_at = datetime.datetime.strptime(updated_at, '%Y-%m-%d %H:%M:%S')
        note = Note(title, body)
        note.note_id = note_id
        note.created_at = created_at
        note.updated_at = updated_at
        return note