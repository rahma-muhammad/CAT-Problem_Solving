class RecentCounter:
    queue =[]

    def __init__(self):
        return None
    
    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue[0] < t - 3000:
            self.queue.pop(0)
        return len(self.queue) #can't use list comprehension due to restrictions

t = RecentCounter()
print(t.ping(1178))
print(t.ping(1483))
print(t.ping(1563))
print(t.ping(4054))
print(t.ping(4152))