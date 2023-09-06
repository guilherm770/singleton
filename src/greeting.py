class Greeting:

    def __init__(self, name):
        self.message = """Olá, {}. Tudo bem?!"""
        self.name = name

    def greet(self):
        print(self.message.format(self.name))

    def change_name(self, name):
        self.name = name