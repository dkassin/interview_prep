class Consumable:

    def consume(self) -> None: pass


class StockAvailable(Consumable):
    def consume(self, machine: 'VendingMachine') -> None:
        print(f"consume succeed: {super.self.stock} remained")


class StockUnavailable(Consumable):

    def __init__(self) -> None:
        self.cooldown = 3

    def consume(self, machine: 'VendingMachine') -> None:
        print(f"consume failed: stock is empty, waiting for cooldown: {self.cooldown}")
        self.cooldown -= 1


class VendingMachine:

    def __init__(self) -> None:
        self.stock = 3
        self.state = StockAvailable()

    def consume(self) -> None:
        if self.stock > 0:
            self.stock -= 1
            self.state.consume
        elif self.stock <= 0:
            self.state = StockUnavailable
            self.state.consume
            self.stock -= 1
        elif self.stock <= (-2):
            self.stock = 2
            self.state = StockAvailable()

            



