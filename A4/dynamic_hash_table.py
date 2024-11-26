from hash_table import HashSet, HashMap
from prime_generator import get_next_size

class DynamicHashSet(HashSet):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        
    def rehash(self):
        # IMPLEMENT THIS FUNCTION
        new_table_size = get_next_size()
        while self.num_elements/new_table_size >= 0.5:
            new_table_size = get_next_size()
        new_params = self.params[:-1] + (new_table_size,)
        new = DynamicHashSet(self.collision_type, new_params)
        for x in self:
            new.insert(x)
        if self.collision_type == "Double":
            self.hash1 = new.hash1
        else:
            self.hash = new.hash
        self.table = new.table
        self.num_elements = new.num_elements
        self.params = new_params
        
    def insert(self, x):
        # YOU DO NOT NEED TO MODIFY THIS
        super().insert(x)
        
        if self.get_load() >= 0.5:
            self.rehash()
            
            
class DynamicHashMap(HashMap):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        
    def rehash(self):
        # IMPLEMENT THIS FUNCTION
        new_table_size = get_next_size()
        while self.num_elements/new_table_size >= 0.5:
            new_table_size = get_next_size()
        new_params = self.params[:-1] + (new_table_size,)
        new = DynamicHashMap(self.collision_type, new_params)
        for x in self:
            new.insert(x)
        if self.collision_type == "Double":
            self.hash1 = new.hash1
        else:
            self.hash = new.hash
        self.table = new.table
        self.num_elements = new.num_elements
        self.params = new_params
        
    def insert(self, key):
        # YOU DO NOT NEED TO MODIFY THIS
        super().insert(key)
        
        if self.get_load() >= 0.5:
            self.rehash()