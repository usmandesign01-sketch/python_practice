'''

Lists

A List is an ordered and mutable collection of items in Python.

Lists allow you to store multiple values inside a single variable.

For example, instead of creating separate variables for every fruit:
fruit1 = "Apple"
fruit2 = "Banana"
fruit3 = "Mango"

You can use a list:
fruits = ["Apple", "Banana", "Mango"]

*Why Do We Need Lists?*

Lists are useful for:
- Storing multiple values
- Managing collections of data
- Iterating through items
- Adding and removing elements
- Sorting and organizing data
- Working with datasets

*1. Creating a List*

Lists are created using square brackets [].
numbers = [10, 20, 30, 40, 50]

A list can contain different data types:
data = ["Python", 25, 3.14, True]

Although Python allows mixed data types, it's usually better to keep a list logically consistent.

*2. Accessing List Elements*

Lists use zero-based indexing, just like strings.
fruits = ["Apple", "Banana", "Mango"]

print(fruits[0])
print(fruits[1])
print(fruits[2])

Output:
Apple
Banana
Mango

The indexes are: Apple 0, Banana 1, Mango 2

*3. Negative Indexing*

You can access elements from the end using negative indexes.
fruits = ["Apple", "Banana", "Mango"]

print(fruits[-1])
print(fruits[-2])

Output:
Mango
Banana

-1 always refers to the last element.

*4. List Slicing*

You can extract a portion of a list using slicing.

numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])

Output:
[20, 30, 40]

Just like strings, the ending index is excluded.

*5. Lists Are Mutable*

One of the biggest differences between lists and strings is that lists are mutable.

This means you can change their elements.

fruits = ["Apple", "Banana", "Mango"]

fruits[1] = "Orange"

print(fruits)

Output:
['Apple', 'Orange', 'Mango']

*6. Adding Elements*

append() Adds an item to the end of the list.

fruits = ["Apple", "Banana"]

fruits.append("Mango")

print(fruits)

Output: ['Apple', 'Banana', 'Mango']

insert() Adds an item at a specific position.

fruits = ["Apple", "Mango"]

fruits.insert(1, "Banana")

print(fruits)

Output: 
['Apple', 'Banana', 'Mango']

*7. Removing Elements*

remove() Removes the first matching value.

fruits = ["Apple", "Banana", "Mango"]

fruits.remove("Banana")

print(fruits)

Output: ['Apple', 'Mango']

pop() Removes an element using its index and returns that element.

fruits = ["Apple", "Banana", "Mango"]

removed = fruits.pop(1)

print(removed)
print(fruits)

Output:
Banana
['Apple', 'Mango']

If no index is provided, pop() removes the last element.

*8. Finding the Length*

Use len() to find the number of elements.

numbers = [10, 20, 30, 40]
print(len(numbers))

Output: 4

*9. Checking if an Element Exists*

Use in to check whether an item exists.

fruits = ["Apple", "Banana", "Mango"]

print("Mango" in fruits)

Output: True

*10. Looping Through a List*

Lists are commonly used with loops.

numbers = [10, 20, 30]

for number in numbers:
    print(number)

Output: 10, 20, 30

*11. Sorting a List*

You can sort a list using sort().

numbers = [50, 10, 40, 20, 30]

numbers.sort()

print(numbers)

Output: [10, 20, 30, 40, 50]

For descending order:
numbers.sort(reverse=True)

*12. Useful List Methods*

Some commonly used methods are:

- append() Add an item to the end
- insert() Add an item at a specific position
- remove() Remove a specific value
- pop() Remove an item by index
- sort() Sort the list
- reverse() Reverse the list
- count() Count occurrences
- index() Find the position of an item
- clear() Remove all items

*13. Lists in AI and Data Science*

Lists are extremely important when working with data.

For example, you might have model predictions:

predictions = [0.92, 0.76, 0.81, 0.65]

Or a collection of text inputs:

documents = [
    "Python is easy to learn",
    "Machine Learning uses data",
    "AI is transforming technology"
]

Later, when you learn NumPy, Pandas, Machine Learning, and NLP, you'll encounter collections of data constantly.

*Lists vs Strings*

- Stores: List = Multiple items, String = Characters/text
- Mutable: List = ✅ Yes, String = ❌ No
- Indexing: ✅ Yes both
- Slicing: ✅ Yes both
- Uses: List = [], String = Quotes

*Common Beginner Mistakes*

❌ Forgetting that indexing starts from 0
❌ Confusing remove() with pop()
❌ Trying to access an index that doesn't exist
❌ Modifying a list while iterating over it without understanding the consequences

*Best Practices*

✅ Use meaningful list names
✅ Keep related data together
✅ Use list methods instead of manually rebuilding lists when appropriate
✅ Choose the right data structure depending on your requirements

*Key Takeaways*

- Lists store multiple items in an ordered collection
- Lists are mutable
- Python lists support indexing and slicing
- append() adds an item to the end
- insert() adds an item at a specific position
- remove() removes a value
- pop() removes an item by index
- Lists are heavily used in Python, Data Science, and AI

'''