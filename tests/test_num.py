import unittest
from controller import num_words as nw


class TestNumWords(unittest.TestCase):
    """Teste para verificar possiveis condicoes"""
    
    def test_ones(self):
        self.assertEqual(nw(-1), 'menos um')
        self.assertEqual(nw(0), 'zero')
        self.assertEqual(nw(1), 'um')
        self.assertEqual(nw(2), 'dois')
        self.assertEqual(nw(3), 'tres')
        self.assertEqual(nw(4), 'quatro')
        self.assertEqual(nw(5), 'cinco')
        self.assertEqual(nw(6), 'seis')
        self.assertEqual(nw(7), 'sete')
        self.assertEqual(nw(8), 'oito')
        self.assertEqual(nw(9), 'nove')        

    def test_tens(self):
        self.assertEqual(nw(-10), 'menos dez')
        self.assertEqual(nw(10), 'dez')
        self.assertEqual(nw(11), 'onze')
        self.assertEqual(nw(12), 'doze')
        self.assertEqual(nw(13), 'treze')
        self.assertEqual(nw(14), 'catorze')
        self.assertEqual(nw(15), 'quinze')
        self.assertEqual(nw(16), 'dezesseis')
        self.assertEqual(nw(17), 'dezessete')
        self.assertEqual(nw(18), 'dezoito')
        self.assertEqual(nw(19), 'dezenove')        

    def test_decs(self):
        self.assertEqual(nw(-20), 'menos vinte')
        self.assertEqual(nw(20), 'vinte')
        self.assertEqual(nw(21), 'vinte e um')
        self.assertEqual(nw(99), 'noventa e nove')

    def test_hunds(self):
        self.assertEqual(nw(-101), 'menos cento e um')
        self.assertEqual(nw(-100), 'menos cem')
        self.assertEqual(nw(100), 'cem')
        self.assertEqual(nw(101), 'cento e um')
        self.assertEqual(nw(110), 'cento e dez')
        self.assertEqual(nw(111), 'cento e onze')
        self.assertEqual(nw(120), 'cento e vinte')
        self.assertEqual(nw(121), 'cento e vinte e um')
        self.assertEqual(nw(199), 'cento e noventa e nove')

        self.assertEqual(nw(200), 'duzentos')
        self.assertEqual(nw(201), 'duzentos e um')
        self.assertEqual(nw(210), 'duzentos e dez')
        self.assertEqual(nw(211), 'duzentos e onze')
        self.assertEqual(nw(220), 'duzentos e vinte')
        self.assertEqual(nw(221), 'duzentos e vinte e um')
        self.assertEqual(nw(299), 'duzentos e noventa e nove')
        self.assertEqual(nw(300), 'trezentos')
        self.assertEqual(nw(400), 'quatrocentos')
        self.assertEqual(nw(500), 'quinhentos')
        self.assertEqual(nw(600), 'seiscentos')
        self.assertEqual(nw(700), 'setecentos')
        self.assertEqual(nw(800), 'oitocentos')
        self.assertEqual(nw(900), 'novecentos')
        self.assertEqual(nw(999), 'novecentos e noventa e nove')

    def test_thous(self):
        self.assertEqual(nw(-999999), 'Numero fora do intervalo')
        self.assertEqual(nw(-99101), 'menos noventa e nove mil e cento e um')
        self.assertEqual(nw(-1000), 'menos mil')
        self.assertEqual(nw(1000), 'mil')
        self.assertEqual(nw(1001), 'mil e um')
        self.assertEqual(nw(1010), 'mil e dez')
        self.assertEqual(nw(1101), 'mil e cento e um')
        self.assertEqual(nw(2000), 'dois mil')
        self.assertEqual(nw(2001), 'dois mil e um')
        self.assertEqual(nw(2010), 'dois mil e dez')
        self.assertEqual(nw(2011), 'dois mil e onze')
        self.assertEqual(nw(2020), 'dois mil e vinte')
        self.assertEqual(nw(2021), 'dois mil e vinte e um')

        self.assertEqual(nw(10000), 'dez mil')
        self.assertEqual(nw(11000), 'onze mil')
        self.assertEqual(nw(20000), 'vinte mil')
        self.assertEqual(nw(90000), 'noventa mil')        
        self.assertEqual(nw(90001), 'noventa mil e um')
        self.assertEqual(nw(90010), 'noventa mil e dez')
        self.assertEqual(nw(90011), 'noventa mil e onze')
        self.assertEqual(nw(90100), 'noventa mil e cem')
        self.assertEqual(nw(90101), 'noventa mil e cento e um')
        self.assertEqual(nw(90120), 'noventa mil e cento e vinte')
        self.assertEqual(nw(90121), 'noventa mil e cento e vinte e um') 
        self.assertEqual(nw(91000), 'noventa e um mil')
        self.assertEqual(nw(99101), 'noventa e nove mil e cento e um')
        self.assertEqual(nw(999999), 'Numero fora do intervalo')


if __name__ == '__main__':
    unittest.main()
