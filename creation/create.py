from owlready2 import *
from rdflib import Graph
onto = get_ontology("social_network.owl")

with onto:
    class Person(Thing):
        has_age = DatatypeProperty()

        def get_age(self):
            return self.has_age[0]

        def set_age(self, value):
            self.has_age = [value]

        age = property(get_age, set_age)

    class Group(Thing):
        pass

    class hasFriend(ObjectProperty):
        domain = [Person]
        range = [Person]

    class memberOf(ObjectProperty):
        domain = [Person]
        range = [Group]

dima = Person("Dima")
sasha = Person("Sasha")
mark=Person("Mark")
groupPython = Group("PythonGroup")
groupJava = Group("JavaGroup")
groupGo = Group("GoGroup")
groupJS = Group("JSGroup")

mark.hasFriend.append(dima)
sasha.hasFriend.append(mark)
dima.memberOf.append(groupPython)
mark.memberOf.append(groupGo)

dima.age = 18
mark.age = 20
sasha.age=25

onto.save(file = "social_network.owl", format = "ntriples")

#16_methods
def calculate_average_age_in_group(group):
    if isinstance(group, Group):
        total_age = 0
        total_persons = 0
        for person in group.memberOf:
            if isinstance(person, Person):
                total_age += person.age
                total_persons += 1
        if total_persons > 0:
            average_age = total_age / total_persons
            return f"Average age in {group.name}: {average_age}"
        else:
            return f"No persons in {group.name}"
    else:
        return "Invalid input, expecting a Group instance"


print(calculate_average_age_in_group(groupPython))


def find_oldest_person(ontology):
    max_age = 0
    oldest_person = None
    for person in ontology.Person.instances():
        if person.age > max_age:
            max_age = person.age
            oldest_person = person
    if oldest_person:
        return f"The oldest person is {oldest_person.name} with age {max_age}"
    else:
        return "No persons in the network"

print(find_oldest_person(onto))


def are_persons_friends(person1, person2):
    if isinstance(person1, Person) and isinstance(person2, Person):
        return f"{person1.name} and {person2.name} are friends: {person2 in person1.hasFriend}"
    else:
        return "Invalid input, expecting Person instances"

print(are_persons_friends(dima, sasha))




#15_queries

