# Practice: Solid Student

Define a Python class named Student. This class will have 5 properties.

1. First name (string)
1. Last name (string)
1. Age (integer)
1. Cohort number (integer)
1. Full name (read-only string)
- Define getters for all properties.
- Define a setter for all but the read only property.
- Ensure that only the appropriate value can be assigned to each.
- The full name property should return first name and last name separated by a space. It's value cannot be set.


# Practice: Convert Student Object to a String
Use the __str__ and __repr__ magic methods on your class to specify what an object's string representation should be. It's just like the toString() method in JavaScript.

If you print a Student object. The output would look something like below.

```
mike = Student()
mike.first_name = "Mike"
mike.last_name = "Ellis"
mike.age = 35
mike.cohort_number = 39

print(mike)
<__main__.Student object at 0x107133f60>
```

But if you specify exactly what string should be returned from __str__ or __repr__, that will print out instead. If you implement the following method on your class...

```
class Student:

    def __str__(self):
        return f"{self.full_name}"
```
then the output will change

```
print(mike)
Mike Ellis
```

Change your class so that any objects created from it will be rerpesented as strings in the following format.

```
Mike Ellis is 35 years old and is in cohort 39
```