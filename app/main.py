class Animal:
    alive = []

    def __init__(self
                 , name: str
                 , health: int = 100
                 , hidden: bool = False
                 ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        list_animal = []
        for i in range(len(Animal.alive)):
            list_animal.append(f"{{Name: {Animal.alive[i].name}"
                               f", Health: {Animal.alive[i].health}"
                               f", Hidden: {Animal.alive[i].hidden}}}")
        Animal.alive.clear()
        Animal.alive = ", ".join(list_animal)
        return Animal.alive


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, other: Herbivore) -> None:
        if (
                isinstance(self, Carnivore) is True
                and isinstance(other, Carnivore) is False
                and other.hidden is False
        ):
            other.health -= 50
            if other.health <= 0:
                Animal.alive.remove(other)
