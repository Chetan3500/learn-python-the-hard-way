# Dictionary

A dictionary display is a possibly empty series of key/value pairs enclosed in curly braces.

# Exercise

1. Create an ex39.py and write following content:
    ```py
    # create a mapping of state to abbreviation
    states = {
            'Oregon': 'OR',
            'Florida': 'FL',
            'California': 'CA',
            'New York': 'NY',
            'Michigan': 'MI'
            }

    # create a basic set of states and some cities in them
    cities = {
            'CA': 'San Francisco',
            'MI': 'Detroit',
            'FL': 'Jacksonville'
            }

    # add some more cities
    cities['NY'] = 'New York'
    cities['OR'] = 'Portland'

    # print out some cities
    print('-' * 10)
    print("NY State has: ", cities['NY'])
    print("OR State has: ", cities['OR'])

    # print some states
    print('-' * 10)
    print("Michigan's abbreviation is: ", states['Michigan'])
    print("Florida's abbreviation is: ", states['Florida'])

    # do it by using the state then cities dict
    print('-' * 10)
    print("Michigan has: ", cities[states['Michigan']])
    print("Florida has: ", cities[states['Florida']])

    # print every state abbreviation
    print('-' * 10)
    for state, abbrev in list(states.items()):
        print(f"{state} is abbreviated {abbrev}")

    # print every city in state
    print('-' * 10)
    for abbrev, city in list(cities.items()):
        print(f"{abbrev} has the city {city}")

    # now do both at the same time
    print('-' * 10)
    for state, abbrev in list(states.items()):
        print(f"{state} state is abbreviated {abbrev}")
        print(f"and has city {cities[abbrev]}")

    print('-' * 10)
    # safely get a abbreviation by state that might not be there
    state = states.get('Texas')

    if not state:
        print("Sorry, no Texas.")

    # get a city with a default value
    city = cities.get('TX', 'Does Not Exist')
    print(f"The city for the state 'TX' is: {city}")
    ```
2. Run Script
    ```
    $ python ex39.py 
    ----------
    NY State has:  New York
    OR State has:  Portland
    ----------
    Michigan's abbreviation is:  MI
    Florida's abbreviation is:  FL
    ----------
    Michigan has:  Detroit
    Florida has:  Jacksonville
    ----------
    Oregon is abbreviated OR
    Florida is abbreviated FL
    California is abbreviated CA
    New York is abbreviated NY
    Michigan is abbreviated MI
    ----------
    CA has the city San Francisco
    MI has the city Detroit
    FL has the city Jacksonville
    NY has the city New York
    OR has the city Portland
    ----------
    Oregon state is abbreviated OR
    and has city Portland
    Florida state is abbreviated FL
    and has city Jacksonville
    California state is abbreviated CA
    and has city San Francisco
    New York state is abbreviated NY
    and has city New York
    Michigan state is abbreviated MI
    and has city Detroit
    ----------
    Sorry, no Texas.
    The city for the state 'TX' is: Does Not Exist
    ```

## Noted

Dictionaries can be created by several means:

   * Use a comma-separated list of "key: value" pairs within braces:
     "{'jack': 4098, 'sjoerd': 4127}" or "{4098: 'jack', 4127:
     'sjoerd'}"

   * Use a dict comprehension: "{}", "{x: x ** 2 for x in range(10)}"

   * Use the type constructor: "dict()", "dict([('foo', 100), ('bar',
     200)])", "dict(foo=100, bar=200)"

For more to know run `pydoc3.10 DICTIONARIES`