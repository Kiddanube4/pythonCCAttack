import  random
class NameGen:
    names = ["Demirhan",
             "Erkut",
             "Günçe",
             "Kutay",
             "Sağın",
             "Tilbe",
             "Türemen",
             "Ananizi"]


    lastNames = ["Zeren",
                 "Yaman",
                 "Pelin",
                 "Pelin",
                 "Kubat",
                 "Kubat",
                 "Oytun",
                 "Siktik"]

    def generateName(self):
        name = self.names[random.randrange(0, len(self.names))]
        lastName = self.lastNames[random.randrange(0, len(self.lastNames))]


        return  name + " " + lastName

class CCgen:
    def createCCno(self):
        isVisa = random.randrange(0,100)
        if isVisa < 50:
            ccNo = "5342"
        else:
            ccNo = "4543"

        for x in range(3):
            randNo = f"{random.randrange(1000, 9999)}"
            ccNo += " " + randNo
        return ccNo
    def createCVV(self):
        return f"{random.randrange(100, 999)}"

    def creteCCDate(self):
        randMonth = random.randrange(1, 12)
        randYear = random.randrange(26, 30)

        if randMonth < 10:
            randMonth = f"0{randMonth}"

        return f"{randMonth}/{randYear}"

