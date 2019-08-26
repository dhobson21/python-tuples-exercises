#Create a tuple named zoo that contains 10 of your favorite animals.
zoo = ("monkey", "penguin", "lion", "tiger", "snake", "bug", "elephant", "lemur", "puma", "zebra")

#Find one of your animals using the tuple.index(value) syntax on the tuple.
print(zoo.index("puma"))

#Determine if an animal is in your tuple by using value in tuple syntax.
animal_to_find = 'monkey'
if animal_to_find in zoo:
    print(f'The {animal_to_find} is in the zoo')
else:
    print(f'The {animal_to_find} is not in the zoo')

#You can reverse engineer a tuple into another tuple with the following syntax.
# children = ("Sally", "Hansel", "Gretel", "Svetlana")
# (first_child, second_child) = children
# print(first_child) # Output is "Sally"
# print(second_child) # Output is "Hansel"
# zoo = (first_child, second_child)
# lilZoo = (zoo[slice(0,3)])
# print("lil zoo", lilZoo)

#Convert your tuple into a list
zoo_list = list(zoo)

#Use extend() to add three more animals to your zoo.
zoo_list.extend(["rhino", "kangaroo", "jaguar"])

#Convert the list back into a tuple.

new_zoo = tuple(zoo_list)