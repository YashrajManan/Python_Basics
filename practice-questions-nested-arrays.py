#question 1 
a = [[1, 2], [3, [4, 5]]]
print(a[1][1][0])

#question 2
a = [[1]*2]*2
a[0][0] = 5
print(a)

#question 3
a = [[1, [2, 3]], [4, 5]]
print(a[0][1][1])

#question 4
a = (("x", "y"), ("z",))
print("y" in a[0])

#question 5
d = {'a': {'b': 2}}
print(d['a']['b'])

#question 6
d = {'p': {'q': 5}}
d['p']['q'] += 1
print(d)

#question 7
d = {'outer': {'inner': {'value': 10}}}
print(d['outer']['inner']['value'])

#question 8
d = {'a': {'b': {'c': 3}}}
print(list(d['a']['b'].keys()))

#question 9
a = {'data': [1, (2, 3)]}
print(a['data'][1][0])

#question 10
a = ([1, 2], {'a': 3})
a[1]['b'] = 4
print(a)

#question 11
a = [{'a': [1, 2]}, {'b': (3, 4)}]
print(a[1]['b'][0])

#question 12
a = {'data': ({'x': 1}, {'y': [2, 3]})}
print(a['data'][1]['y'][1])

#question 13
a = {'a': [1, {'b': (2, 3)}]}
print(a['a'][1]['b'][1])

#question 14
a = {'a': {'b': [{'c': 1}, {'d': 2}]}}
print(a['a']['b'][0]['c'])

#question 15
a = [(1, {'a': 10}), (2, {'b': 20})]
print(a[1][1]['b'])

#question 16
a = [[{'a': 1}], [{'b': 2}]]
print(a[1][0]['b'])

#question 17
a = {'outer': [{'inner': (1, {'val': 2})}]}
print(a['outer'][0]['inner'][1]['val'])

#question 18
a = {'a': [{'b': {'c': (1, 2)}}]}
print(a['a'][0]['b']['c'][1])

#question 19
a = [{'a': {1, 2}}, {'b': {3, 4}}]
print(4 in a[1]['b'])

#question 20
a = [{'a': {'b': {'c': [1, 2]}}}]
print(a[0]['a']['b']['c'][0])

#question 21
a = {'x': (1, [2, {'y': 3}])}
print(a['x'][1][1]['y'])

#question 22
a = ({'x': [1, 2]}, {'y': (3, {'z': 4})})
print(a[1]['y'][1]['z'])



