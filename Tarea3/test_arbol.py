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
        self.nodo.setNodoIzq()