from unittest import TestCase
from arbol import Nodo,Hoja,Arbol
class TestNodo(TestCase):
    def setUp(self):
        self.hoja1 = Hoja(1)
        self.hoja2 = Hoja(2)
        self.nodo = Nodo("*",self.hoja1,self.hoja2) 
    def test_soyHoja(self):
        self.assert_(self.hoja1.soyHoja())
        self.assertFalse(self.nodo.soyHoja())
    
    def test_getValor(self):
        self.assertEquals(self.hoja1.getValor(),1)
        self.assertEquals(self.hoja2.getValor(),2)
        self.assertEquals(self.nodo.getValor(),"*")
    def test_setValor(self):
        self.hoja1.setValor(11)
        self.hoja2.setValor(22)
        self.nodo.setValor("+")
        self.assertEquals(self.hoja1.getValor(),11)
        self.assertEquals(self.hoja2.getValor(),22)
        self.assertEquals(self.nodo.getValor(),"+")
    
    def test_getNodoIzq(self):
        self.assertEquals(self.nodo.getNodoIzq(),self.hoja1)
    def test_setNodoIzq(self):
        hoja3=Hoja(3)
        self.nodo.setNodoIzquierdo(hoja3)
        self.assertEquals(self.nodo.getNodoIzq(),hoja3)
    
    def test_getNodoDer(self):
        self.assertEquals(self.nodo.getNodoDer(),self.hoja2)
    def test_setNodoDer(self):
        hoja3=Hoja(3)
        self.nodo.setNodoDerecho(hoja3)
        self.assertEquals(self.nodo.getNodoDer(),hoja3)
    def test_numberHojas(self):
        self.assertEquals(self.nodo.numberHojas(),2)
class TestArbol(TestCase):
    def setUp(self)
        self.hoja1 = Hoja(1)
        self.hoja2 = Hoja(2)
        self.nodo = Nodo("*",self.hoja1,self.hoja2) 
        self.arbol=Arbol(nodo)
    def test_getRaiz(self):
        raiz=self.arbol.getRaiz()
        self.assertEquals(raiz,nodo)
    def test_copy(self):
        arbol_copy =self.arbol.copy()
        self.assertEquals(self.arbol.getRaiz().getValor(),arbol_copy.getRaiz().getValor())
        self.assertEquals(self.arbol.getRaiz().getNodoIzq().getValor(),arbol_copy.getRaiz().getNodoIzq().getValor())
        self.assertEquals(self.arbol.getRaiz().getNodoDer().getValor(),arbol_copy.getRaiz().getNodoDer().getValor())
    def test_replaceNodo(self):
        hoja3=Hoja(3)
        self.arbol.replaceNodo(self.nodo,self.hoja1,hoja3)
        self.assertEquals(self.arbol.getRaiz().getNodoIzq(),hoja3)
    def test_findNodo_nHojas(self):
        node=self.arbol.findNodo_nHojas(self.nodo,2)
        self.assertEquals(self.nodo,node)
    def test_evaluate(self):
        valor=self.arbol.evaluate(self.nodo)
        self.assertEquals(valor,2)
    def test_evaluatePoint(self):
        hoja1 = Hoja('x')
        hoja2 = Hoja(5)
        nodo = Nodo("*",hoja1,hoja2)
        arbol=Arbol(nodo)
        value=arbol.evaluatePoint(nodo,5)
        self.assertEquals(25,value)

    def test_imprimir(self):
        imprimir=self.arbol,imprimir(self.nodo)
        self.assertEquals('(1*2)',imprimir)
    