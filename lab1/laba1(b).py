
import doctest


class Person:
    def __init__(self, name: str, age: int):
        """
        Создание и подготовка к работе объекта

        :param name: Имя человека
        :param age: Возраст человека

        Пример:
        >>> person = Person("Мария", 20)

        """
        if not isinstance(name, (str)):
            raise TypeError("Имя должно быть типа str")
        self.name = name
        if not isinstance(age, (int)):
            raise TypeError("Возраст должен быть типа int")
        if age <= 0:
            raise ValueError("Возраст должен быть положительным числом")
        self.age = age

    def birthday(self, year: int):
        """
        Функция определяет год рождения

        :return: Год рождения

        """
        ...

    def gender(self):
        """
        Функция определяет гендер

        """
        ...


class Furniture:
    def sit(self):
        ...

    def size_of_object(self, size: int):
        ...


class Facebook:
    def post(self, content: str):
        ...

    def like(self, post_id: int) -> bool:
        ...


if __name__ == "__main__":
    doctest.testmod()
