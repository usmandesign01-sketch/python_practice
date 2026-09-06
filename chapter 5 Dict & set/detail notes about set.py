''' Sets*

A Set is an unordered collection of unique elements in Python.

Unlike Lists and Tuples, a Set does not allow duplicate values.

Example:
numbers = {1, 2, 3, 4, 5}
print(numbers)

*Why Do We Need Sets?*
Sets are useful when you need to:

- Remove duplicate values.
- Quickly check whether an item exists.
- Perform mathematical set operations.
- Compare collections of data.
- Work efficiently with unique values.

*1. Creating a Set*
Sets are usually created using curly braces {}.

fruits = {"Apple", "Banana", "Mango"}
print(fruits)

A Set can contain different data types:
data = {10, "Python", 3.14, True}

However, every element must be hashable.

*2. Sets Automatically Remove Duplicates*

This is one of the most important properties of a Set.

numbers = {1, 2, 2, 3, 3, 4}
print(numbers)

Output will contain each value only once:
{1, 2, 3, 4}

This makes Sets very useful for removing duplicates.

numbers = [1, 2, 2, 3, 3, 4]
unique_numbers = set(numbers)
print(unique_numbers)

*3. Sets Are Unordered*
Sets do not provide positional indexing like Lists and Tuples.

So this is not valid:

numbers = {10, 20, 30}
print(numbers[0])

It produces a TypeError.
If you need elements in a specific order or need indexing, a List may be more appropriate.

*4. Adding Elements*
Use `add()` to add a single element.

numbers = {1, 2, 3}
numbers.add(4)
print(numbers)

*5. Adding Multiple Elements*
Use `update()` to add multiple elements.

numbers = {1, 2, 3}
numbers.update([4, 5, 6])
print(numbers)

*6. Removing Elements*

- *remove()* — Removes a specific element. If the element doesn't exist, it raises a KeyError.
- *discard()* — Also removes an element, but does not raise an error if the element is missing.

numbers = {1, 2, 3}
numbers.discard(10)
print(numbers)

No error occurs.

*7. Set Operations*
Suppose we have:
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

- *Union:* Combines elements from both sets. `A | B` or `A.union(B)` → `{1, 2, 3, 4, 5, 6}`
- *Intersection:* Returns common elements. `A & B` or `A.intersection(B)` → `{3, 4}`
- *Difference:* Elements in first but not second. `A - B` → `{1, 2}`
- *Symmetric Difference:* In either, but not both. `A ^ B` → `{1, 2, 5, 6}`

*8. Checking Membership*
Sets are very useful for checking whether an element exists.

fruits = {"Apple", "Banana", "Mango"}
print("Apple" in fruits) # True

Set membership testing is very efficient because Sets are implemented using hash tables.

*9. Empty Set — Important Trap* ⚠️
This does not create an empty Set:
data = {}

It creates an empty Dictionary.
To create an empty Set, use:
data = set()

*10. Immutable Elements Only*
Set elements must be hashable.

- This works: `{1, 2, 3}`
- This doesn't: `{[1][2], [3][4]}` — Lists are mutable
- This works: `{(1, 2), (3, 4)}` — Tuple with hashable elements

*11. Sets in AI and Data Science*
Sets are useful in many data-processing tasks.

categories = ["AI", "ML", "AI", "NLP", "ML"]
unique_categories = set(categories)

Sets can also be useful for:

- Removing duplicate records.
- Finding unique labels.
- Comparing datasets.
- Checking whether values exist.
- Finding common elements between datasets.

*List vs Tuple vs Set*
Feature	      List  Tuple	 Set
Ordered	    ✅	  ✅	     ❌
Mutable	    ✅	  ❌	     ✅
Duplicates	✅	  ✅	     ❌
Indexing	    ✅	 ✅	       ❌
Syntax        	[]	     ()         	{}

⚠️ *One Important Note*
Modern Python guarantees that dictionaries preserve insertion order, but sets should still be treated as unordered collections. Don't rely on a Set's iteration order.

*Common Beginner Mistakes*
❌ Trying to access a Set using an index.
❌ Assuming Sets preserve a specific order.
❌ Using {} when you want an empty Set.
❌ Trying to put a List inside a Set.
❌ Confusing remove() with discard().

*Best Practices*
✅ Use Sets when uniqueness matters.
✅ Use Sets for efficient membership checks.
✅ Use discard() when you want to safely remove a potentially missing element.
✅ Use Lists or Tuples when order and indexing are important.

*Key Takeaways*

- Sets store unique elements.
- Sets don't support indexing.
- Sets are mutable, but their individual elements must be hashable.
- add() adds one element, update() adds multiple.
- remove() raises an error if missing, discard() doesn't.
- Sets support Union, Intersection, Difference, and Symmetric Difference.
- Extremely useful for removing duplicates and membership checks.

'''