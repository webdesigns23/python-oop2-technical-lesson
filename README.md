# Technical Lesson: Object Oriented Programming (OOP)- Part 2

In this lesson, we will explore how to apply more complex features to our models such as properties. 

## The Scenario

Imagine you are working for the same veterinarian clinic you were working on previously. You already have a dog model but you need to add several features to it. You will be adding and updating several properties.

* Update age property to use decorator
* Adding a new instance property called vets
* Updating checkups to be a list of dictionaries
* New methods to add a new checkup

## Resources & Tools
* [GitHub Repo](https://github.com/learn-co-curriculum/python-oop2-technical-lesson)

## Instructions

### Set Up

Before we begin coding, let's complete the initial setup for this lesson: 

* Fork and Clone
  * For this lesson, you will need the following GitHub Repo:
    * Go to the provided GitHub repository link.
    * Fork the repository to your GitHub account.
    * Clone the forked repository to your local machine.
* Open and Run File
  * Open the project in VSCode.
  * Run npm install to install all necessary dependencies.

### Task 1: Define the Problem

They would like for you to update an existing dog model. You will be tasked with:

* Update age property to use decorator
* Adding a new instance property called vets
* Updating checkups to be a list of dictionaries
* New methods to add a new checkup and find a checkup

### Task 2: Determine the Design

Dog attributes
* Breed
* Name
* Checkups
* Age
* Vets

Determine necessary methods
* add_checkup
* find_checkup

### Task 3: Develop, Test, and Refine the Code

#### Step 1: Create a Feature Branch

```bash
git checkout -b updated_dog_model
```

#### Step 2: Analyze and Update the Model

As we are working on this model the first step is to analyze the model and see what we have. In this case we have an existing model with 4 attributes and a property. Matching it to what we need to do we can see that we need to remove the attribute of last_checkup and replace it with checkups. We also need to add another attribute vets
<br />
All code changes will happen in lib/dog.py:

```python
class Dog:
def __init__(self, name, breed, age):
	self.name = name
	self.breed = breed
	self.age = age
	self.vets = []
	self.checkups = []
def get_age(self):
	return self._age
def set_age(self,value):
	if type(value) is int and 0 <= value:
		self._age = value
	else:
		print("Not valid age")
age = property(get_age,set_age)
```

We set up vets and checkups as well as remove last_checkup from the init, in this case we shall initialize each as an empty array. The attribute vets shall just be an array of strings (the vets name) and checkups will be an array of dictionaries. Each dictionary in this array will include the vets name, the date of the checkup, and any notes.  

#### Step 3: Apply property decorator

We will now change our getter and setter to use the property decorator. This will help clean up our code.

```python
class Dog:
def __init__(self, name, breed, age):
	self.name = name
	self.breed = breed
	self.age = age
	self.vets = []
	self.checkups = []

@property
def age(self):
	return self._age
@age.setter
def age(self,value):
	if type(value) is int and 0 <= value:
		self._age = value
	else:
		raise ValueError("Not valid age")	
```

When applying the decorator we use @property on top of the getter which we now name based on what property we are adding, in this case age. We then do the same using age.setter to apply the setter to define the setter and getter. We also change the else within our setter to raise a value error as we want our program to return an error the moment that an age is invalid.

#### Step 4: Create methods - add_checkup

Now we will begin working with our collections. We know what our checkups array should look like and we also know we want to update vets when we add a checkup so lets do so.

```python
class Dog:
def __init__(self, name, breed, age):
	self.name = name
	self.breed = breed
	self.age = age
	self.vets = []
	self.checkups = []

@property
def age(self):
	return self._age
@age.setter
def age(self,value):
	if type(value) is int and 0 <= value:
		self._age = value
	else:
		raise ValueError("Not valid age")	

def add_checkup(self, vet, date, notes):
	if vet not in self.vets:
		self.vets.append(vet)
	new_checkup = {
		"vet": vet,
		"date": date,
		"notes": notes
	}
	self.checkups.append(new_checkup)
```

When adding this new method we need to think of when and what we are adding. In the case of every single checkup we want to add it to checkups to be logged, however for updating vets we only want to update vets in the case that the vet is not currently in the array. 

#### Step 5: Create methods - find_checkup

For this method we must think of the user experience. As a user there are many things I may want to use to find a checkup, we will focus on one however. We will have the find checkup method find a checkup by date.

```python
class Dog:
def __init__(self, name, breed, age):
	self.name = name
	self.breed = breed
	self.age = age
	self.vets = []
	self.checkups = []

@property
def age(self):
	return self._age
@age.setter
def age(self,value):
	if type(value) is int and 0 <= value:
		self._age = value
	else:
		raise ValueError("Not valid age")	

def add_checkup(self, vet, date, notes):
	if vet not in self.vets:
		self.vets.append(vet)
	new_checkup = {
		"vet": vet,
		"date": date,
		"notes": notes
	}
	self.checkups.append(new_checkup)

def find_checkup(self, date):
	for checkup in self.checkups:
		if checkup["dates"] == date:
			print(f"Checkup on {date} by {checkup['vet']}: {checkup['notes']}")
			return
	print(f"No checkup found on {date}")
```

For our find checkup logic we will loop through the existing checkups. If the date passed in matches the date of the checkup we will print the details and then return. This return is important as it will exit out of the method so that the no checkup notice will not be printed. If however we never find the date we will never hit the return and thus we will reach the end of the for loop and print a message that no checkups were found.

#### Step 6: Testing Methods

For testing these methods we need to think about what cases we want to test. We want to see if the two collection attributes are updated upon using add_checkup as well as a successful and unsuccessful case for find_checkup.

```python
class Dog:
def __init__(self, name, breed, age):
	self.name = name
	self.breed = breed
	self.age = age
	self.vets = []
	self.checkups = []

@property
def age(self):
	return self._age
@age.setter
def age(self,value):
	if type(value) is int and 0 <= value:
		self._age = value
	else:
		raise ValueError("Not valid age")	

def add_checkup(self, vet, date, notes):
	if vet not in self.vets:
		self.vets.append(vet)
	new_checkup = {
		"vet": vet,
		"date": date,
		"notes": notes
	}
	self.checkups.append(new_checkup)

def find_checkup(self, date):
	for checkup in self.checkups:
		if checkup["dates"] == date:
			print(f"Checkup on {date} by {checkup['vet']}: {checkup['notes']}")
			return
	print(f"No checkup found on {date}")

fido = Dog(
   name = "Fido",
   age = 3, 
   breed = "Golden Retriever"
   )
fido.add_checkup("Doolittle", "02/20/22","Good health!")
print(fido.vets)
print(fido.checkups)
fido.find_checkup("02/20/22")
fido.find_checkup("03/22/24")
```

In this case we build an instance of the Dog class and test out add_checkup. After calling that method we print vets and checkups of fido and should see an updated array for each. Then we test find_checkup twice, the first should give us the success message and the second should give us the no checkup found.
<br />
After verifying that the class methods work commit changes.

```bash
git commit -am "Updated Dog model"
```

#### Step 7: Push changes to GitHub and Merge Branches

* Push the branch to GitHub:

```bash
git push origin updated_dog_model
```

* Create a Pull Request (PR) on GitHub.

* Merge the PR into main after review.

* Pull the new merged main branch locally and delete merged feature branch (optional): 

```bash
git checkout main
git pull origin main

git branch -d updated_dog_model
```

If the last command doesn’t delete the branch, it’s likely git is not recognizing the branch as having been merged. Verify you do have the merged code in your main branch, then you can run the same command but with a capital D to ignore the warning and delete the branch anyway.

```bash
git branch -D updated_dog_model
```

### Task 4: Document and Maintain

Best Practice documentation steps:

* Add comments to code to explain purpose and logic
* Clarify intent / functionality of code to other developers
* Add screenshot of completed work included in Markdown in README.
* Update README text to reflect the functionality of the application following https://makeareadme.com. 
* Delete any stale branches on GitHub
* Remove unnecessary/commented out code
* If needed, update git ignore to remove sensitive data

## Considerations

* Decorators
  * It is important that the decorator be immediately followed by a method! If it is not then it will not work
* Dictionaries
  * While dictionaries are similar to objects in javascript it is important to remember the distinctions. In python we cannot use ```dict.attr```, we need to use ```dict[“attr”]```. So in this case we should not use checkup.date, we need to use ```checkup[“date”]```
