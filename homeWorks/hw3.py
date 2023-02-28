class Bank:
    def __init__(self, name, balanse):
        self._name = name
        self._balanse = balanse 

    def moneyX(self):
        user = int(input('top up balanse?: '))
        self._balanse += user
        return f'In your balanse: {self._balanse}, Username: {self._name}'

    def _kill(self):
        user = int(input('how much do u want to cash out?: '))
        if user <= 0:
            self._balanse -= user
            return f'in your balense: {self._balanse}'
        else:
            return f'there is not enough money in your balanse, in the balanse: {self._balanse}'

    def __jackpot(self):
        return 'f multiply your balanse by 10. your balanse: {self._balanse * 10}'

    def unite(self, Bekbolot, Zahro):
        self.beka = Bekbolot
        self.zara = Zahro
        return f'beka: {100}, zahro: {self.zara + 100} '

optima = Bank('Zahro', 100)
print(optima.moneyX())
print(optima._kill())
print(optima._Bank__jackpot())
print(optima.unite('beka', 100))
