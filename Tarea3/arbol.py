class Nodo:
    def __init__(self,valor,nodoIzquierdo,nodoDerecho):

        self.valor = valor
        self.nodoIzquierdo = nodoIzquierdo
        self.nodoDerecho = nodoDerecho
    
    def setValor(self, valor):
        self.valor = valor

    def soyHoja(self):
        return False

    def setNodos(self,nodoIzquierdo,nodoDerecho):
        self.nodoIzquierdo = nodoIzquierdo
        self.nodoDerecho = nodoDerecho
    
    def getNodoIzq(self):
        return self.nodoIzquierdo

    def getNodoDer(self):
        return self.nodoDerecho

    def getValor(self):
        return self.valor


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
    
    def copy(self):
        copia = Arbol(self.copyNodo(self.raiz))
        return copia

    def getRaiz(self):
        return self.raiz

    def setValueRaiz(self):
        pass

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
        
    def imprimir(self,nodo):

        if nodo.soyHoja():
            return str(nodo.getValor())

        else:
            operacion = nodo.getValor() 
            nodoIzq = self.imprimir(nodo.getNodoIzq())
            nodoDer = self.imprimir(nodo.getNodoDer())
            return nodoIzq+operacion+nodoDer


hoja1 = Hoja(1)
hoja2 = Hoja(2)
hoja3 = Hoja(3)
hoja4 = Hoja(4)

nodo1 = Nodo('+',hoja1,hoja2)
nodo2 = Nodo('*',hoja3,hoja4)
raiz = Nodo("-",nodo1,nodo2)

arbol = Arbol(raiz)
arbol2 = arbol.copy()

hoja2.setValor(5)
arbol.getRaiz().setValor('+')

print(arbol.evaluate(arbol.getRaiz()))
print(arbol.imprimir(arbol.getRaiz()))
print(arbol2.imprimir(arbol2.getRaiz()))
