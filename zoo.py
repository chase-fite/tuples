zoo = ('lion', 'tiger', 'bear', 'panther', 'cheetah', 'panda', 'giraffe', 'hyena', 'wolf', 'otter')

print(zoo.index('panther'))

print(('tiger' in zoo))

(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10) = zoo

for var in zoo:
    print(var)

zoo = list(zoo)

zoo.extend(['kangaroo', 'sloth', 'eagle'])

print(zoo)

zoo = tuple(zoo)

print(zoo)