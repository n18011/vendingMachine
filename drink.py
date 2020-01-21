class Drink:
    def __init__(self, name, much):
        self.name = name
        self.much = much


if __name__ == '__main__':
    CORA = Drink('cora', 120)
    print(CORA.name, CORA.much)
