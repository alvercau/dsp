import pandas as pd
from collections import defaultdict

faculty_dict = defaultdict(list)

# Q6
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


# Q7
with open("faculty.csv") as f:
    data = pd.read_csv(f)
    data = data.rename(columns=lambda x: x.strip())
    df = data['name'].str.rsplit(' ')
    names = []
    professor_dict = defaultdict(list)
    for row in df:
        if len(row) == 3:
            row = row[::2]
            names.append(row)
        else:
            names.append(row)
    tuple_names = [tuple(name) for name in names]
    data['name_clean'] = tuple_names
    data = data.ix[:, ['degree', 'title', 'email', 'name_clean']]
    data['info'] = data[['degree', 'title', 'email']].values.tolist()
    data_needed = data[['name_clean','info']]
    for row in data_needed.itertuples():
        professor_dict[row[1]] = (row[2])
    print {k: professor_dict[k] for k in professor_dict.keys()[:3]}

# Q8
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