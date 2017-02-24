# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

> Both lists and tuples are ordered, i.e., their elements always occur in the same order, so they can be indexed by a number. Both lists and tuples can also be concatenated, multiplied, we can determine their length, check whether they contain a certain element and loop over them. They differ in the sense that lists are mutable while tuples are immutable, i.e., you cannot udpate tuples or delete elements from them, while this is possible in lists. Lists and tuples also have different syntax: lists are indicated with square brackets, while tuples are indicated by parentheses.
> Only tuples can serve as a key in a python dictionary, since keys need to be immutable.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

> Both lists and sets contain values only. Lists are ordered, sets are not (like dictionaries), hence sets cannot be indexed or sliced, while lists can. Sets cannot contain duplicates, lists can. You can perform seet-theoretical formulas on sets, but not on lists. For instance, you can find the intersetction fo two sets, or figure out whether a set of elements is a subset of another set.
> Example of list:
> ```python
> li = ['cat', 'dog', 'icecream', 'dog']
> print li[1] #will print 'dog', the element with index 1.
> ```
> Example of set:
> ```python
> s1 = {1, 2,3}
> s2 = set(li)
> print s2 #will print set(['icecream', 'dog', 'cat']), the second occurrence of dog is not there because duplicates are not allowed. The order may vary because sets are unordered.
> print s2[2] # will raise TypeError, since sets do not support indexing
> ```
> It's faster to find an element in a set than in a list, because python lists are implemented as dynamic arrays and sets are implemented as hash tables. Hash tables are faster for lookup.

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

> The `lambda` function or operator in oython can be used to create anonymous functions, i.e., functions that have no name (contrary to the functions created with `def`). It is generally used for short functions that are used only once. For more complex functions or functions that are needed repeatedly, `def`is preferred. 
> The syntax of `lambda` is as follows:
> ```python
> lambda arg_iterable: expression
> ```
> When compared to a regular function, the arg_iterable is what goes in the brackets after the name of the function, and the expression is what is returned:
> ```python
> def f(arg_iterable) : return expression
> ```
> The `lambda` function is very often in functions that require a function as an argument, such as `filter()`, which filters lists, `map()`which maps lists to another list and `reduce()`, which reduces lists (like the `sum()`function).
> These functions take two arguments: a function and a list. An example:
> ```python
> li = range(1, 45)
> print filter(lambda x: x%3 == 0, li)
> ```
> This piece of code will print a list of all numbers in the range 1-45 (so numbers from 1 upto but no including 45) that are divisable by 3.
> Another example in which `lambda` is used in the `key` argument of `sorted`:
> ```python
> animals = ['cat', 'dog', 'zebra', 'elephant', 'cow']
> print sorted(animals, key=lambda x: x[-1])
> ```
> The code above will print the list of animals sorted by the last letter. Another example:
> ```python
> addresses = [('Buffelstraat', 1, 5600, 'Steenokkerzeel'), ('Meibloemstraat', 83, 9000, 'Gent'), ('Oscar de Reusestraat', 53, 9050, 'Sint-Amandsberg')]
> print sorted(addresses, key=lambda x: x[3])
> ```
> This prints out the list of addresses sorted by city.


---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

> List comprehensions is a syntax to create a list based on a list without having to write a loop. An example:
> ```python
> vals = range(1,45)
> mean = sum(vals)/len(vals)
> # for a list of values, returns a list of the squared difference of each value minus the mean of the values (calculated elsewhere)
> squared_differences = [(i-mean)**2 for i in vals]
> # equivalent to:
> squared_differences = map(lambda i: (i-mean)**2, vals)
> 
> animals = ['crocodile', 'lion', 'tiger', 'cat', 'cobra', 'duck', 'bat']
> # gives you the list of animal names that contain an 'a'
> only_a = [animal for animal in animals if 'a' in animal]
> # equivalent to:
> only_a = filter(lambda x: 'a' in x, animals)
```

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

> ```python
> import datetime
> date_start = '01-02-2013'
> date_stop = '07-28-2015'
> new_start = datetime.datetime.strptime(date_start, "%m-%d-%Y")
> new_end = datetime.datetime.strptime(date_stop, "%m-%d-%Y")
> print new_end - new_start
> ```

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

> ```python
> import datetime
> date_start = '12312013'  
> date_stop = '05282015'
> new_start = datetime.datetime.strptime(date_start, "%m%d%Y")
> new_end = datetime.datetime.strptime(date_stop, "%m%d%Y")
> print new_end - new_start
> ```

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

> ```python
> import datetime
> date_start = '15-Jan-1994'
> date_stop = '14-Jul-2015'
> new_start = datetime.datetime.strptime(date_start, "%d-%b-%Y")
> new_end = datetime.datetime.strptime(date_stop, "%d-%b-%Y")
> print new_end - new_start
> ``

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





