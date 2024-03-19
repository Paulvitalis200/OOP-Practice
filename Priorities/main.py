from collections import deque
import random
from datetime import datetime

class Priority:
    def __init__(self, title, weight):
        self.id = random.randint(0, 999999999999)
        self.title = title
        self.weight = weight
        self.completed = False
        self.date_completed = None


class Priorities:
    def __init__(self):
        self.items = deque()

    def push(self, title, weight):
        priority = {
            'id' : random.randint(0, 999999999999),
            'title' : title,
            'weight' : weight,
            'completed' :False,
            'date_completed' : None
        }

        if weight == 1:
            self.items.appendleft(priority)
        else:
            self.items.append(priority)

    def get_items(self):
        return self.items
    
    def get_total_completed(self):
        completed = 0

        for i in range(len(self.items)):
            if self.items[i]['completed'] == True:
                completed += 1

        return str((completed / len(self.items)) * 100) + '%'
    
    def get_total_completed_by_priority(self, priority):
        completed = 0

        priority_length = 0
        for i in range(len(self.items)):
            if self.items[i]['weight'] == priority:
                priority_length += 1
        for i in range(len(self.items)):
            if self.items[i]['completed'] == True and self.items[i]['weight'] == priority:
            
                completed += 1

        return str((completed / priority_length) * 100) + '%'
    
    def complete_task(self, task):
        for i in range(len(self.items)):
            if task.lower() == self.items[i]['title'].lower():
                now = datetime.now()
                self.items[i]['completed'] = True
                self.items[i]['date_completed'] = now.strftime("%d/%m/%Y %H:%M:%S")

    

    
priorities = Priorities()
priorities.push("Buy car", 4)
priorities.push("Buy sneakers", 2)
priorities.push("Have emergency fund", 1)
priorities.push("Generate lots and lots of income", 1)
priorities.push("Buy Macbook", 1)
priorities.push("Buy Smartphone", 1)

priorities.complete_task('buy sneakers')
priorities.complete_task('Generate lots and lots of income')
priorities.complete_task('buy macbook')
priorities.complete_task('buy smartphone')
priorities.complete_task('have emergency fund')
print(priorities.get_items())
print("\n")
print("=========================")
print("\n")
print("Total completed: ", priorities.get_total_completed())
priority = 2
print("Priority {i} completed: ".format(i=priority), priorities.get_total_completed_by_priority(priority))