class Temperatura:
    def __init__(self, fecha : Fecha, maxTemp : int, minTemp : int) -> None:
        self._fecha = fecha
        self._tMax = maxTemp
        self._tMin = minTemp
   
    def modificar_temperaturas(self, maxTemp, minTemp):
        self._tMax = maxTemp
        self._tMin = minTemp
   
    def devolver_temp_max(self):
        return self._tMax
   
    def devolver_temp_min(self):
        return self._tMin
   
    def devolver_temp_media(self):
        return (self._tMax+self._tMin)/2
   
    def __str__(self) -> str:
        return (f"Fecha: {self._fecha}; Temp.max: {self.devolver_temp_max()}; Temp.min: {self.devolver_temp_min()}; Temp.media {self.devolver_temp_media()}")


def test_temp():
    fechas = Fecha()
    fechas.modificar_fecha(12,2,2024)
    temp = Temperatura(fechas, 5, 20)
    print(temp)



class Factura:
    def __init__(self) -> None:
        pass

def test_fact():
    pass

tests = [test_bombilla, test_fecha, test_temp, test_fact]

opt = int(input(f"Dime numero de test [1-{len(tests)}]: "))
tests[opt-1]()
