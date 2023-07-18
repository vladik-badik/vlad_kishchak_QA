class AttributePrinterMixin:

    def __str__(self):
        class_name = self.__class__.__name__
        attributes = self._get_attributes()
        output = f"{class_name}: {{\n"
        output += self._format_attributes(attributes)
        output += "}"
        return output

    def _get_attributes(self):
        attributes = {}
        for base_class in reversed(self.__class__.__bases__):
            if issubclass(base_class, AttributePrinterMixin):
                attributes.update(base_class._get_attributes(base_class))
        attributes.update(self.__dict__)
        return attributes

    def _format_attributes(self, attributes):
        output = ""
        for key, value in attributes.items():
            formatted_key = self._format_key(key)
            formatted_value = self._format_value(value)
            output += f"\t{formatted_key}: {formatted_value}\n"
        return output

    def _format_key(self, key):
        if key.startswith("_") and not key.startswith("__"):
            key = key[1:]
        elif key.startswith(f"_{self.__class__.__name__}__"):
            key = key[len(self.__class__.__name__) + 2:]
        return key

    def _format_value(self, value):
        if isinstance(value, list):
            return f"[{', '.join(str(item) for item in value)}]"
        return str(value)


class A(AttributePrinterMixin):
    def __init__(self):
        super().__init__()
        self.public_field = 3
        self._protected_field = 'q'
        self.__private_field = [1, 2, 3]

a = A()
print(a)
