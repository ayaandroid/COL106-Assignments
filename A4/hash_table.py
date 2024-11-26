from prime_generator import get_next_size

def p(x):
    if x.islower():
        return ord(x)-97
    elif x.isupper():
        return ord(x)-39
    return ord(x)

def polyhash_factory(z, mod):
    def polyhash(s):
        val = 0
        for i in range(len(s)-1,-1,-1):
            val = (val*z + p(s[i])) % mod
        return val
    return polyhash

class HashTable:
    def __init__(self, collision_type, params):
        '''
        Possible collision_type:
            "Chain"     : Use hashing with chaining
            "Linear"    : Use hashing with linear probing
            "Double"    : Use double hashing
        '''

        if collision_type == "Double":
            z1, z2, c2, table_size = params
            self.hash1 = polyhash_factory(z1, table_size)
            f = polyhash_factory(z2, c2)
            self.hash2 = lambda s: c2 - f(s)
        else:
            z, table_size = params
            self.hash = polyhash_factory(z, table_size)

        self.table = [None]*table_size
        self.num_elements = 0

        self.collision_type = collision_type
        self.params = params
    
    def insert(self, x):
        pass
    
    def find(self, key):
        pass
    
    def get_slot(self, key):
        if self.collision_type == "Double":
            return self.hash1(key)
        return self.hash(key)

    def get_load(self):
        return self.num_elements/len(self.table)
    
    def __str__(self):
        pass
    
    def __iter__(self):
        if self.collision_type == "Chain":
            for x in self.table:
                if x is not None:
                    for y in x:
                        yield y
        else:
            for x in self.table:
                if x is not None:
                    yield x

    # TO BE USED IN PART 2 (DYNAMIC HASH TABLE)
    def rehash(self):
        pass
    
# IMPLEMENT ALL FUNCTIONS FOR CLASSES BELOW
# IF YOU HAVE IMPLEMENTED A FUNCTION IN HashTable ITSELF, 
# YOU WOULD NOT NEED TO WRITE IT TWICE
    
class HashSet(HashTable):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
    
    def insert(self, key): 
        
        i = self.get_slot(key)

        if self.collision_type == "Chain":
            if self.table[i] is None:
                self.table[i] = []
            for j in range(len(self.table[i])):
                if self.table[i][j] == key:
                    return
            self.table[i].append(key)
            self.num_elements += 1
            return
        elif self.collision_type == "Linear":
            step = 1
        else:
            step = self.hash2(key)
        
        n = len(self.table)
        num_probes = 0
        while num_probes < n:
            if self.table[i] is None:
                self.table[i] = key
                self.num_elements += 1
                return
            elif self.table[i] == key:
                return
            i = (i + step) % n
            num_probes += 1
        
        raise Exception("HashTable is full")
    
    def find(self, key):

        i = self.get_slot(key)

        if self.collision_type == "Chain":
            if self.table[i] is None:
                return False
            return key in self.table[i]
        elif self.collision_type == "Linear":
            step = 1
        else:
            step = self.hash2(key)
        
        n = len(self.table)
        num_probes = 0
        while num_probes < n:
            if self.table[i] is None:
                return False
            if self.table[i] == key:
                return True
            i = (i + step) % n
            num_probes += 1

        return False

    def get_slot(self, key):
        return super().get_slot(key)
    
    def get_load(self):
        return super().get_load()
    
    def __str__(self):
        result = []

        if self.collision_type == "Chain":
            for x in self.table:
                if x is None:
                    result.append('<EMPTY>')
                else:
                    result.append(' ; '.join(x))
        else:
            for x in self.table:
                if x is None:
                    result.append('<EMPTY>')
                else:
                    result.append(x)

        return ' | '.join(result)
    
class HashMap(HashTable):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
    
    def insert(self, x):
        # x = (key, value)

        key = x[0]

        i = self.get_slot(key)

        if self.collision_type == "Chain":
            if self.table[i] is None:
                self.table[i] = []
            for j in range(len(self.table[i])):
                if self.table[i][j][0] == key:
                    old_value = self.table[i][j][1]
                    self.table[i][j] = x
                    return old_value
            self.table[i].append(x)
            self.num_elements += 1
            return
        elif self.collision_type == "Linear":
            step = 1
        else:
            step = self.hash2(key)
        
        n = len(self.table)
        num_probes = 0
        while num_probes < n:
            if self.table[i] is None:
                self.table[i] = x
                self.num_elements += 1
                return
            elif self.table[i][0] == key:
                old_value = self.table[i][1]
                self.table[i] = x
                return old_value
            i = (i + step) % n
            num_probes += 1
        
        raise Exception("HashTable is full")
    
    def find(self, key):
        i = self.get_slot(key)

        if self.collision_type == "Chain":
            if self.table[i] is None:
                return None
            for x in self.table[i]:
                if x[0] == key:
                    return x[1]
            return None
        elif self.collision_type == "Linear":
            step = 1
        else:
            step = self.hash2(key)
        
        n = len(self.table)
        num_probes = 0
        while num_probes < n:
            if self.table[i] is None:
                return None
            if self.table[i][0] == key:
                return self.table[i][1]
            i = (i + step) % n
            num_probes += 1

        return None
    
    def get_slot(self, key):
        return super().get_slot(key)
    
    def get_load(self):
        return super().get_load()
    
    def __str__(self):
        result = []

        if self.collision_type == "Chain":
            for x in self.table:
                if x is None:
                    result.append('<EMPTY>')
                else:
                    result.append(' ; '.join([f'({y[0]}, {y[1]})' for y in x]))
        else:
            for x in self.table:
                if x is None:
                    result.append('<EMPTY>')
                else:
                    result.append(f'({x[0]}, {x[1]})')

        return ' | '.join(result)

mp = HashMap("Linear", (2, 5))
mp.insert(('Ayaan', [1,2]))
print(mp)