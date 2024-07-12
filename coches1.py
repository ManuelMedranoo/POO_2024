class Motos:
    def _init_(self,color,marca,modelo,velocidad,caballaje,pesoMax,precio):
        self.color=color
        self.marca=marca
        self.modelo=modelo
        self.velocidad=velocidad
        self.caballaje=caballaje
        self.pesoMax=pesoMax
        self.precio=precio

    def acelerar(self):
        self.velocidad+=1

    def frenar(self):
        self.velocidad-=1

    def getColor(self):
      return self.color

    def setColor(self,color):
      self.color=color 

    def getMarca(self):
      return self.marca

    def setMarca(self,marca):
      self.marca=marca 

    def getModelo(self):
      return self.modelo

    def setModelo(self,modelo):
      self.modelo=modelo        

    def getVelocidad(self):
       return self.velocidad

    def setVelocidad(self,velocidad):
      self.velocidad=velocidad 

    def getCaballaje(self):
       return self.caballaje

    def setCaballaje(self,caballaje):
      self.caballaje=caballaje  

    def getPesoMax(self):
       return self.pesoMax

    def setPesoMax(self,pesoMax):
      self.pesoMax=pesoMax 

    def getPrecio(self):
       return self.precio

    def setPesoMax(self,precio):
      self.precio=precio 

    def getInfo(self):
       print(f"Marca: {self.getMarca()} {self.getColor()}, pseo maximo soportado por el vehiculo: {self.getPesoMax()} \nModelo: {self.getModelo()} con una velocidad de {self.getVelocidad()} Km/h y un potencia de {self.getCaballaje()} hp \nY tiene un precio de {self.getPrecio()} pesos mexicanos.")  

class ATV(Motos):
   def _init_(self,color,marca,modelo,velocidad,caballaje,pesoMax,precio,transmision,capacidadCarga):
    super()._init_(color,marca,modelo,velocidad,caballaje,pesoMax,precio)
    self.transmision=transmision
    self.capacidadCarga=capacidadCarga

   CC=""

   def clindrada(self,CC):
    self.CC=CC
    return self.CC

   def getTransmision(self):
     return self.transmision

   def setTransmision(self,transmision):
      self.transmision=transmision  

   def getcapacidadCarga(self):
     return self.capacidadCarga

   def setcapacidadCarga(self,capacidadCarga):
      self.capacidadCarga=capacidadCarga 

   def getInfo(self):
      print(f"Marca: {self.getMarca()} {self.getColor()}, capacidad de peso maximo soportado: {self.getPesoMax()} \nModelo: {self.getModelo()} con una velocidad de {self.getVelocidad()} Km/h, una potencia de {self.getCaballaje()} hp, con una transmision {self.getTransmision()} y una capacidad de carga de {self.getcapacidadCarga()} metros cubicos")       

class Deportivas(Motos):
  def _init_(self,color,marca,modelo,velocidad,caballaje,pesoMax,precio,transmision,velociades):
    super()._init_(color,marca,modelo,velocidad,caballaje,pesoMax,precio)
    self.transmision=transmision
    self.velocidades=velociades

  RPM=0
  def potencia(self,RPM):
      self.RPM=RPM
      return self.RPM

  def getTransmision(self):
     return self.transmision

  def setTransmision(self,transmision):
      self.transmision=transmision

  def getVelocidades(self):
    return self.velocidades

  def setVelocidades(self,velocidades):
    self.velocidades=velocidades

  def getInfo(self):
      print(f"Marca: {self.getMarca()} {self.getColor()}, capacidad de peso maximo soportado: {self.getPesoMax()} \nModelo: {self.getModelo()} con una velocidad de {self.getVelocidad()} Km/h, una potencia de {self.getCaballaje()} hp, con una transmision {self.getTransmision()} y con {self.getVelocidades()} cambios de velocidades.")