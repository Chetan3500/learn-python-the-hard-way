# Functions and Variables

## Exercise

1. Create an ex19.py and write following content:
    ```py
    def cheese_and_crackers(cheese_count, boxes_of_crackers):
        print(f"""You have {cheese_count} cheeses!
    You have {boxes_of_crackers} boxes of crackers!
    Man that's enough for a party!
    Get a blanket.\n""")

    print("We can just give the function numbers directly:")
    cheese_and_crackers(20, 30)

    print("OR, we can use variables from our script:")
    amount_of_cheese = 10
    amount_of_crackers = 50

    cheese_and_crackers(amount_of_cheese, amount_of_crackers)

    print("We can even do math inside too:")
    cheese_and_crackers(10 + 20, 5 + 6)

    print("And we can combine the two, variables and math:")
    cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
    ```
2. Run the script and output be:
    ```
    We can just give the function numbers directly:
    You have 20 cheeses!
    You have 30 boxes of crackers!
    Man that's enough for a party!
    Get a blanket.

    OR, we can use variables from our script:
    You have 10 cheeses!
    You have 50 boxes of crackers!
    Man that's enough for a party!
    Get a blanket.

    We can even do math inside too:
    You have 30 cheeses!
    You have 11 boxes of crackers!
    Man that's enough for a party!
    Get a blanket.

    And we can combine the two, variables and math:
    You have 110 cheeses!
    You have 1050 boxes of crackers!
    Man that's enough for a party!
    Get a blanket.
    ```