# Python Study

- Cpython, a primary interpreter of Python is written in C
## Loops
while & for loops
### While loops
_In C_
```
int counter = 0;
    
    while (counter < 100)
    {
        printf("%d\n", counter);
        counter++;
    }
    return (0);
```

_In Python_
```
counter = 0;
while counter < 100
    print(counter)
    counter += 1
```

### For loops
_In C_
```
for (int counter = 0; counter < 100; counter++)
{
    printf("%d\n",counter);
}
return (0);
```

_In Python_
```
for counter in range (10):
    print(counter)

print("counting in 2's now")
for counter in range (0, 10, 2):
    print(counter)
```
## Lists
### List comprehension
```
nums = [x for x in range (10)]
print(nums)
```
check [list_for.py](lists/list_for.py)

- ### Tacking on to an existing list
1. Appending
```
nums = [1, 2, 3, 4]
nums.append(5)
```
check [appending.py](lists/appending.py)

2. Inserting
```
nums = [1, 2, 3 ,4]
nums.insert(4, 5)
```
check [inserting.py](lists/inserting.py)

3. Attaching a list at the end of another
```
nums = [1, 2, 3, 4, 5]
nums.insert(4,5)
```
check [splicing.py](lists/splicing.py)

## Tuples
check [ucl_winner.py](tuples_n_dicts/ucl_winner.py)

## Dictionaries
check [pizzas.py](tuples_n_dicts/pizzas.py)

## Functions
- use `def`

check [square.py](functions/square.py)

## Objects
Python is an object-oriented programming lang.
- Objects have properties and methods(functions inherent to the object).
- methods are defined inside the object
- objects aren't passed into a function;

~~`function(object)`~~

rather methods are called on objects

`object.method()`
- the `class` keyword is used to define a type of object
- Classes require an initialization function
- in defining each method of an object, `self` should be its first parameter.

### Example
```
class Student():

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def changeID(self, id):
        self.id = id

    def print(self):
        print("{} - {}".format(self.name, self.id))


jane = Student("Jane", 10)
jane.print()
jane.changeID(11)
jane.print()
```
check [change_id](functions/change_id.py)

## Additional info
You can make your programs more like C programs when they execute by adding a `shebang` to the top of your Python files.
`#!/usr/bin/env python3`
then we can run using `./<filename>`

*Learning With CS50x*