# Python Fundamentals - Day 1

A complete beginner's guide to Python basics: data types, variables, operators, strings, control flow, loops, and I/O.

---

## 1. Data Type Hierarchy

Every value in Python has a **type**. The most common built-in types you will use daily are shown below.

```mermaid
graph TD
    A[object] --> B[int]
    A --> C[float]
    A --> D[str]
    A --> E[bool]
    A --> F[NoneType]

    B --- B1["Whole numbers<br/>42, -7, 0"]
    C --- C1["Decimal numbers<br/>3.14, -0.5, 2.0"]
    D --- D1["Text / characters<br/>'hello', &quot;world&quot;"]
    E --- E1["True or False"]
    F --- F1["None<br/>(represents nothing)"]

    style A fill:#4a90d9,color:#fff
    style B fill:#5cb85c,color:#fff
    style C fill:#5cb85c,color:#fff
    style D fill:#f0ad4e,color:#fff
    style E fill:#d9534f,color:#fff
    style F fill:#777,color:#fff
```

> **Key insight:** `bool` is actually a subclass of `int` in Python. `True` is `1` and `False` is `0`.

```python
# Check the type of any value
type(42)        # <class 'int'>
type(3.14)      # <class 'float'>
type("hello")   # <class 'str'>
type(True)      # <class 'bool'>
type(None)      # <class 'NoneType'>
```

```mermaid
graph LR
    subgraph Numeric
        int
        float
        bool
    end
    subgraph Text
        str
    end
    subgraph Special
        NoneType
    end

    bool -.->|"subclass of"| int
```

---

## 2. Variables & Assignment

A **variable** is a name that refers to a value stored in memory. Think of it as a label you stick on a box.

```mermaid
graph LR
    A["name = 'Alice'"] --> B["name"] --> C["'Alice'<br/>(str object in memory)"]
    D["age = 25"] --> E["age"] --> F["25<br/>(int object in memory)"]

    style C fill:#f0ad4e,color:#fff
    style F fill:#5cb85c,color:#fff
```

### Assignment Basics

```python
# Single assignment
x = 10
name = "Alice"

# Multiple assignment on one line
a, b, c = 1, 2, 3

# Same value to multiple variables
x = y = z = 0

# Swapping values (Python makes this easy!)
a, b = b, a
```

### Naming Conventions

| Rule                       | Good                 | Bad                          |
| -------------------------- | -------------------- | ---------------------------- |
| Start with letter or `_`   | `my_var`, `_private` | `2fast`                      |
| Use `snake_case`           | `user_name`          | `userName`                   |
| No spaces or special chars | `total_count`        | `total count`, `total-count` |
| Avoid reserved keywords    | `my_class`           | `class`, `for`, `if`         |
| Be descriptive             | `student_age`        | `x`, `sa`                    |

```python
# Reserved keywords you CANNOT use as variable names:
# False, True, None, and, or, not, if, elif, else,
# for, while, break, continue, pass, def, return,
# class, import, from, as, try, except, finally,
# raise, with, yield, lambda, global, nonlocal, del,
# in, is, assert
```

---

## 3. Arithmetic Operators

```python
# Addition
5 + 3        # 8

# Subtraction
10 - 4       # 6

# Multiplication
6 * 7        # 42

# Division (always returns float)
10 / 3       # 3.3333...
10 / 2       # 5.0  <-- still a float!

# Floor Division (rounds down to nearest int)
10 // 3      # 3
-10 // 3     # -4  (rounds toward negative infinity)

# Modulo (remainder)
10 % 3       # 1
17 % 5       # 2

# Exponent (power)
2 ** 3       # 8
9 ** 0.5     # 3.0  (square root!)
```

### Augmented Assignment

```python
x = 10
x += 5    # x = x + 5   -> 15
x -= 3    # x = x - 3   -> 12
x *= 2    # x = x * 2   -> 24
x /= 4    # x = x / 4   -> 6.0
x //= 2   # x = x // 2  -> 3.0
x %= 2    # x = x % 2   -> 1.0
x **= 3   # x = x ** 3  -> 1.0
```

```mermaid
graph TD
    A["10 / 3"] -->|"True Division"| B["3.3333..."]
    C["10 // 3"] -->|"Floor Division"| D["3"]
    E["10 % 3"] -->|"Modulo"| F["1"]

    style B fill:#5cb85c,color:#fff
    style D fill:#f0ad4e,color:#fff
    style F fill:#d9534f,color:#fff
```

---

## 4. Comparison & Logical Operators

### Comparison Operators

```python
# All comparison operators return True or False

5 == 5      # True   (equal to)
5 != 3      # True   (not equal to)
5 > 3       # True   (greater than)
5 < 3       # False  (less than)
5 >= 5      # True   (greater than or equal to)
5 <= 3      # False  (less than or equal to)
```

### Logical Operators

```mermaid
graph TD
    subgraph "and (both must be True)"
        A1["True and True"] --> R1["True"]
        A2["True and False"] --> R2["False"]
        A3["False and True"] --> R3["False"]
        A4["False and False"] --> R4["False"]
    end

    style R1 fill:#5cb85c,color:#fff
    style R2 fill:#d9534f,color:#fff
    style R3 fill:#d9534f,color:#fff
    style R4 fill:#d9534f,color:#fff
```

```mermaid
graph TD
    subgraph "or (at least one must be True)"
        B1["True or True"] --> S1["True"]
        B2["True or False"] --> S2["True"]
        B3["False or True"] --> S3["True"]
        B4["False or False"] --> S4["False"]
    end

    style S1 fill:#5cb85c,color:#fff
    style S2 fill:#5cb85c,color:#fff
    style S3 fill:#5cb85c,color:#fff
    style S4 fill:#d9534f,color:#fff
```

```mermaid
graph TD
    subgraph "not (flips the value)"
        C1["not True"] --> T1["False"]
        C2["not False"] --> T2["True"]
    end

    style T1 fill:#d9534f,color:#fff
    style T2 fill:#5cb85c,color:#fff
```

```python
age = 25
has_license = True

# Combining comparisons with logical operators
if age >= 18 and has_license:
    print("Can drive")

# Chained comparisons (Python special feature!)
x = 5
1 < x < 10      # True  (same as: 1 < x and x < 10)
1 < x < 3       # False
```

---

## 5. Operator Precedence

Operators at the top are evaluated first. When in doubt, use parentheses `()` to make your intent clear.

```mermaid
graph TD
    P1["1. () Parentheses<br/>(highest priority)"] --> P2
    P2["2. ** Exponent"] --> P3
    P3["3. +x, -x, ~x  Unary"] --> P4
    P4["4. *, /, //, %  Multiply / Divide"] --> P5
    P5["5. +, -  Add / Subtract"] --> P6
    P6["6. ==, !=, <, >, <=, >=  Comparisons"] --> P7
    P7["7. not  Logical NOT"] --> P8
    P8["8. and  Logical AND"] --> P9
    P9["9. or  Logical OR<br/>(lowest priority)"]

    style P1 fill:#d9534f,color:#fff
    style P2 fill:#e8603c,color:#fff
    style P3 fill:#e8783c,color:#fff
    style P4 fill:#f0ad4e,color:#fff
    style P5 fill:#c6c43e,color:#fff
    style P6 fill:#8cc63f,color:#fff
    style P7 fill:#5cb85c,color:#fff
    style P8 fill:#4a90d9,color:#fff
    style P9 fill:#6a5acd,color:#fff
```

```python
# Precedence in action
2 + 3 * 4        # 14  (not 20! multiplication first)
(2 + 3) * 4      # 20  (parentheses override)

2 ** 3 ** 2       # 512  (** is right-associative: 2 ** 9)
(2 ** 3) ** 2     # 64

not True or False  # False  (not applies to True first)
not (True or False)  # False
```

---

## 6. Strings

Strings are **sequences of characters**. They are **immutable** -- once created, they cannot be changed in place.

### Creating Strings

```python
# Single or double quotes (no difference)
s1 = 'hello'
s2 = "hello"

# Triple quotes for multi-line strings
s3 = """This is
a multi-line
string"""

# Escape characters
s4 = "He said \"hi\""   # He said "hi"
s5 = 'It\'s fine'       # It's fine
s6 = "Line1\nLine2"     # \n = newline
s7 = "Tab\there"        # \t = tab
```

### Indexing & Slicing

```mermaid
graph TD
    subgraph "String: 'Python'"
        direction LR
        I0["P<br/>index 0<br/>index -6"]
        I1["y<br/>index 1<br/>index -5"]
        I2["t<br/>index 2<br/>index -4"]
        I3["h<br/>index 3<br/>index -3"]
        I4["o<br/>index 4<br/>index -2"]
        I5["n<br/>index 5<br/>index -1"]
    end

    style I0 fill:#d9534f,color:#fff
    style I1 fill:#e8603c,color:#fff
    style I2 fill:#f0ad4e,color:#fff
    style I3 fill:#8cc63f,color:#fff
    style I4 fill:#4a90d9,color:#fff
    style I5 fill:#6a5acd,color:#fff
```

```python
s = "Python"

# Indexing (single character)
s[0]     # 'P'  (first character)
s[-1]    # 'n'  (last character)
s[2]     # 't'

# Slicing: s[start:stop:step]
# start = inclusive, stop = exclusive
s[0:3]   # 'Pyt'  (index 0, 1, 2)
s[2:5]   # 'tho'
s[:3]    # 'Pyt'  (start defaults to 0)
s[3:]    # 'hon'  (stop defaults to end)
s[:]     # 'Python'  (full copy)

# Slicing with step
s[::2]   # 'Pto'  (every 2nd character)
s[::-1]  # 'nohtyP'  (reverse the string!)
s[1:5:2] # 'yh'
```

```mermaid
graph LR
    subgraph "s = 'Python'"
        A["s[0:3]"] --> R1["'Pyt'"]
        B["s[2:]"] --> R2["'thon'"]
        C["s[::-1]"] --> R3["'nohtyP'"]
        D["s[::2]"] --> R4["'Pto'"]
    end
```

### Common String Methods

```python
s = "  Hello, World!  "

# Case methods
s.upper()       # '  HELLO, WORLD!  '
s.lower()       # '  hello, world!  '

# Whitespace removal
s.strip()       # 'Hello, World!'   (both sides)
s.lstrip()      # 'Hello, World!  ' (left only)
s.rstrip()      # '  Hello, World!' (right only)

# Splitting and joining
"a,b,c".split(",")           # ['a', 'b', 'c']
"hello world".split()        # ['hello', 'world'] (splits on whitespace)
", ".join(["a", "b", "c"])   # 'a, b, c'

# Finding and replacing
s = "Hello, World!"
s.find("World")     # 7  (index where it starts)
s.find("xyz")       # -1  (not found)
s.replace("World", "Python")  # 'Hello, Python!'
s.count("l")        # 3

# Checking content
"hello".startswith("he")  # True
"hello".endswith("lo")    # True
"abc123".isalnum()        # True
"abc".isalpha()           # True
"123".isdigit()           # True
```

### String Operations

```python
# Concatenation
"Hello" + " " + "World"   # 'Hello World'

# Repetition
"ha" * 3                  # 'hahaha'

# Length
len("Python")             # 6

# Membership
"Py" in "Python"          # True
"xyz" not in "Python"     # True
```

---

## 7. Control Flow

### if / elif / else

```mermaid
flowchart TD
    A[Start] --> B{condition 1?}
    B -->|True| C[Execute if block]
    B -->|False| D{condition 2?}
    D -->|True| E[Execute elif block]
    D -->|False| F[Execute else block]
    C --> G[Continue]
    E --> G
    F --> G
```

```python
age = 18

if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")
```

**Important rules:**

- Indentation matters! Use 4 spaces (not tabs).
- The colon `:` at the end of `if`, `elif`, `else` is required.
- `elif` and `else` are optional.
- You can have as many `elif` blocks as you want but only one `else`.

```python
# Ternary (one-line if/else)
status = "adult" if age >= 18 else "minor"
```

### for Loop

```mermaid
flowchart TD
    A[Start] --> B[Get next item from iterable]
    B --> C{More items?}
    C -->|Yes| D[Execute loop body]
    D --> B
    C -->|No| E[End / else block]
```

### while Loop

```mermaid
flowchart TD
    A[Start] --> B{condition?}
    B -->|True| C[Execute loop body]
    C --> B
    B -->|False| D[End / else block]
```

---

## 8. Loops

### for Loop

```python
# Looping over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Looping over a string
for char in "Hello":
    print(char)

# Looping over a range of numbers
for i in range(5):       # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 6):    # 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(i)

for i in range(5, 0, -1):  # 5, 4, 3, 2, 1 (countdown!)
    print(i)
```

### range() Explained

```mermaid
graph LR
    subgraph "range(stop)"
        A1["range(5)"] --> R1["0, 1, 2, 3, 4"]
    end
    subgraph "range(start, stop)"
        A2["range(2, 6)"] --> R2["2, 3, 4, 5"]
    end
    subgraph "range(start, stop, step)"
        A3["range(0, 10, 2)"] --> R3["0, 2, 4, 6, 8"]
        A4["range(5, 0, -1)"] --> R4["5, 4, 3, 2, 1"]
    end
```

### enumerate()

When you need both the **index** and the **value** during iteration:

```python
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# 0: apple
# 1: banana
# 2: cherry

# Start counting from a different number
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")
# 1: apple
# 2: banana
# 3: cherry
```

### while Loop

```python
count = 0
while count < 5:
    print(count)
    count += 1       # Don't forget this or infinite loop!

# while with user input
password = ""
while password != "secret":
    password = input("Enter password: ")
print("Access granted!")
```

### break and continue

```mermaid
flowchart TD
    A[Start loop] --> B{Check condition}
    B -->|continue| A
    B -->|break| C[Exit loop entirely]
    B -->|normal| D[Execute rest of body]
    D --> A
```

```python
# break - exits the loop immediately
for i in range(10):
    if i == 5:
        break           # stops at 5
    print(i)            # prints 0, 1, 2, 3, 4

# continue - skips to the next iteration
for i in range(10):
    if i % 2 == 0:
        continue        # skip even numbers
    print(i)            # prints 1, 3, 5, 7, 9
```

### Nested Loops

```python
# Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print("---")
```

```mermaid
flowchart TD
    A[Outer loop: i = 1] --> B[Inner loop: j = 1, 2, 3]
    B --> C[Outer loop: i = 2]
    C --> D[Inner loop: j = 1, 2, 3]
    D --> E[Outer loop: i = 3]
    E --> F[Inner loop: j = 1, 2, 3]
    F --> G[Done]
```

---

## 9. Input / Output

### print()

```python
# Basic printing
print("Hello, World!")

# Printing multiple values
name = "Alice"
age = 25
print("Name:", name, "Age:", age)    # separated by space

# Custom separator
print("a", "b", "c", sep="-")       # a-b-c

# Custom end character (default is newline)
print("Hello", end=" ")
print("World")                        # Hello World (on one line)
```

### f-strings (Formatted String Literals)

The modern and recommended way to format strings in Python (3.6+):

```python
name = "Alice"
age = 25

# Basic f-string
print(f"My name is {name} and I am {age} years old.")

# Expressions inside braces
print(f"Next year I'll be {age + 1}.")

# Formatting numbers
pi = 3.14159
print(f"Pi is approximately {pi:.2f}")    # Pi is approximately 3.14

price = 49.99
print(f"Price: ${price:>10.2f}")          # Price:      $49.99

# Padding and alignment
print(f"{'left':<20}")     # left aligned, 20 chars wide
print(f"{'center':^20}")   # center aligned
print(f"{'right':>20}")    # right aligned
```

### input()

```python
# input() always returns a string!
name = input("Enter your name: ")
print(f"Hello, {name}!")

# To get a number, convert the result
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
```

```mermaid
flowchart LR
    A["input('Enter age: ')"] --> B["User types: 25"]
    B --> C["Returns: '25'<br/>(string!)"]
    C --> D["int('25')"]
    D --> E["25<br/>(integer)"]

    style C fill:#f0ad4e,color:#fff
    style E fill:#5cb85c,color:#fff
```

---

## 10. Type Conversion

```mermaid
graph TD
    subgraph "Type Conversion Functions"
        A["int()"] --- A1["Converts to integer<br/>int('42') -> 42<br/>int(3.9) -> 3<br/>int(True) -> 1"]
        B["float()"] --- B1["Converts to float<br/>float('3.14') -> 3.14<br/>float(42) -> 42.0"]
        C["str()"] --- C1["Converts to string<br/>str(42) -> '42'<br/>str(3.14) -> '3.14'<br/>str(True) -> 'True'"]
        D["bool()"] --- D1["Converts to boolean<br/>bool(1) -> True<br/>bool(0) -> False<br/>bool('') -> False<br/>bool('hi') -> True"]
    end

    style A fill:#5cb85c,color:#fff
    style B fill:#4a90d9,color:#fff
    style C fill:#f0ad4e,color:#fff
    style D fill:#d9534f,color:#fff
```

```python
# int() - converts to integer
int("42")       # 42
int(3.9)        # 3  (truncates, does NOT round!)
int(3.1)        # 3
int(True)       # 1
int(False)      # 0
# int("hello")  # ValueError! Can't convert non-numeric string

# float() - converts to float
float("3.14")   # 3.14
float(42)       # 42.0
float("inf")    # inf (infinity)

# str() - converts to string
str(42)         # '42'
str(3.14)       # '3.14'
str(True)       # 'True'
str(None)       # 'None'

# bool() - converts to boolean
# "Falsy" values (become False):
bool(0)         # False
bool(0.0)       # False
bool("")        # False  (empty string)
bool(None)      # False
bool([])        # False  (empty list)

# "Truthy" values (become True):
bool(1)         # True  (any non-zero number)
bool(-5)        # True
bool("hello")   # True  (any non-empty string)
bool(" ")       # True  (space is not empty!)
```

### Truthy and Falsy Cheat Sheet

```mermaid
graph TD
    subgraph "Falsy values (bool returns False)"
        F1["0, 0.0"]
        F2["'' (empty string)"]
        F3["None"]
        F4["[] {} () (empty collections)"]
        F5["False"]
    end

    subgraph "Truthy values (bool returns True)"
        T1["Any non-zero number"]
        T2["Any non-empty string"]
        T3["Non-empty collections"]
        T4["True"]
    end

    style F1 fill:#d9534f,color:#fff
    style F2 fill:#d9534f,color:#fff
    style F3 fill:#d9534f,color:#fff
    style F4 fill:#d9534f,color:#fff
    style F5 fill:#d9534f,color:#fff
    style T1 fill:#5cb85c,color:#fff
    style T2 fill:#5cb85c,color:#fff
    style T3 fill:#5cb85c,color:#fff
    style T4 fill:#5cb85c,color:#fff
```

---

## Quick Reference Summary

| Concept      | Syntax                       | Example                     |
| ------------ | ---------------------------- | --------------------------- |
| Variable     | `name = value`               | `x = 10`                    |
| Type check   | `type(value)`                | `type(42)` -> `int`         |
| Arithmetic   | `+ - * / // % **`            | `10 // 3` -> `3`            |
| Comparison   | `== != < > <= >=`            | `5 > 3` -> `True`           |
| Logical      | `and or not`                 | `True and False` -> `False` |
| String index | `s[i]`                       | `"hi"[0]` -> `"h"`          |
| String slice | `s[start:stop:step]`         | `"hello"[1:4]` -> `"ell"`   |
| f-string     | `f"text {expr}"`             | `f"age: {25}"`              |
| if/elif/else | `if cond:`                   | See section 7               |
| for loop     | `for x in iterable:`         | `for i in range(5):`        |
| while loop   | `while cond:`                | `while x < 10:`             |
| Type convert | `int() float() str() bool()` | `int("42")` -> `42`         |
