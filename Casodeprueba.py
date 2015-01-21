'''
Created on Jan 18, 2015

@author: maria-esthervidal
Se considera la tarifa diurna desde las 6:00 hasta 18:00
Se considera la tarifa nocturna desde las 18:01 hasta 05:59
'''

import unittest
from Tarifa import *
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

class TestFecha(unittest.TestCase):
    
    def testresv(self):
        
        formato = '%d/%m/%Y %H:%M'
        
        #Frontera
        fi = datetime.strptime("01/01/2015 16:30", formato)
        ff = datetime.strptime("01/01/2015 16:45", formato)
        tarifa = CalcularTarifa(fi, ff, 50, 100)
        self.assertEquals(tarifa, 50)
        
        #Frontera
        fi = datetime.strptime("01/01/2015 04:30", formato)
        ff = datetime.strptime("01/01/2015 04:45", formato)
        tarifa = CalcularTarifa(fi, ff, 50, 100)
        self.assertEquals(tarifa, 100)
        
        #Frontera
        fi = datetime.strptime("01/01/2015 05:00", formato)
        ff = datetime.strptime("04/01/2015 05:00", formato)
        tarifa = CalcularTarifa(fi, ff, 50, 100)
        self.assertEquals(tarifa, 5400)
        
        #Esquina y Frontera
        fi = datetime.strptime("01/01/2015 05:45", formato)
        ff = datetime.strptime("01/01/2015 6:00", formato)
        tarifa = CalcularTarifa(fi, ff, 50, 100)
        self.assertEquals(tarifa, 100)
        
        #Esquina y Frontera
        fi = datetime.strptime("01/01/2015 17:45", formato)
        ff = datetime.strptime("01/01/2015 18:00", formato)
        tarifa = CalcularTarifa(fi, ff, 50, 100)
        self.assertEquals(tarifa, 50)
        
        #Esquina y Frontera
        fi = datetime.strptime("01/01/2015 17:46", formato)
        ff = datetime.strptime("01/01/2015 18:01", formato)
        tarifa = CalcularTarifa(fi, ff, 50, 100)
        self.assertEquals(tarifa, 100)
        
        #Esquina 
        fi = datetime.strptime("01/01/2015 06:00", formato)
        ff = datetime.strptime("01/01/2015 18:00", formato)
        tarifa = CalcularTarifa(fi, ff, 50, 100)
        self.assertEquals(tarifa, 600)
        
        #Esquina
        fi = datetime.strptime("01/01/2015 06:00", formato)
        ff = datetime.strptime("02/01/2015 06:00", formato)
        tarifa = CalcularTarifa(fi, ff, 50, 100)
        self.assertEquals(tarifa, 1800)
        
        #Esquina
        fi = datetime.strptime("01/01/2015 17:00", formato)
        ff = datetime.strptime("01/01/2015 18:01", formato)
        tarifa = CalcularTarifa(fi, ff, 50, 100)
        self.assertEquals(tarifa, 150)
        
        #Esquina
        fi = datetime.strptime("01/01/2015 17:00", formato)
        ff = datetime.strptime("01/01/2015 18:00", formato)
        tarifa = CalcularTarifa(fi, ff, 50, 100)
        self.assertEquals(tarifa, 50)
        
        #Esquina
        fi = datetime.strptime("01/01/2015 18:01", formato)
        ff = datetime.strptime("02/01/2015 05:59", formato)
        tarifa = CalcularTarifa(fi, ff, 50, 100)
        self.assertEquals(tarifa, 1200)
        
        #Esquina y Frontera
        fi = datetime.strptime("01/01/2015 18:00", formato)
        ff = datetime.strptime("04/01/2015 18:00", formato)
        tarifa = CalcularTarifa(fi, ff, 50, 100)
        self.assertEquals(tarifa, 5400)
        
        #Esquina y Frontera
        fi = datetime.strptime("01/01/2015 06:00", formato)
        ff = datetime.strptime("04/01/2015 06:00", formato)
        tarifa = CalcularTarifa(fi, ff, 50, 100)
        self.assertEquals(tarifa, 5400)
        
        #Esquina
        fi = datetime.strptime("01/01/2015 18:00", formato)
        ff = datetime.strptime("04/01/2015 06:00", formato)
        tarifa = CalcularTarifa(fi, ff, 50, 100)
        self.assertEquals(tarifa, 4800)
        
        #Frontera
        fi = datetime.strptime("01/01/2015 17:00", formato)
        ff = datetime.strptime("01/01/2015 17:10", formato)
        tarifa = CalcularTarifa(fi, ff, 50, 100)
        self.assertEquals(tarifa, 0)
        
        #Frontera
        fi = datetime.strptime("01/01/2015 18:00", formato)
        ff = datetime.strptime("05/01/2015 18:00", formato)
        tarifa = CalcularTarifa(fi, ff, 50, 100)
        self.assertEquals(tarifa, 0)
        