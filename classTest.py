class Auto():
    blub = 6

    def __init__(self, reifen, marke):
        self.reifen = reifen
        self.marke = marke
        self.__farbe = "rot"

    def name(self):
        print(str(self.reifen) + self.marke)

    def square(self):
        print(self.reifen*self.reifen)

    def jawoll(self):
        if self.__farbe == "rot":
            print("ja")




class Phonebook():
    def __init__(self):
        self.__entries= {}

    def addNumber(self, name, number):
        self.__entries[name] = number

    def get(self, name):
        if name in self.__entries:
            return self.__entries[name]
        else:
            return None

    def __str__(self):
        return "Phonebook" + str(self.__entries)


book = Phonebook()
book.addNumber("Peter","0815")

#print(book.get("Peter"))

print(book)


#print("hallo")
harri = Auto(4, "audi")

harri.name()
harri.square()
harri.name()
#print(harri.blub)
harri.jawoll()

