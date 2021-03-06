import datetime

last_id = 0
class Note():
    """Creates a note in notebook, provides a function of searching for note by tags or note name
    Also every note has its own id"""
    def __init__(self, memo, tags=''):
        """makes a note with its datetime and unique id"""
        self.date = datetime.date.today()
        self.memo = memo
        self.tags = tags
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        """Searches for matches in tags and notes"""
        return filter in self.tags or filter in self.memo


class Notebook():
    def __init__(self):
        self.notes = []

    def new_note(self, memo, tags=''):
        self.notes.append(Note(memo, tags))

    def _find_note(self, id):
        """Searches for note with given id"""
        for note in self.notes:
            if note.id == id:
                return note
        return None

    def modify_memo(self, id, new_memo):
        """Modifies memo to the given one"""
        self._find_note(id).memo = new_memo

    def modify_tags(self, id, new_tag):
        """Finds the note with given id and changes its tag to given value"""
        for note in self.notes:
            if note.id == id:
                note.memo = new_tag

    def search(self, filter):
        """Searches for notes with given value"""
        return [note for note in self.notes if note.match(filter)]

f = Notebook()
f.new_note('how are you')
f.new_note('im fine')
f.modify_memo(1, 'im bad')
print(f.search('e'))
print(f.notes[0].memo)