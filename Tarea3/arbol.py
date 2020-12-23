import random

# Class to create nodo

class Nodo:

    # Contructor of the nodo, receives:
    # valor: Its the valor of the nodo
    # nodoIzquierdo: Its a reference of a nodo
    # nodoDerecho: Its a reference of a nodo

    def __init__(self,valor,nodoIzquierdo,nodoDerecho):

        self.valor = valor
        self.nodoIzquierdo = nodoIzquierdo
        self.nodoDerecho = nodoDerecho

    # Sets Value of the nodo
    
    def setValor(self, valor):
        self.valor = valor

    # Checks it is leaf the nodo

    def soyHoja(self):
        return False

    # Sets left nodo with a nodo

    def setNodoIzquierdo(self,nodoIzquierdo):
        self.nodoIzquierdo = nodoIzquierdo

    # Sets right nodo with a nodo

    def setNodoDerecho(self,nodoDerecho):
        self.nodoDerecho = nodoDerecho
    
    # Gets left nodo

    def getNodoIzq(self):
        return self.nodoIzquierdo

    # Gets right nodo

    def getNodoDer(self):
        return self.nodoDerecho

    # Gets value

    def getValor(self):
        return self.valor
    
    # Returns number of leafs of the nodo

    def numberHojas(self):
        if self.soyHoja():
            return 1
        else:
            c = self.getNodoDer().numberHojas()
            c += self.getNodoIzq().numberHojas()
            return c
    

# Hoja, its subclass of nodo

class Hoja(Nodo):

    # Contructor of the Hoja, receives:
    # valor: Its the valor of the nodo
    
    def __init__(self,valor):
        super().__init__(valor,None,None)

    # Checks its is leaf

    def soyHoja(self):
        
        return True

# Class Arbol to operate nodes

class Arbol:

    # Contructor of the Arbol, receives:
    # raiz: Its the root of the tree

    def __init__(self,raiz):
        self.raiz = raiz

    # Copy a nodo and his nodes
    
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
    
    # Add random nodo in a leaf

    def addRandomNodo(self, nodo_actual,nodo_final):
        if nodo_actual.soyHoja() :
            return True
        
        else:
            if(random.random() > 0.5):
                if self.addRandomNodo(nodo_actual.getNodoIzq(),nodo_final): 
                    nodo_actual.setNodoIzquierdo(nodo_final)
            else:
                if self.addRandomNodo(nodo_actual.getNodoDer(),nodo_final):
                    nodo_actual.setNodoDerecho(nodo_final)

    # Sets random nodo in a nodo that has 2 leaf

    def setRandomNodo(self, nodo_actual,nodo_final):
        if nodo_actual.getNodoDer().soyHoja() and nodo_actual.getNodoIzq().soyHoja():
            return True
        else:
            if((not nodo_actual.getNodoDer().soyHoja()) and (nodo_actual.getNodoIzq().soyHoja())):
                if self.setRandomNodo(nodo_actual.getNodoDer(),nodo_final):
                    nodo_actual.setNodoDerecho(nodo_final)
            elif(( nodo_actual.getNodoDer().soyHoja()) and (not nodo_actual.getNodoIzq().soyHoja())):
                if self.setRandomNodo(nodo_actual.getNodoIzq(),nodo_final):
                        nodo_actual.setNodoIzquierdo(nodo_final)
            else:
                if(random.random() > 0.5):
                    if self.setRandomNodo(nodo_actual.getNodoIzq(),nodo_final): 
                        nodo_actual.setNodoIzquierdo(nodo_final)
                else:
                    if self.setRandomNodo(nodo_actual.getNodoDer(),nodo_final):
                        nodo_actual.setNodoDerecho(nodo_final)

    # Sets random hoja

    def setRandomHoja(self,nodo_actual,value):
        if(nodo_actual.soyHoja()):
            nodo_actual.setValor(value)
        else:
            if(random.random() > 0.5):
                self.setRandomHoja(nodo_actual.getNodoIzq(),value)
                    
            else:
                self.setRandomHoja(nodo_actual.getNodoDer(),value)
    
    # Sets Random Operation in anyone nodo

    def setRandomOperation(self,nodo_actual,n_nodos,set_operations):
        if(nodo_actual.soyHoja()):
            pass
        else:
            rand = random.randint(1,n_nodos)
            if (rand == 1):
                operations = set_operations.copy()
                operations.remove(nodo_actual.getValor())
                operation=random.choice(operations)
                nodo_actual.setValor(operation)
            elif(rand < n_nodos//2 ):
                self.setRandomOperation(nodo_actual.getNodoIzq(),nodo_actual.getNodoIzq().numberHojas()-1,set_operations) 
                    
            else:
                self.setRandomOperation(nodo_actual.getNodoDer(),nodo_actual.getNodoDer().numberHojas()-1,set_operations)

    # Copy an arbol

    def copy(self):
        copia = Arbol(self.copyNodo(self.raiz))
        return copia

    # Gets Raiz (root)

    def getRaiz(self):
        return self.raiz

    # Replace a Nodo given for another
    
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

    # Find a Nodo with a certain number of hojas (leafs)

    def findNodo_nHojas(self,nodo,numero_hojas): 
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
        

    # Evaluate a nodo with only numbers in the leafs

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
    
    # Evaluate a three with numbers and 'x'

    def evaluatePoint(self,nodo,x):
        if nodo.soyHoja():
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
        
    # Returns a string of the tree

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