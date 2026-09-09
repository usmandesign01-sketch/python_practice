# Static Method:
# When we write "@staticmethod", after we don't enter argument.......
# Method that don't use self parameter

class Method:
    @staticmethod
    def static_method():
        print("This is static method")

# Call the static method using the class name
Method.static_method()
