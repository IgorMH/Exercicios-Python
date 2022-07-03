class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatada(self):
        if self.dia < 10 and self.mes < 10:
            print("0{}/0{}/{}".format(self.dia, self.mes, self.ano))

        if self.dia >= 10 > self.mes:
            print("{}/0{}/{}".format(self.dia, self.mes, self.ano))

        if self.dia < 10 <= self.mes:
            print("0{}/{}/{}".format(self.dia, self.mes, self.ano))

        if self.dia >= 10 and self.mes >= 10:
            print("{}/{}/{}".format(self.dia, self.mes, self.ano))

d1 = Data(10, 10, 2022)
d1.formatada()