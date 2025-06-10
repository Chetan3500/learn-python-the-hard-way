# Make a game

Well this exercise is do-your-own type. Make a story for a game then start working on it. Here are few things that can gain from doing this exercise which need to inlcude in exercise:
1. Make a different game from last one.
2. Use more than one file, and use `import` to use them. Make sure you know what that is.
3. Use one class per room and give the classes names that fit their purposes (like GoldRoom, KoiPondRoom).
4. Your runner will need to know about these rooms, so make a class that runs them and knows about them. There’re plenty of ways to do this, but consider having each room return what room is next or setting a variable of what room is next.

Before starting here the remaining note that might help:

**Function style**
- Programmer call functions that are part of classes "method".
- Name function like giving them a command. Eg. pop() is saying “Hey list, pop this off.” It isn’t called remove_from_end_of_list because even though that’s what it does, that’s not a command to a list.
- Keep function small and simple.

**Class style**
- Name of class should be in CamelCase. Eg. SuperGoldFactory.
- Try not to do too much in __init__ functions. It make harder to use.
- Name of function can be made with '_'. Eg. my_awesome_hair.
- Be consistent in how you organize your function arguments. If your class has to deal with users, dogs, and cats, keep that order throughout unless it really doesn’t make sense. If you have one function that takes (dog, cat, user) and the other takes (user, cat, dog), it’ll be hard to use.
- Try not to use variables that come from the module or globals. They should be fairly self-contained.

**Code style** (Author opinion)
- Give your code vertical space so people can read it. You will find some very bad programmers who are able to write reasonable code but who do not add any spaces. This is bad style in any language because the human eye and brain use space and vertical alignment to scan and separate visual elements. Not having space is the same as giving your code an awesome camouflage paint job.
- If you can’t read it out loud, it’s probably hard to read. If you are having a problem making something easy to use, try reading it out loud. Not only does this force you to slow down and really read it, but it also helps you find difficult passages and things to change for readability.
- Try to do what other people are doing in Python until you find your own style.
- Once you find your own style, do not be a jerk about it. Working with other people’s code is part of being a programmer, and other people have really bad taste. Trust me, you will probably have really bad taste, too, and not even realize it.
- If you find someone who writes code in a style you like, try writing something that mimics that style.

**Good Comment** (Author opinion)
- Programmers will tell you that your code should be readable enough that you do not need comments. They’ll then tell you in their most official sounding voice, “Ergo one should never write comments or documentation. QED.” Those programmers are either consultants who get paid more if other people can’t use their code, or incompetents who tend to never work with other people. Ignore them and write comments.
- When you write comments, describe why you are doing what you are doing. The code already says how, so why you did things the way you did is more important.
- When you write doc comments for your functions, make the comments documentation for
-omeone who will have to use your code. You do not have to go crazy, but a nice little sentence about what someone can do with that function helps a lot.
- While comments are good, too many are bad, and you have to maintain them. Keep your comments relatively short and to the point, and if you change a function, review the comment to make sure it’s still correct.

