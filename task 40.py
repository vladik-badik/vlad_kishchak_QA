from abc import ABC, abstractmethod


class Sedan(ABC):
    @abstractmethod
    def useful_function_a(self) -> str:
        pass

class Hatchback(ABC):
    @abstractmethod
    def useful_function_b(self) -> str:
        pass


class mersedes_S(Sedan):
    def useful_function_a(self) -> str:
        return "The result of the mersedes S class."

class mersedes_CLK(Sedan):
    def useful_function_a(self) -> str:
        return "The result of the mersedes CLK."


class mersedes_A1(Hatchback):
    def useful_function_b(self) -> str:
        return "The result of the mersedes A1 class ."

class miniCooper(Hatchback):
    def useful_function_b(self) -> str:
        return "The result of the Mini Cooper."


class Concern_Mersedes(ABC):
    @abstractmethod
    def create_product_a(self) -> Sedan:
        pass

    @abstractmethod
    def create_product_b(self) -> Hatchback:
        pass


class Mersedes_LTD(Concern_Mersedes):
    def create_product_a(self) -> Sedan:
        return mersedes_S()

    def create_product_b(self) -> Hatchback:
        return mersedes_A1()


class Cooper_LTD(Concern_Mersedes):
    def create_product_a(self) -> Sedan:
        return mersedes_CLK()

    def create_product_b(self) -> Hatchback:
        return miniCooper()


def client_code(factory: Concern_Mersedes) -> None:
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(product_a.useful_function_a())
    print(product_b.useful_function_b())


if __name__ == "__main__":
    factory1 = Mersedes_LTD()
    client_code(factory1)

    factory2 = Cooper_LTD()
    client_code(factory2)
