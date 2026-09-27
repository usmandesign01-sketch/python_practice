# let's work on string

name = "Usman"
print(type(name))

print(name.upper())
print(name.lower())

'''



Strings*

A String is a sequence of characters used to represent text. Names, sentences, email addresses,
file paths, messages, and many other types of textual information are represented using strings.

Example:
name = "Alice"
message = "Welcome to Python!"

Here, both `"Alice"` and `"Welcome to Python!"` are strings.

*Why Do We Need Strings?*

Strings are essential for:
- Storing text
- Processing user input
- Working with names and messages
- Reading and processing files
- Handling data from APIs
- Processing text for AI and NLP applications

*1. Creating Strings*

Strings can be created using single or double quotes.

name = "Alice"
city = 'Mumbai'

Both are valid.

You can also use triple quotes for multi-line strings:

message = """This is
a multi-line
string."""

*2. Accessing Characters*

Every character in a string has an index. Python uses zero-based indexing, meaning the first character is at index 0.

word = "Python"

print(word[0]) # P
print(word[1]) # y
print(word[5]) # n

The indexes look like this:
P y t h o n
0 1 2 3 4 5

*3. Negative Indexing*

Python also supports negative indexes. The last character has index -1.
word = "Python"

print(word[-1]) # n
print(word[-2]) # o
Indexing from the end looks like:

P y t h o n
-6 -5 -4 -3 -2 -1

*4. String Slicing*

Slicing allows you to extract part of a string.
Syntax: `string[start:end]` — The end index is not included.

Example:
word = "Python"
print(word[0:3]) # Pyt

Because indexes 0, 1, and 2 are included, but index 3 is excluded.

*Slicing with a Step*
word = "Python"
print(word[0:6:2]) # Pto

*5. String Length*

Use the `len()` function to find the number of characters.
text = "Python"
print(len(text)) # 6

Spaces are also counted as characters.

*6. Important String Methods*

*upper()* — Converts text to uppercase.

text = "hello"
print(text.upper()) # HELLO

*lower()* — Converts text to lowercase.

text = "HELLO"
print(text.lower()) # hello

*strip()* — Removes leading and trailing whitespace.

text = " Python "
print(text.strip()) # Python

*replace()* — Replaces part of a string.

text = "I like Java"
print(text.replace("Java", "Python")) # I like Python

*split()* — Splits a string into a list.

text = "Python is powerful"
words = text.split()
print(words) # ['Python', 'is', 'powerful']

*join()* — Combines elements into a string.

words = ["Python", "is", "powerful"]
text = " ".join(words)
print(text) # Python is powerful

*7. Checking Content*

You can check whether a substring exists using `in`.

text = "Python is easy"
print("Python" in text) # True
print("Java" not in text) # True

*8. Strings Are Immutable*

One of the most important things to understand about Python strings is that they are immutable.
This means you cannot directly change an individual character.

.. This is not allowed:
word = "Python"
word[0] = "J"
Instead, you create a new string:
word = "Python"
word = "J" + word[1:]
print(word) # Jython

*9. String Concatenation*

You can combine strings using `+`.
first_name = "Alice"
last_name = "Smith"
full_name = first_name + " " + last_name
print(full_name) # Alice Smith

*10. f-Strings*

f-strings provide a convenient way to insert variables into strings.
name = "Alice"
age = 25
message = f"My name is {name} and I am {age} years old."
print(message) # My name is Alice and I am 25 years old.

f-strings are widely used because they make formatted text easier to read.

*11. Strings in AI and NLP*

Strings become especially important when you move into Artificial Intelligence.
AI systems frequently work with text such as: User questions, Chat messages, Documents,
Reviews, Emails, Search queries, AI prompts.

Before text can be processed by many NLP and LLM systems, it often needs to be cleaned,
transformed, tokenized, or converted into numerical representations.

For example:
text = " AI is AMAZING! "
cleaned_text = text.strip().lower()
print(cleaned_text) # ai is amazing!

This is a very simple example of text preprocessing.

* Common Mistakes:
.. Forgetting that indexing starts at 0.
.. Assuming the end index in slicing is included.
.. Trying to modify an individual character.
.. Confusing split() with join().
.. Forgetting that spaces count toward string length.

*Best Practices*
.. Use meaningful variable names.
.. Use appropriate string methods instead of manually processing characters when possible.
.. Use f-strings for readable string formatting.
.. Remember that strings are immutable.

*Key Takeaways*
- A string is a sequence of characters.
- Python uses zero-based indexing.
- Negative indexing starts from -1.
- Slicing extracts portions of a string.
- len() returns the number of characters.
- Strings are immutable.
- Methods such as upper(), lower(), strip(), split(), and replace() are extremely useful.
- Strings are fundamental to NLP, LLMs, and AI applications.

'''