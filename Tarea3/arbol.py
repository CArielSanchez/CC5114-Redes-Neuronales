import random

class Nodo:
    def __init__(self,valor,nodoIzquierdo,nodoDerecho):

        self.valor = valor
        self.nodoIzquierdo = nodoIzquierdo
        self.nodoDerecho = nodoDerecho
    
    def setValor(self, valor):
        self.valor = valor

    def soyHoja(self):
        return False

    def setNodoIzquierdo(self,nodoIzquierdo):
        self.nodoIzquierdo = nodoIzquierdo

    def setNodoDerecho(self,nodoDerecho):
        self.nodoDerecho = nodoDerecho
    
    def getNodoIzq(self):
        return self.nodoIzquierdo

    def getNodoDer(self):
        return self.nodoDerecho

    def getValor(self):
        return self.valor
    
    def numberHojas(self):
        if self.soyHoja():
            return 1
        else:
            c = self.getNodoDer().numberHojas()
            c += self.getNodoIzq().numberHojas()
            return c
    

class Hoja(Nodo):
    def __init__(self,valor):
        super().__init__(valor,None,None)

    def soyHoja(self):
        
        return True

# Arbol de expresiones

class Arbol:
    def __init__(self,raiz):
        self.raiz = raiz
    
    def copyNodo(self,nodo):
        if nodo.soyHoja():
            nuevaHoja = Hoja(nodo.getValor())
            return nuevaHoja

        else:
            operacion = nodo.getValor() 
            nodoIzq = self.copyNodo(nodo.getNodoIzq())
            nodoDer = self.copyNodo(nodo.getNodoDer())
            nuevoNodo = Nodo(operacion,nodoIzq,nodoDer)
            return nuevoNodo
    
    def addRandomNodo(self, nodo_actual,nodo_final):
        if nodo_actual.soyHoja() :
            return True
        
        else:
            if(random.random() > 0.5):
                if self.addRandomNodo(nodo_actual.getNodoIzq(),nodo_final): #Se fue a la izq
                    nodo_actual.setNodoIzquierdo(nodo_final)
            else:
                if self.addRandomNodo(nodo_actual.getNodoDer(),nodo_final):
                    nodo_actual.setNodoDerecho(nodo_final)
    def setRandomNodo(self, nodo_actual,nodo_final):
        if nodo_actual.getNodoDer().soyHoja() and nodo_actual.getNodoIzq().soyHoja():
            return True
        else:
            if((not nodo_actual.getNodoDer().soyHoja()) and (nodo_actual.getNodoIzq().soyHoja())):
                if self.setRandomNodo(nodo_actual.getNodoDer(),nodo_final):
                    nodo_actual.setNodoDerecho(nodo_final)
            elif(( nodo_actual.getNodoDer().soyHoja()) and (not nodo_actual.getNodoIzq().soyHoja())):
                if self.setRandomNodo(nodo_actual.getNodoIzq(),nodo_final): #Se fue a la izq
                        nodo_actual.setNodoIzquierdo(nodo_final)
            else:
                if(random.random() > 0.5):
                    if self.setRandomNodo(nodo_actual.getNodoIzq(),nodo_final): #Se fue a la izq
                        nodo_actual.setNodoIzquierdo(nodo_final)
                else:
                    if self.setRandomNodo(nodo_actual.getNodoDer(),nodo_final):
                        nodo_actual.setNodoDerecho(nodo_final)
    def setRandomHoja(self,nodo_actual,value):
        if(nodo_actual.soyHoja()):
            nodo_actual.setValor(value)
        else:
            if(random.random() > 0.5):
                self.setRandomHoja(nodo_actual.getNodoIzq(),value) #Se fue a la izq
                    
            else:
                self.setRandomHoja(nodo_actual.getNodoDer(),value)
                    
    def setRandomOperation(self,nodo_actual,n_nodos,set_operations):
        if(nodo_actual.soyHoja()):
            print("aca")
            pass
        else:
            rand = random.randint(1,n_nodos)
            if (rand == 1):
                operations = set_operations.copy()
                operations.remove(nodo_actual.getValor())
                operation=random.choice(operations)
                nodo_actual.setValor(operation)
            elif(rand < n_nodos//2 ):
                self.setRandomOperation(nodo_actual.getNodoIzq(),nodo_actual.getNodoIzq().numberHojas()-1,set_operations) #Se fue a la izq
                    
            else:
                self.setRandomOperation(nodo_actual.getNodoDer(),nodo_actual.getNodoDer().numberHojas()-1,set_operations)
    
    # def changeRandomValue(self, nodo_actual,nodo_final):
    #     if nodo_actual.soyHoja() :
    #         return True
        
    #     else:
    #         if(random.random() > 0.5):
    #             if self.addRandomNodo(nodo_actual.getNodoIzq(),nodo_final): #Se fue a la izq
    #                 nodo_actual.setNodoIzquierdo(nodo_final)
    #         else:
    #             if self.addRandomNodo(nodo_actual.getNodoDer(),nodo_final):
    #                 nodo_actual.setNodoDerecho(nodo_final)

    def copy(self):
        copia = Arbol(self.copyNodo(self.raiz))
        return copia

    def getRaiz(self):
        return self.raiz

    def setValueRaiz(self):
        pass
    
    def replaceNodo(self,raiz, nodoIni,nodoFin):
        if raiz.soyHoja():
            return False
        elif raiz == nodoIni:
            return True
        else:
            if self.replaceNodo(raiz.getNodoIzq(),nodoIni,nodoFin):
                raiz.setNodoIzquierdo(nodoFin)
            elif self.replaceNodo(raiz.getNodoDer(),nodoIni,nodoFin):
                raiz.setNodoDerecho(nodoFin)

    def findNodo_nHojas(self,nodo,numero_hojas): ##Cuidado que puede que la cantidad de hojas que se busca no sea exacta en el arbol.
       
          
        if nodo.soyHoja():
            pass
        elif numero_hojas == nodo.numberHojas():
            return nodo
        else:
            nodoIzq = nodo.getNodoIzq()
            nodoDer = nodo.getNodoDer()
            if(random.random() > 0.5):
                self.findNodo_nHojas(nodoIzq, numero_hojas)
                self.findNodo_nHojas(nodoDer, numero_hojas)
            else:
                self.findNodo_nHojas(nodoDer, numero_hojas)
                self.findNodo_nHojas(nodoIzq, numero_hojas)
        


    def evaluate(self,nodo):

        if nodo.soyHoja():
            return nodo.getValor()
        else:
            operacion = nodo.getValor() 
            nodoIzq = self.evaluate(nodo.getNodoIzq())
            nodoDer = self.evaluate(nodo.getNodoDer())

            if operacion == '+':
                return nodoIzq+nodoDer

            elif operacion == '-':
                return nodoIzq-nodoDer

            elif operacion == '*':
                return nodoIzq*nodoDer

            elif operacion == '/':

                return nodoIzq/nodoDer

    def evaluatePoint(self,nodo,x):
        if nodo.soyHoja():
            #print(nodo.getValor())
            if(nodo.getValor() == 'x'):
                return x
            else:
                return nodo.getValor()
        else:
            operacion = nodo.getValor() 
            nodoIzq = self.evaluatePoint(nodo.getNodoIzq(),x)
            nodoDer = self.evaluatePoint(nodo.getNodoDer(),x)

            if operacion == '+':
                return nodoIzq+nodoDer

            elif operacion == '-':
                return nodoIzq-nodoDer

            elif operacion == '*':
                return nodoIzq*nodoDer

            elif operacion == '/':
                return nodoIzq/nodoDer
        
    def imprimir(self,nodo):
        try:
            if nodo.soyHoja():
                return str(nodo.getValor())

            else:
                operacion = nodo.getValor() 
                nodoIzq = self.imprimir(nodo.getNodoIzq())
                nodoDer = self.imprimir(nodo.getNodoDer())
                return '('+nodoIzq+operacion+nodoDer+')'
        except AttributeError:
            return "no soy nodo"

# hoja1 = Hoja(1)
# hoja2 = Hoja(2)
# hoja3 = Hoja(3)
# hoja4 = Hoja(4)
# hoja5 = Hoja(1)


# nodo1 = Nodo('+',hoja1,hoja2)
# nodo2 = Nodo('*',hoja3,hoja4)
# nodo3 = Nodo('/',hoja5,nodo2)

# raiz = Nodo("-",nodo1,nodo3)

# arbol = Arbol(raiz)

# print(arbol.imprimir(arbol.getRaiz()))

# arbol.setRandomHoja(arbol.getRaiz(),15)

# print(arbol.imprimir(arbol.getRaiz()))

# arbol.setRandomOperation(arbol.getRaiz(),arbol.getRaiz().numberHojas()-1,['+','-','*','/'])


# print(arbol.imprimir(arbol.getRaiz()))



# arbol2 = arbol.copy()

# #hoja2.setValor(5)
# arbol.getRaiz().setValor('+')

# # print(arbol.evaluate(arbol.getRaiz()))
# # print(arbol.imprimir(arbol.getRaiz()))
# # print(arbol2.imprimir(arbol2.getRaiz()))

# arbol.replaceNodo(arbol.getRaiz(),nodo2,nodo3)

# print(arbol.imprimir(arbol.getRaiz()))

# nodo4 = Nodo('-',hoja1,Hoja(2))

# arbol.setRandomNodo(arbol.getRaiz(),nodo4)

# print(arbol.imprimir(arbol.getRaiz()))

# print(arbol.imprimir(arbol.findNodo_nHojas(arbol.getRaiz(),4)))
# #print(nodo1.numberHojas())
# #print(arbol.getRaiz().numberHojas())
