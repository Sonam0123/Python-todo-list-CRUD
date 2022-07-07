from tinydb import TinyDB, Query

db = TinyDB('db.json')
search = Query()

class Task:
    def __init__(self):
        pass

    def create(self, todo):
        db.insert({'task': todo, 'completed': False})
        print(db.all())

    def search(self, todo):   
        db.search(search.task == todo)

    def read(self, todo):
        print(db.all())

    def update(self, todo):
        db.update({'completed': True, 'task': todo})
        print(db.all())

    def delete(self, todo):
        db.remove(search.task == todo)
        print(db.all())
       
# Task().read('')
Task().create('something')
# Task().search('something')
# Task().update('something')
# Task().delete('something')