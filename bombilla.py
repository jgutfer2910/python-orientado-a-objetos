class Bombilla():
    def __init__(self, _contador, _encendida, _fundida):
        _contador = 0
        _encendida = False
        _fundida = False

    def encender(self):
        if self._fundida:
            print ("La bombilla esta fundida")
        else:
            if self._encendida:
                print ("La bombilla ya está encendida")
            else:
                self._encendida = True
                self._contador += 1 
                if self._contador == 1000:
                    self._fundida = True
                    
    def apagar(self):
        if self._fundida:
            print ("La bombilla esta fundida")
        else:
            if self._encendida == False:
                print ("La bombilla ya está apagada")
            else:
                self._encendida = False
