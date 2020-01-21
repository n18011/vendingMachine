import drink
import money


class VendingMachine:
    def __init__(self):
        self.money = 0
        self.money_display()

    # 飲み物をセットする
    def set_drink(self, d):
        self.drink = d

    # 飲み物を表示する
    def drink_display(self):
        print(self.drink.name)

    # お金を投入する
    def set_money(self, m):
        self.money = m.much

    # 投入金額を表示する
    def money_display(self):
        print(self.money)

    # 飲み物を出す
    def put_out_drink(self):
        print(self.drink)

    # お釣りを出す
    def put_out_change(self):
        print(self.money)


if __name__ == '__main__':
    YEN500 = money.Money(500)
    CORA = drink.Drink('cora', 120)
    VM = VendingMachine()
    VM.set_drink(CORA)
    VM.drink_display()
    VM.set_money(YEN500)
    VM.money_display()
