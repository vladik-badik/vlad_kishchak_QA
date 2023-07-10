from abc import ABC, abstractmethod


class AbstractProductA(ABC):
    @abstractmethod
    def useful_function_a(self) -> str:
        pass

class AbstractProductB(ABC):
    @abstractmethod
    def useful_function_b(self) -> str:
        pass


class specificProductA1(AbstractProductA):
    def useful_function_a(self) -> str:
        return "The result of the product A1."

class specificProductA2(AbstractProductA):
    def useful_function_a(self) -> str:
        return "The result of the product A2."


class specificProductB1(AbstractProductB):
    def useful_function_b(self) -> str:
        return "The result of the product B1."

class specificProductB2(AbstractProductB):
    def useful_function_b(self) -> str:
        return "The result of the product B2."


class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass


class specificFactory1(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return specificProductA1()

    def create_product_b(self) -> AbstractProductB:
        return specificProductB1()


class specificFactory2(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return specificProductA2()

    def create_product_b(self) -> AbstractProductB:
        return specificProductB2()


def client_code(factory: AbstractFactory) -> None:
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(product_a.useful_function_a())
    print(product_b.useful_function_b())


if __name__ == "__main__":
    factory1 = specificFactory1()
    client_code(factory1)

    factory2 = specificFactory2()
    client_code(factory2)
