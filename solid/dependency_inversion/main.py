"""Dependency Inversion Principle (DIP).
High-level modules should not depend on low-level modules.
Both should depend on abstractions.
Abstractions should not depend on details.
Details should depend on abstractions.
"""

from abc import abstractmethod
from enum import Enum


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return self.name


class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name: str) -> list[Person]:
        pass


class Relationships(RelationshipBrowser):
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent: Person, child: Person):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))

    def find_all_children_of(self, name: str) -> list[Person]:
        return [r[2].name for r in self.relations if r[0].name == name and r[1] == Relationship.PARENT]


# Violation: High-level module (Research) directly depends on low-level module (Relationships).
# Research extracts data directly from the internal data structure of Relationships (self.relationships = relationships.relations),
# instead of depending on an abstraction (e.g., an interface or method).
class Research:
    # def __init__(self, relationships: Relationships):
    # Direct access to the 'relations' field - DIP violation
    # for r in relationships.relations:
    #     if r[0].name == "John" and r[1] == Relationship.PARENT:
    #         print(f"John has a child called {r[2].name}")

    def __init__(self, browser: RelationshipBrowser):
        for p in browser.find_all_children_of("John"):
            print(f"John has a child called {p}")


def main():
    parent = Person("John")
    child1 = Person("Chris")
    child2 = Person("Matt")
    relationships = Relationships()
    relationships.add_parent_and_child(parent, child1)
    relationships.add_parent_and_child(parent, child2)

    Research(relationships)


if __name__ == "__main__":
    main()
