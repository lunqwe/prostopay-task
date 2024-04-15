import pytest 

"""
This example demonstrates the implementation of a hashmap (hash map) using a simple hash function to facilitate the process of searching and accessing data based on a key.

Passenger Class:
   This class represents a passenger. It has two attributes: the passenger's name and seat number.

HashMap Class:
   This class implements a hashmap using an array of fixed size. The size of the array is determined when an instance of the class is created.
   - The _get_hash method takes a key and returns the hash code, which will be used to determine the index in the array where the value will be stored.
   - The put method takes a key and value, computes the hash code of the key, and stores the value in the corresponding position of the hashmap array.
   - The get method takes a key, computes the hash code of the key, and returns the value stored at the corresponding position of the hashmap array.
""" 

class Passanger:
    def __init__(self, passanger_name: str, seat_number: int):
        self.name = passanger_name
        self.seat_number = seat_number

class HashMap:
    def __init__(self, size):
        self.size = size
        self.map = [None] * self.size

    def _get_hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            raise ValueError(f"Collision detected for key {key}.")
        else:
            self.map[key_hash] = value

    def get(self, key):
        key_hash = self._get_hash(key)
        if key_hash:
            return self.map[key_hash]
        else:
            raise ValueError(f"Value for key {key} not found.")
        
    def delete(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            self.map[key_hash] = None
            print(f"Element with key {key} has been deleted.")
            return None
        else:
            raise ValueError("Element not found.")
    

def test_hashmap_example():
    """
    Example Usage:
    - An instance of the hashmap `airplane` with a size of 100 is created.
    - An instance of the passenger `passenger` with the name "John" and seat number 1 is created.
    - The passenger is added to the hashmap using the seat number as the key and the name as the value.
    - The passenger's name is retrieved from the hashmap using their seat number as the key using the `get` method and displayed.

    This example illustrates the basic principles of a hashmap: hashing keys, adding, deleting, and retrieving data by key
    """
    airplane = HashMap(100)
    passanger1 = Passanger("John", 1)
    passanger2 = Passanger("David", 2)

    airplane.put(passanger1.seat_number, passanger1.name)
    airplane.put(passanger2.seat_number, passanger2.name)

    assert airplane.get(passanger1.seat_number) == "John"
    assert airplane.get(passanger2.seat_number) == "David"

    error_passanger = Passanger('Pupa', 1)

    with pytest.raises(ValueError) as put_exc_info:
        airplane.put(error_passanger.seat_number, error_passanger.name)
    
    assert str(put_exc_info.value) == "Collision detected for key 1."

    error_passanger.seat_number = 3
    with pytest.raises(ValueError) as get_exc_info:
        airplane.get(error_passanger.seat_number)

    assert str(get_exc_info)



