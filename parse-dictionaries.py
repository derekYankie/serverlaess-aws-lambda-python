
#  Dictionary Exercises: Iterate with loops and List comprehension

# Create dictionary
mydict = {
  "course": "python",
  "fee": 2500,
  "duration": "120 days"
}
print(mydict)
## Output:
{'course': 'python', 'fee': 2500, 'duration': '120 days'}


# Loop through by Dict Keys
technology={"Course":"python","Fee":2500,"Duration":"120 days"}
for x in technology:
    print(x)

## Output:
Course
Fee
Duration


# Example 1: Loop through by Dict Keys
technology={"Course":"python","Fee":2500,"Duration":"120 days"}
for x in technology:
    print(x)

# Example 2: Loop through by Key and Value
technology={"Course":"python","Fee":2500,"Duration":"120 days"}
for key, value in technology.items():
    print(key, value)

## Output:
Course python
Fee 2500
Duration 120 days

# Example 3: Use key to get the Value
technology={"Course":"python","Fee":2500,"Duration":"120 days"}
for key in technology:
    print(key,technology[key])


## Output:
Course python
Fee 2500
Duration 120 days


# Example 4: Use dict.keys() & dict.values()
technology={"Course":"Python","Fee":2500,"Duration":"120 days"}
for key in technology.keys():
    print('Key: '+ key)
for value in technology.values():
    print('Value: '+value)

## Output:
Key: Course
Key: Fee
Key: Duration
Value: python
Value: 2500
Value: 120 days

# Using for loop through dictionary to get index
mydict = {"course": 1,"fee": 2,"duration": 3}    
for i in mydict:
    print(i,mydict[i])

# Output:
course 1
fee 2
duration 3


# Lambda Syntax
lambda arguments: expression
# Using lambda function to iterate over a dictionary
my_squares = {2:4,3:9,4:16,5:25}  
my_cubes = list(map(lambda key: key**3, my_squares.keys()))  
print(my_cubes)
#Outputs
[8, 27, 64, 125]


# Syntax of the dictionary comprehension
{key: value for variable in iterable(if conditional)}
# Iterate dictionary using dictionary comprehension
mydict = {"course": "python","fee": 2500,"duration": "45 days"}
newdict = {key: value for (key, value) in mydict.items()}
print(newdict)
# Outputs:
{'course': 'python', 'fee': 2500, 'duration': '45 days'}


# Return a View object After Modification of Dictionary
courses = { 1:'java', 2:'python', 3:'pandas',4:'sparks'}
dict_view=courses.items()
print("original courses:",dict_view)

# Output: 
original courses: dict_items([(1, 'Chemistry'), (2, 'Python'), (3, 'Economics'), (4, 'Art')])

courses[5]='NumPy'
print("new courses:",dict_view)
# Output:
new courses: dict_items([(1, 'Chemistry'), (2, 'Python'), (3, 'Economics'), (4, 'Art'), (5, 'Marketing')])


# Iterate 2-D array and get indexes & values
for index, value in np.ndenumerate(arr):
  print(index, value)

# Output:
(0,) 0
(1,) 1
(2,) 2
(3,) 3
(4,) 4
(5,) 5
(6,) 6
(7,) 7
(8,) 8
(9,) 9
(10,) 10
(11,) 11


# Create dictionary
my_dict = {'course':'python','fee':2500,'duration':'120days', 'discount':200}
print(my_dict)
# Get the keys of dictionary as a list 

# my_dict.keys()
print(my_dict.keys())

# type
print(type(my_dict.keys()))

# Convert to list
list_of_keys = list(my_dict.keys())
print(keys)

# Output: Print Keys my_dict.keys()
my_dict.keys() ==> (['course', 'fee', 'duration', 'discount'])
# Output: Print list of Keys
list_of_keys['course', 'fee', 'duration', 'discount']