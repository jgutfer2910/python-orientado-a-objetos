class Fecha:
    def __init__(self):
        self._año = 0
        self._mes = 0
        self._dia= 0
    def ModificarFecha(self, dia , mes , año):
        self.ModificarDia(dia)
        self.ModificarMes(mes)
        self.ModificarAño(año)

    def ModificarDia(self, dia ):
        if self.ComprobarDia(dia):
            self._dia = dia
        else:
            print("El numero debe estar entre 1 y 31")
           
    def ModificarMes(self, mes):
        if self.ComprobarMes(mes):
            self._mes=mes
        else:
            print("El numero debe estar entre 1 y 12")
           
    def ModificarAño(self, año):
        self._año = año
   
    def DevoverDia(self) ->int:
        return self._dia
   
    def DevoverMes(self) ->int:
        return self._mes
   
    def DevoverAño(self) ->int:
        return self._año
   
    def  ComprobarDia(self, dia):
        return dia >=1 and dia <=31
   
    def  ComprobarMes(self, mes):
        return mes >=1 and mes <= 12

    def __str__(self) -> str:
        return f"{self.DevoverDia()}/{self.DevoverMes()}/{self.DevoverAño()}"

def test_fecha():
    d=int(input("dame el dia: "))
    m=int(input("dame el mes: "))
    a=int(input("dame el año: "))
    fechas = Fecha()
    fechas.ModificarFecha(d,m,a)
    print(fechas)

test_fecha()
