class MyHashSet:

    def __init__(self):
        self.storage = [None] * 1000000
        

    def add(self, key: int) -> None:
        self.storage[key] = key
        

    def remove(self, key: int) -> None:
        self.storage[key] = None

    def contains(self, key: int) -> bool:
        return self.storage[key] is not None
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
