

class Product:

    def __init__(self,pid,pnm,pqty,pven,pprc):
        self.prodId = pid
        self.prodName = pnm
        self.prodQty = pqty
        self.prodVen = pven
        self.prodPrice = pprc

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'''{self.__dict__}'''
