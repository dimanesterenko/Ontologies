from owlready2 import get_ontology
onto = get_ontology("ont.owx").load()
def count_classes():
    return len(list(onto.classes()))
def count_instances():
    return len(list(onto.individuals()))

def classes_with_property(property_name):
    classes = []
    for cls in onto.classes():
        if hasattr(cls, property_name):
            classes.append(cls)
    return classes

def print_all_classes():
    for cls in onto.classes():
        print(cls)

if __name__ == "__main__":
    num_classes = count_classes()
    num_instances = count_instances()
    specific_property = "забезпечується"
    classes_with_specific_property = classes_with_property(specific_property)
    print(f"Кількість класів: {num_classes}")
    print(f"Кількість екземплярів: {num_instances}")
    print(f"Класи з властивістю {specific_property}: {classes_with_specific_property}")
    print("Назви усіх класів:")
    print_all_classes()