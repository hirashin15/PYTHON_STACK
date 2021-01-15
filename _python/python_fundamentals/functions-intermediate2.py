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

# 1.1 Change 10 in x to 15
x[1][0]=15

# 1.2 Change last name of first student from Jordan to Bryant
students[0]["last_name"]= "Bryant"

# 1.3 Change Messi to Andres in sports directory
sports_directory["soccer"][0]= "Andres"

# 1.4 Change 20 in z to 30
z[0]["y"]=30

# 2 
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
  for item in some_list:
    concat = ""
    for first, last in item.items():
      concat += f"{first} - {last}, "
    print(concat)

# 3 
def iterateDictionary2(key_name, some_list):
  for item in some_list:
    print(item["last_name"])

# 4
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
  for key in some_dict:
    length = len(some_dict[key])
    print(f"{length} {key.upper()}")
    for item in some_dict[key]:
      print(item)

printInfo(dojo)
  