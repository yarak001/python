# #list
# shoplist = ['apple', 'mango', 'carrot', 'banana']
#
# print("I have", len(shoplist), 'items to purchase.')
#
# print("These items are:",)
# for item in shoplist:
#     print(item,)
#
# print("\nI also have to buy rice.")
# shoplist.append("rice")
# print("My shopping list is now", shoplist)
#
# print('I will sort my list now')
# shoplist.sort()
# print("Sorted shopping list is", shoplist)
#
# print("The first item i will buy is", shoplist[0])
# olditem = shoplist[0]
# del shoplist[0]
# print("I bought the", olditem)
# print("My shopping list is now", shoplist)

#tuple
# zoo = ('python', 'elephant', 'penguin')
# print("Number of animals in the zoo is", len(zoo))
#
# new_zoo = 'monkey', 'camel', zoo
# print("Number of cages in the new zoo is", len(new_zoo))
# print("All animals in new zoo are", new_zoo)
# print("Animals brought from old zoo are", new_zoo[2])
# print("Last animal brought from old zoo is", new_zoo[2][2])
# print("Number of animals in the new zoo is", len(new_zoo) - 1 + len(new_zoo[2]))

#dictionary
# ab = {
#     'Swaroop' : 'swaroop@swaroop.com',
#     'Larry' : 'larry@wall.org',
#     'Matsumoto' : 'matz@ruby-lang.org',
#     'Spammer' : 'Spammer@hotmail.com'
# }
#
# print("Swaroop's address is", ab['Swaroop'])
#
# del ab['Spammer']
#
# print("\nThere are {} contracts in the address-book\n".format(len(ab)))
#
# for name, address in ab.items():
#     print("Contact {} at {}".format(name, address))
#
# ab["Guido"] = 'guido@python.org'
#
# if 'Guido' in ab:
#     print("\nGuido's address is", ab['Guido'])

#Enumeration

# shoplist = ['apple', 'mango', 'carrot', 'banana']
# name = 'swaroop'
#
# print("Item 0 is", shoplist[0])
# print("Item 1 is", shoplist[1])
# print("Item 2 is", shoplist[2])
# print("Item 3 is", shoplist[3])
# print("Item -1 is", shoplist[-1])
# print("Item -2 is", shoplist[-2])
# print("Character 0 is", name[0])
#
# print("Item 1 to 3 is", shoplist[1:3])
# print("Item 2 to end is", shoplist[2:])
# print("Item 1 to -1 is", shoplist[1:-1])
# print("Item start to end is", shoplist[:])
#
# print("Character 1 to 3 is", name[1:3])
# print("Character 2 to end is", name[2:])
# print("Character 1 to -1 is", name[1:-1])
# print("Character start to end is", name[:])

#set
# bri = set(['brazil', 'russia', 'india'])
# print(bri)
# print('india' in bri)
# print('usa' in bri)
#
# bric = bri.copy()
# bric.add('china')
# print(bric)
# print(bric.issuperset(bri))
#
# bri.remove('russia')
# print(bri)
# print(bri & bric)

#reference binding
# print("Simple Assignment")
# shoplist = ['apple', 'mango', 'carrot', 'banana']
# mylist = shoplist
#
#
# del shoplist[0]
#
# print("Shoplist is", shoplist)
# print("mylist is", mylist)
#
# print("Copy by making a full slice")
# mylist = shoplist[:]
# del mylist[0]

# print("Shoplist is", shoplist)
# print("mylist is", mylist)

# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def say_hi(self):
#         print("Hello, how are you?", self.name)
#
# p = Person("yarak")
# p.say_hi()

# class Robot:
#     """
#
#     """
#     population = 0
#
#     def __init__(self, name):
#         """
#
#         :param name:
#         """
#         self.name = name
#         print("(Initializing {})".format(self.name))
#
#         Robot.population += 1
#
#     def die(self):
#         """
#
#         :return:
#         """
#         print("{} is beigng destroyed".format(self.name))
#
#         Robot.population -= 1
#
#         if Robot.population == 0:
#             print("{} was the last one.".format(self.name))
#         else:
#             print("Theer are still {:d} robots working".format(Robot.population))
#
#     def say_hi(self):
#         """
#
#         :return:
#         """
#         print("Greetings, my masters call me {}.".format(self.name))
#
#     @classmethod
#     def how_many(cls):
#         """
#
#         :return:
#         """
#         print("We have {:d} robots.".format(cls.population))
#
# droid1 = Robot("R2-D2")
# droid1.say_hi()
# Robot.how_many()
#
# droid2 = Robot("C-3PO")
# droid2.say_hi()
# Robot.how_many()
#
# print("\nRobots can do some work here.\n")
# print("Robots have finished their work. So let's destory them.")
# droid1.die()
# droid2.die()
#
# Robot.how_many()

# class SchoolMember:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print("(Initialized SchoolMember: {})".format(self.name))
#
#     def tell(self):
#         print("Name:{}, Age:{}".format(self.name, self.age),)
#
#
# class Teacher(SchoolMember):
#     def __init__(self, name, age, salary):
#         SchoolMember.__init__(self, name, age)
#         self.name = name
#         self.age = age
#         self.salary = salary
#         print("(Initialized Teacher: {})".format(self.name))
#
#     def tell(self):
#         SchoolMember.tell(self)
#         print("Salary: {}".format(self.salary))
#
# class Student(SchoolMember):
#     def __init__(self, name, age, marks):
#         SchoolMember.__init__(self, name, age)
#         self.name = name
#         self.age = age
#         self.marks = marks
#         print("(Initialized Student: {})".format(self.name))
#
#     def tell(self):
#         SchoolMember.tell(self)
#         print("Marks:{}".format(self.marks))
#
#
# t = Teacher("Mrs. Shrividya", 40, 30000)
# s = Student("Swarooop", 25, 75)
#
# print
#
# members = [t, s]
# for member in members:
#     member.tell();

try:
    text = input("Enter something:")
except EOFError:
    print("EOFError")
except KeyboardInterrupt:
    print("KeyboardInterrupt")
# else:
#     print("you entered {}".format(text))

print("you entered {}".format(text))