import pandas as pd

with open("faculty.csv") as f:
    data = pd.read_csv(f)
    data = data.rename(columns=lambda x: x.strip())
    degrees = data['degree'].str.strip()
    degrees = degrees.str.replace('\.', '')
    df = degrees.str.split(' ', expand=True)
    values = df.apply(pd.Series.value_counts)
    sum_degrees = values.sum(axis = 1)
    print 'There are '+str(len(sum_degrees)) + ' different degrees.\n'
    print sum_degrees

    titles = data['title'].str.strip()
    df = titles.str.split(' ', expand=True)
    sum_titles = df[0].value_counts()
    print '\nThere are '+str(len(sum_titles)) + ' different titles.\n'
    for title, total in sum_titles.iteritems():
        if title == 'Professor':
            print 'There are ' + str(int(total)) +' ' +title+'s of Biostatistics.'
        else:
            print 'There are ' + str(int(total)) +' ' +title+' Professors of Biostatistics.'

    emails = data['email'].str.strip()
    print list(emails)

    domains = emails.str.split('@', expand = True)
    print 'There are ' + str(len(domains[1].unique())) + ' domains :' + str(domains[1].unique())

# without pandas

import csv
import re

with open('faculty.csv') as f:
    reader = csv.reader(f)
    degrees = []
    for row in reader:
        degrees.append(row[1])
    degrees = degrees[1:]
    stripped_degrees = map(str.strip, degrees)
    no_dots = [s.replace('.', '') for s in stripped_degrees]
    totals = {}
    for degree in no_dots:
        if degree in totals:
            totals[degree]+=1
        else:
            totals[degree]=1
    print totals