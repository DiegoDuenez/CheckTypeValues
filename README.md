# pyvar

Python library to check the value of a variable.

This library is based on functions that will detect the value they receive and return a true or false depending on whether the expected value is correct.

## Installation 🛠

```
git clone https://github.com/DiegoDuenez/pyvar.git
```

## Import 📦

Import the file in your python code

<pre>import pyvar</pre>

## Getting Started 🚀

Below, you will see an example of the use of this library.

### Functions

### How do they work? 

All functions (so far) are made up of two parameters.

The first parameter is the **value** and the second is the **warning** (optional).

**value** is the variable or value that will be passed to the function to identify its data type.

**warning** is an optional Boolean parameter, by default its value is true and it is not necessary to specify it when instantiating the function.

Unnecessary way:

```

v = 5

pyvar.isInt(5, True) ❌

```

What this parameter allows is that when it is true, a message will appear in the console like this:

```

v = "hello!"

pyvar.isInt(v)

```

```

* * * The values hello! is not an Int * * *

```

To prevent these messages from getting out, all you have to do is put **warning** as False and the function will continue to work the same but nothing will appear on the console.

isInt()

- This function checks if the given value is an Integer.


```

v = 5

pyvar.isInt(v)

```

isFloat()

- This function checks if the given values is a Float. 

```

v = 5.1

pyvar.isFloat(v)

```


isString()

- This function checks if the given values is an String.

```

v = "hello!"

pyvar.isString(v)

```

isBool()

- This function checks if the given values is a Boolean.

```

v = True

pyvar.isBool(v)

```

isNumericBool()

- This function checks if the given values is a Numeric boolean (0 or 1)

```

v = 1

pyvar.isBool(v)

```

isList()

- This function checks if the given values is a List.

```

v = ["diego", "dueñez"]

pyvar.isList(v)

```

isTuple()

- This function checks if the given values is a Tuple.

```

v = ("diego", "dueñez")

pyvar.isTuple(v)

```

isDict()

- This function checks if the given values is a Dictionary.

```

v = {"name":"diego", "lastname":"dueñez"}

pyvar.isDict(v)

```

isComplex()

- This function checks if the given values is a Complex.

```

v = complex(1,4)

pyvar.isComplex(v)

```
