
  
len_of_strings = lambda names: [len(x) for x in names]

names = ['Aqwe', 'dfs', 'hbkjhbkjh']
lengths = len_of_strings(names)
print(lengths)

for e in lengths:
    if e%2==1:
        print( 'Boy')