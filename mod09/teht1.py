class Auto:
    def __init__(self, rek_nro, huippunopeus):
        self.rek_nro = rek_nro
        self.nopeus = 0
        self.huippunopeus = huippunopeus

    def tulosta_rekkari(self):
        print(f'Rekkari: {self.rek_nro}')


Auto('ABC-123', 120).tulosta_rekkari()
Auto('XYZ-789', 250)