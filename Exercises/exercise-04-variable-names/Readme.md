# Variable and Names

Variable are nothing but a name which use to store specific type of value.

## Exercise

1. Create ex4.py and write following content:

    ```py
    cars = 100
    space_in_a_car = 4.0
    drivers = 30
    passengers = 90
    cars_not_driven = cars - drivers
    cars_driven = drivers
    carpool_capacity = cars_driven * space_in_a_car
    average_passengers_per_cars = passengers / cars_driven

    print("There are", cars, "cars availabe.")
    print("There are only", drivers, "drivers available.")
    print("There will be", cars_not_driven, "empty cars today.")
    print("We can transport", carpool_capacity, "people today.")
    print("We have", passengers, "to carpool today.")
    print("We need to put about", average_passengers_per_cars, "in each car.")
    ```

2. On terminal run `python ex4.py`

3. Output be:

    ```
    There are 100 cars availabe.
    There are only 30 drivers available.
    There will be 70 empty cars today.
    We can transport 120.0 people today.
    We have 90 to carpool today.
    We need to put about 3.0 in each car.
    ```
