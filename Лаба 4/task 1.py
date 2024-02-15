if __name__ == "__main__":
    class Vehicle:
        """
        Базовый класс для различных видов транспортных средств
        """

        def __init__(self, brand: str, model: str, year: int):
            """
            Конструктор класса Vehicle.

            :param brand: Марка транспортного средства
            :param model: Модель транспортного средства
            :param year: Год выпуска транспортного средства
            """
            self.brand = brand
            self.model = model
            self.year = year

        def __str__(self) -> str:
            return f"{self.brand} {self.model} ({self.year})"

        def __repr__(self) -> str:
            return f"Vehicle({self.brand}, {self.model}, {self.year})"


    class Car(Vehicle):
        """
        Дочерний класс, представляющий легковой автомобиль
        """

        def __init__(self, brand: str, model: str, year: int, color: str):
            """
            Конструктор класса Car

            :param brand: Марка автомобиля
            :param model: Модель автомобиля
            :param year: Год выпуска автомобиля
            :param color: Цвет автомобиля
            """
            super().__init__(brand, model, year)
            self.color = color

        def drive(self, distance: float) -> None:
            """
            Метод для перемещения автомобиля на заданное расстояние

            :param distance: Расстояние в километрах
            """
            print(f"The {self.color} {self.brand} {self.model} is driving {distance} km.")

        def __str__(self) -> str:
            return f"{self.color} {self.brand} {self.model} ({self.year})"

        def __repr__(self) -> str:
            return f"Car({self.brand}, {self.model}, {self.year}, {self.color})"

    pass
