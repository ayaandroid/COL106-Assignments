import hash_table as ht

class DigitalLibrary:
    # DO NOT CHANGE FUNCTIONS IN THIS BASE CLASS
    def __init__(self):
        pass
    
    def distinct_words(self, book_title):
        pass
    
    def count_distinct_words(self, book_title):
        pass
    
    def search_keyword(self, keyword):
        pass
    
    def print_books(self):
        pass

def merge(A1, A2):
    n = len(A1)
    m = len(A2)
    merged = []
    i = 0
    j = 0
    while i < n and j < m:
        if A1[i] <= A2[j]:
            merged.append(A1[i])
            i += 1
        else:
            merged.append(A2[j])
            j += 1
    while i < n:
        merged.append(A1[i])
        i += 1
    while j < m:
        merged.append(A2[j])
        j += 1
    return merged

def mergesort(A):
    if len(A) <= 1:
        return A
    A1 = mergesort(A[:len(A)//2])
    A2 = mergesort(A[len(A)//2:])
    return merge(A1, A2)
  
class MuskLibrary(DigitalLibrary):
    # IMPLEMENT ALL FUNCTIONS HERE
    def __init__(self, book_titles, texts):
        self.lib = []
        for i in range(len(book_titles)):
            sorted_text = mergesort(texts[i])
            distinct_words = [sorted_text[0]]
            for word in sorted_text:
                if distinct_words[-1] != word:
                    distinct_words.append(word)
            self.lib.append((book_titles[i], distinct_words))
        self.lib = mergesort(self.lib)
    
    def distinct_words(self, book_title):
        low = 0
        high = len(self.lib) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.lib[mid][0] < book_title:
                low = mid + 1
            elif self.lib[mid][0] == book_title:
                return self.lib[mid][1]
            else:
                high = mid - 1
    
    def count_distinct_words(self, book_title):
        low = 0
        high = len(self.lib) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.lib[mid][0] < book_title:
                low = mid + 1
            elif self.lib[mid][0] == book_title:
                return len(self.lib[mid][1])
            else:
                high = mid - 1
    
    def search_keyword(self, keyword):
        result = []
        for book in self.lib:
            distinct_words = book[1]
            low = 0
            high = len(distinct_words) - 1
            while low <= high:
                mid = (low + high) // 2
                if distinct_words[mid] < keyword:
                    low = mid + 1
                elif distinct_words[mid] == keyword:
                    result.append(book[0])
                    break
                else:
                    high = mid - 1
        return result
    
    def print_books(self):
        for book in self.lib:
            print(book[0], ': ', ' | '.join(book[1]), sep = '')

class JGBLibrary(DigitalLibrary):
    # IMPLEMENT ALL FUNCTIONS HERE
    def __init__(self, name, params):
        '''
        name    : "Jobs", "Gates" or "Bezos"
        params  : Parameters needed for the Hash Table:
            z is the parameter for polynomial accumulation hash
            Use (mod table_size) for compression function
            
            Jobs    -> (z, initial_table_size)
            Gates   -> (z, initial_table_size)
            Bezos   -> (z1, z2, c2, initial_table_size)
                z1 for first hash function
                z2 for second hash function (step size)
                Compression function for second hash: mod c2
        '''
        
        if name == "Jobs":
            self.collision_type = "Chain"
        elif name == "Gates":
            self.collision_type = "Linear"
        else:
            self.collision_type = "Double"
    
        self.lib = ht.HashMap(self.collision_type, params)
        self.catalog = []

        self.params = params
    
    def add_book(self, book_title, text):
        word_set = ht.HashSet(self.collision_type, self.params)
        for word in text:
            word_set.insert(word)
        self.lib.insert((book_title, word_set))
        self.catalog.append(book_title)

    def distinct_words(self, book_title):
        result = list(self.lib.find(book_title))
        if result is not None:
            return list(result)
    
    def count_distinct_words(self, book_title):
        result = self.lib.find(book_title)
        if result is not None:
            return result.num_elements
    
    def search_keyword(self, keyword):
        result = []
        for book_title in self.catalog:
            word_set = self.lib.find(book_title)
            if word_set.find(keyword):
                result.append(book_title)
        return result
    
    def print_books(self):
        for book_title, word_set in self.lib:
            print(book_title, ':', word_set, sep = '')