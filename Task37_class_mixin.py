class AttributePrinterMixin:
    pass
def __str__(self):
        class_name = type(self).__name__
        attributes = self._get_attributes()
        return self._format_output(class_name, attributes)

def _get_attributes(self):
        attributes = {}
        for cls in reversed(type(self).mro()):
            for name, value in cls.__dict__.items():
                if not callable(value) and not name.startswith('_'):
                    attributes[name] = value
        return attributes
def _format_output(self, class_name, attributes):
        output = f'{class_name}:\n'
        for name, value in attributes.items():
            if name.startswith('__') and name.endswith('__'):
                name = name[2:-2]  # Remove leading and trailing underscores for special names
            elif name.startswith('_'):
                name = name[1 + len(class_name):]  # Remove class name prefix for private fields
            output += f'\t{name}: {value}\n'
        return output

class Person(AttributePrinterMixin):
        def __init__(self, name, age):
            self.name = name
            self._age = age
            self.__address__ = '123 Main St'

class Student(Person):
        def __init__(self, name, age, major):
            super().__init__(name, age)
            self.major = major
person = Person('Alice', 25)
print(person)

student = Student('Bob', 20, 'Computer Science')
print(student)
