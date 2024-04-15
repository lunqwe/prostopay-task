from .models import Passanger, HashMap
import pytest



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
