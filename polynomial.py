
""" define some class for polynomial """
class term:
    def __init__(self,coef = None,expo = None):
        if coef == None or expo == None:
            raise ValueError("invaild value")
        self.coef = coef
        self.expo = expo
        
    def toString(self):
        if self.expo == 0 and self.coef > 0:
            return " + "+str(self.coef)
        elif self.expo == 0 and self.coef < 0:
            return " - "+str(-self.coef)
        elif self.coef > 0:
            return  " + "+str(self.coef)+"X^"+str(self.expo)
        elif self.coef < 0:
            return " - "+str(-self.coef)+"X^"+str(self.expo)

class polynomial:
    def __init__(self,li = None):
        if li == None:
            self.fun = [term(1,0)]
            self.len = 1
            return
        self.fun = []
        self.terms = []
        for item in li:
            terms = term(item[0],item[1])
            self.terms.append(terms)
        self.fun = self.build(self.terms)
        self.len = len(self.fun)

    def Differential(self):
        li = []
        for item in self.fun:
            if item.expo == 0:
                break
            else:
                li.append([item.coef*item.expo,item.expo-1])
        polydiff = polynomial(li)
        return polydiff

    def build(self,li):
        t = term(1,1)
        for i in range(0,len(li)):
            for j in range(0,len(li)):
                if li[i].expo > li[j].expo:
                    t.expo = li[j].expo
                    t.coef = li[j].coef
                    li[j].coef = li[i].coef
                    li[j].expo = li[i].expo
                    li[i].coef = t.coef
                    li[i].expo = t.expo
        return li

    def compute(self,x):
        res = 0
        for item in self.fun:
            res += item.coef*pow(x,item.expo)
        return res

    def show(self):
        cnt = 0
        for item in self.fun:
            if cnt == 0:
                 print(item.toString(),end = "")
                 cnt = 1
            else:
                print(item.toString(),end = "")
        print()
