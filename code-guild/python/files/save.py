import json


class Todo(object):
    def __init__(self):
        self.templist = []

    def _set(self, *tasks):
        for task in tasks:
            self.templist.append(task)
        persistence = Storage()
        return persistence.save(self.templist)

    def _get(self):
        persistence = Storage()
        return persistence.load()


class Storage(object):
    def save(self, list_of_tasks):
        with open("/home/student/data.json", "w") as out_file:
            json.dump(list_of_tasks, out_file)

    def load(self):
        with open("/home/student/data.json", "r") as in_file:
            todo = json.load(in_file)
            print(todo)


my_task = Todo()
my_task._set(1,2,3,4)
my_task._get()
