"Way of using String and Text"

types_of_ppl = 10
x = f"There are {types_of_ppl} type of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilariouse = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilariouse))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
