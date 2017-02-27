# Advanced Python    

### Regular Expressions, Dictionary, Writing to CSV File  

This question has multiple parts, and will take **20+ hours** to complete, depending on your python proficiency level.  Knowing these skills will be extremely beneficial during the first few weeks of the bootcamp.

For Part 1, use of regular expressions is optional.  Work can be completed using a programming approach of your preference. 

---

The data file represents the [Biostats Faculty List at University of Pennsylvania](http://www.med.upenn.edu/cceb/biostat/faculty.shtml)

This data is available in this file:  [faculty.csv](python/faculty.csv)

--- 

### Part I - Regular Expressions  


####Q1. Find how many different degrees there are, and their frequencies: Ex:  PhD, ScD, MD, MPH, BSEd, MS, JD, etc.

>There are 9 different degrees:
> Degree | Total
> ---|---
> 0|1
> BSEd |1
> JD   |    1
> MA    |   1
> MD     |  1
> MPH     | 2
> MS     |  2
> PhD   |  31
> ScD   |   6



#### Q2. Find how many different titles there are, and their frequencies:  Ex:  Assistant Professor, Professor

>There are 3 different titles: 
> Title|Total
> ---|---
> Professor of biostatistics|13
> Associate Professor of biostatistics|12
> Assistant Professor of biostatistics|12


#### Q3. Search for email addresses and put them in a list.  Print the list of email addresses.

>['bellamys@mail.med.upenn.edu', 'warren@upenn.edu', 'bryanma@upenn.edu', 'jinboche@upenn.edu', 'sellenbe@upenn.edu', 'jellenbe@mail.med.upenn.edu', 'ruifeng@upenn.edu', 'bcfrench@mail.med.upenn.edu', 'pgimotty@upenn.edu', 'wguo@mail.med.upenn.edu', 'hsu9@mail.med.upenn.edu', 'rhubb@mail.med.upenn.edu', 'whwang@mail.med.upenn.edu', 'mjoffe@mail.med.upenn.edu', 'jrlandis@mail.med.upenn.edu', 'liy3@email.chop.edu', 'mingyao@mail.med.upenn.edu', 'hongzhe@upenn.edu', 'rlocalio@upenn.edu', 'nanditam@mail.med.upenn.edu', 'knashawn@mail.med.upenn.edu', 'propert@mail.med.upenn.edu', 'mputt@mail.med.upenn.edu', 'sratclif@upenn.edu', 'michross@upenn.edu', 'jaroy@mail.med.upenn.edu', 'msammel@cceb.med.upenn.edu', 'shawp@upenn.edu', 'rshi@mail.med.upenn.edu', 'hshou@mail.med.upenn.edu', 'jshults@mail.med.upenn.edu', 'alisaste@mail.med.upenn.edu', 'atroxel@mail.med.upenn.edu', 'rxiao@mail.med.upenn.edu', 'sxie@mail.med.upenn.edu', 'dxie@upenn.edu', 'weiyang@mail.med.upenn.edu']


#### Q4. Find how many different email domains there are (Ex:  mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.).  Print the list of unique email domains.

>There are 4 domains :['mail.med.upenn.edu' 'upenn.edu' 'email.chop.edu' 'cceb.med.upenn.edu']

Place your code in this file: [advanced_python_regex.py](python/advanced_python_regex.py)

---

### Part II - Write to CSV File

#### Q5.  Write email addresses from Part I to csv file

Place your code in this file: [advanced_python_csv.py](python/advanced_python_csv.py)

The emails.csv file you create should be added and committed to your forked repository.

Your file, emails.csv, will look like this:
```
bellamys@mail.med.upenn.edu
warren@upenn.edu
bryanma@upenn.edu
```

---

### Part III - Dictionary

#### Q6.  Create a dictionary in the below format:
```
faculty_dict = { 'Ellenberg': [['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']],
              'Li': [['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']]}
```
Print the first 3 key and value pairs of the dictionary:

> It doesn't make much sense to speak of 'the first 3 key and value pairs of the dictionary', because dictionaries are not ordered. Anyway, three random key value pairs:
```python
import pandas as pd
from collections import defaultdict
faculty_dict = defaultdict(list)

with open("faculty.csv") as f:
    data = pd.read_csv(f)
    data = data.rename(columns=lambda x: x.strip())
    df = data['name'].str.rsplit(' ', expand=True, n=1)
    data = data.join(df[1])
    data = data.ix[:, ['degree', 'title', 'email', 1]]
    data[2] = data[['degree', 'title', 'email']].values.tolist()
    data_needed = data[[1,2]]
    for row in data_needed.itertuples():
        faculty_dict[row[1]].append(list(row[2]))
    print {k: faculty_dict[k] for k in faculty_dict.keys()[:3]}
```

> {'Putt': [[' PhD ScD', 'Professor of Biostatistics', 'mputt@mail.med.upenn.edu']], 'Feng': [[' Ph.D', 'Assistant Professor of Biostatistics', 'ruifeng@upenn.edu']], 'Bilker': [['Ph.D.', 'Professor of Biostatistics', 'warren@upenn.edu']]}

#### Q7.  The previous dictionary does not have the best design for keys.  Create a new dictionary with keys as:

```
professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'], ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu'] }
```

Print the first 3 key and value pairs of the dictionary:

> {('Hongzhe', 'Li'): [' Ph.D', 'Professor of Biostatistics', 'hongzhe@upenn.edu'], ('Justine', 'Shults'): [' Ph.D.', 'Professor of Biostatistics', 'jshults@mail.med.upenn.edu'], ('Yimei', 'Li'): [' Ph.D.', 'Assistant Professor of Biostatistics', 'liy3@email.chop.edu']}

```python
with open("faculty.csv") as f:
    data = pd.read_csv(f)
    data = data.rename(columns=lambda x: x.strip())
    df = data['name'].str.rsplit(' ', expand=True, n=1)
    data = data.join(df[1])
    data = data.ix[:, ['degree', 'title', 'email', 1]]
    data[2] = data[['degree', 'title', 'email']].values.tolist()
    data_needed = data[[1,2]]
    for row in data_needed.itertuples():
        faculty_dict[row[1]].append(list(row[2]))
    print {k: faculty_dict[k] for k in faculty_dict.keys()[:3]}
```

#### Q8.  It looks like the current dictionary is printing by first name.  Print out the dictionary key value pairs based on alphabetical orders of the last name of the professors

>{('Landis', 'J.'): [' B.S.Ed. M.S. Ph.D.', 'Professor of Biostatistics', 'jrlandis@mail.med.upenn.edu'], ('Joffe', 'Marshall'): [' MD MPH Ph.D', 'Professor of Biostatistics', 'mjoffe@mail.med.upenn.edu'], ('Propert', 'Kathleen'): [' Sc.D.', 'Professor of Biostatistics', 'propert@mail.med.upenn.edu']}

```python
with open("faculty.csv") as f:
    data = pd.read_csv(f)
    data = data.rename(columns=lambda x: x.strip())
    df = data['name'].str.rsplit(' ')
    names = []
    professor_dict = defaultdict(list)
    for row in df:
        if len(row) == 3:
            row = row[::2]
            names.append(row[::-1])
        else:
            names.append(row[::-1])
    tuple_names = [tuple(name) for name in names]
    data['name_clean'] = tuple_names
    data = data.ix[:, ['degree', 'title', 'email', 'name_clean']]
    data['info'] = data[['degree', 'title', 'email']].values.tolist()
    data_needed = data[['name_clean','info']]
    for row in data_needed.itertuples():
        professor_dict[row[1]] = (row[2])
    print {k: professor_dict[k] for k in professor_dict.keys()[:3]}
```

Place your code in this file: [advanced_python_dict.py](python/advanced_python_dict.py)

--- 

If you're all done and looking for an extra challenge, then try the below problem:  

### [Markov](python/markov.py) (Optional)

