
# Update Values in Dictionaries and Lists Assignment


x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

# ---------------------------------------------------------

# Change the value 10 in x to 15.
x[1][0] = 15
print(x)

# Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = 'Bryant'
print(students)

# In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

# Change the value 20 in z to 30
z[0]['y'] = 30
print(z)

# Iterate Through a List of Dictionaries

def iterateDictionary(some_list):
    for ind in range(0, len(some_list)):
        pass
        for key, value in some_list[ind].items():
            print(f" {key} - {value},")

iterateDictionary(students)

def iterateDictionary2(key_name, some_list):
    for x in some_list:
     print(x[key_name])

iterateDictionary2('first_name', students)

# Iterate Through a Dictionary with List Values

def printInfo(some_dict):
    for x, y in some_dict.items():
        print(str(len(y)) + ' ' + x.title())
        for index in range(0, len(y)):
            print(y[index])

# This was a hard one!! Took a lot of surfing the internet to figure out how to structure this(and yes, i still peaked at the solution video to help me understand the concept. I hope thats okay)

printInfo(dojo)