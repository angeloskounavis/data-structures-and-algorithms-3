from data_structures.queue import Queue
from data_structures.linked_list import TargetError


class AnimalShelter(Queue):
    def __init__(self):
        super().__init__()

    def dequeue(self, pref):
        if str(self.front.value) == pref:
            return super().dequeue()
        else:
            prev = None
            current = self.front
            while current:
                if str(current.value) == pref:
                    prev.next = current.next
                    return current.value
                else:
                    prev = current
                    current = current.next
            raise TargetError(f"There are no {pref}'s. Come back another time.")


class Dog:
    def __str__(self):
        return 'dog'


class Cat:
    def __str__(self):
        return 'cat'


shelter = AnimalShelter()
cat = Cat()
dog = Dog()
shelter.enqueue(cat)
shelter.enqueue(dog)
actual = shelter.dequeue("dog")
expected = dog

print(actual)
print(expected)
