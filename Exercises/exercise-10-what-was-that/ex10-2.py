"Here demonstration of each escape character behaviour."

# Backslash
print("Backslash: \\")

# Single quote
print('Single quote: \'')

# Double quote
print("Double quote: \"")

# ASCII bel (may beep in some terminals)
print("Bell (\\a): \a")

# ASCII backspace
print("Backspace: ABC\bD")

# ASCII formfeed (rare, behaves like a page break in some contexts)
print("Formfeed: ABC\fDEF")

# ASCII newline
print("Linefeed (newline): Line1\nLine2")

# Unicode character by name (Python only)
print("Unicode name (\\N{name}): \N{GREEK CAPITAL LETTER DELTA}")

# Carriage return
print("Carriage return: Hello\rWorld")

# Horizontal tab
print("Tab:\tColumn2")

# Unicode with 16-bit hex
print("Unicode 16-bit: \u03A9")

# Unicode with 32-bit hex
print("Unicode 32-bit: \U0001F600")

# Vertical tab
print("Vertical tab: A\vB")

# Octal value
print("Octal value: \101")

# Hex value
print("Hex value: \x41")
