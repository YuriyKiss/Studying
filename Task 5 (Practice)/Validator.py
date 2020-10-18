class Validator:
    @staticmethod
    def input_int(message):
        while True:
            try:
                num = int(input())
            except TypeError:
                print("This should be an integer type")
