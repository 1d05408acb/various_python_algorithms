import hashlib

def hash_generator(my_string):
    """Generate a hash for a given string."""
    return hashlib.shake_256(my_string.encode()).hexdigest(5)

if __name__ == "__main__":
    string = input ("Enter a string to hash: ")
    print (hash_generator(string))

# Path: main.py
