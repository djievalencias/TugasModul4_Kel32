class nasabah:
    def __init__(self, id, custPin = 1212, custBalance = 100000):
        self.id = id
        self.custPin = custPin
        self.custBalance = custBalance

    def cekId(self):
        return self.id
    
    def cekPin (self):
        return self.custPin
    def cekBalance (self):

    def withdrawBalance (self, nomimal):
        self.custBalance -= nominal)

    def depositBalance (self, nominal):
        self.custBalance += nominal