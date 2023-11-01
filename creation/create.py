from owlready2 import *

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
