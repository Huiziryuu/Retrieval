__author__ = 'liuhui'

# HashTable class
class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.value = [None] * self.size

    # hash function to produce hashvalue
    def hashfunction(self, key, size):
        return key % size

    # rehash function to solve the collision
    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    # put function: insert key-data pairs
    def put(self, key, data):
        # get hashvalue
        hashvalue = self.hashfunction(key, self.size)

        # if the slot is not occupied
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.value[hashvalue] = data
        # in case the target slot is not empty
        else:
            # it the key value is the same
            if self.slots[hashvalue] == key:
                self.value[hashvalue] = data # replace the existing value
            # rehash to look for next empty slot
            else:
                nextslot = self.rehash(hashvalue,self.size)
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot,self.size)

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.value[nextslot] = data
                else:
                    self.value[nextslot] = data # replace


    # get function:
    def get(self,key):
        startslot = self.hashfunction(key, self.size)

        data = None
        stop = False
        found = False

        postion = startslot

        while self.slots[postion] != None and \
                not found and not stop:
            if self.slots[postion] == key:
                found = True
                data = self.value[postion]
            else:
                postion = self.rehash(postion,self.size)
                if postion == startslot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        return self.put(key, value)


# for testing
H = HashTable()
H[54] = "cat"
H[26] = "dog"
H[93] = "lion"
H[17] = "tiger"
H[77] = "bird"
H[31] = "cow"
H[44] = "goat"
H[55] = "pig"
H[20] = "chicken"

print(H.slots)
print(H.value)
print(H[20])
H[20] = "duck"
print(H[20])
print(H[99])

