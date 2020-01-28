class PriorityQueue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def is_empty(self):
        return len(self.queue) == []

    def insert(self, rubik):
        self.queue.append(rubik)

    def delete(self):
        try:
            min = 0
            if len(self.queue) != 0:
                for i in range(len(self.queue)):
                    if self.queue[i].path_cost < self.queue[min].path_cost:
                        min = i
                item = self.queue[min]
                del self.queue[min]
                return item
        except IndexError:
            print()
            exit()