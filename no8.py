class pecahan :
    def init(self, atas, bawah):
        self.num = atas
        self.den = bawah

    def repr(self):
        return repr(str(self.num)+"/"+ str(self.den))

x = input("pembilang =")
y = input("penyebut =")
z = pecahan(x,y)
print (z)