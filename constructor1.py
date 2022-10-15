# in python two or more constructor does not work at a same time.
# does not work overloading
class poliparty:
    def __init__(self):
        self.symbol ="Alaram"
        self.pname = "NCP"

    def dispParty(self):
        print(self.pname)
        print(self.symbol)
Obj = poliparty()
Obj.dispParty()

#address print
print(Obj.dispParty)
#" Function is a object " explain this stament following two lines.IMp for interview
#type of object object cha class ha tyacha class name aste
print(type(Obj))

#in the class function is a method and it can not change anytime
print(type(Obj.dispParty))