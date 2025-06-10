# Automated Testing

These automated tests won’t catch all your bugs, but they will cut down on the time you spend repeatedly typing and running your code.

# Exercise

**Part 1:**

1. Copy [skeleton dir](../exercise-46-project-skeleton/projects/) of ex46.
    ```sh
    cp -r ../exercise-46-project-skeleton/projects/ .
    ```
2. Rename everything with NAME to ex47.
3. Change the word NAME in all the files to ex47.
4. Finally, remove all the *.pyc files to make sure you’re clean.

**Part 2:**

1. Create ex47/game.py file and write the following:
    ```py
    class Room():

        def __init__(self, name, description):
            self.name = name
            self.description = description
            self.paths = {}

        def go(self, direction):
            return self.paths.get(direction, None)

        def add_paths(self, paths):
            self.paths.update(paths)
    ```
2. Change test skeleton (Name__init__.py to BLAH_tests.py) and write the following:
    ```py
    from ex47.game import Room

    def test_room():
        gold = Room("GoldRoom",
                """This room has gold in it you can grab.
                There's a door to the north.""")
        assert gold.name == "GoldRoom"
        assert gold.paths == {}

    def test_room_paths():
        center = Room("Center", "Test room in the center.")
        north = Room("North", "Test room in the north.")
        south = Room("South", "Test room in the south.")

        center.add_paths({'north': north, 'south': south})
        assert center.go('north') == north
        assert center.go('south') == south

    def test_map():
        start = Room("Start", "You can go west and down a hole.")
        west = Room("Trees", "There are trees here, you can go east.")
        down = Room("Dungeon", "It's dark down here, you can go up.")

        start.add_paths({'west': west, 'down': down})
        west.add_paths({'east': start})
        down.add_paths({'up': start})

        assert start.go('west') == west
        assert start.go('west').go('east') == start
        assert start.go('down').go('up') == start
    ```

Follow this loose set of guidelines when making your tests:
1. Test files go in tests/ and are named BLAH_tests.py, otherwise nosetests won’t run them. This also keeps your tests from clashing with your other code.
2. Write one test file for each module you make.
3. Keep your test cases (functions) short, but do not worry if they are a bit messy. Test cases are usually kind of messy.
4. Even though test cases are messy, try to keep them clean and remove any repetitive code you can. Create helper functions that get rid of duplicate code. You will thank me later when you make a change and then have to change your tests. Duplicated code will make changing your tests more difficult.
5. Finally, do not get too attached to your tests. Sometimes, the best way to redesign something is to just delete it and start over.

Since we used pytest so to test:
```sh
$ pytest BLAH_tests.py
```