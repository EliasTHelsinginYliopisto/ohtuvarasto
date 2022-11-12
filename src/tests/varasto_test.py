import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_lisaa_negatiivinen_maara(self):
        self.varasto.lisaa_varastoon(-2)

        #ei voi lisää negatiivista lukua
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)
    
    def test_lisaa_liikaa(self):
        self.varasto.lisaa_varastoon(20)

        #ei voi lisää liikaa
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_virheellinen_varasto_koko(self):
        varasto = Varasto(-10)

        #varaston tila on luvun itseisarvo
        self.assertAlmostEqual(varasto.paljonko_mahtuu(),10)
    
    def test_virheellinen_varasto_saldo(self):
        varasto = Varasto(10, alku_saldo=-10)

        #negatiivinen saldo muuttuu nollaksi
        self.assertAlmostEqual(varasto.paljonko_mahtuu(),0)

    def test_virheellinen_varasto_saldo(self):
        varasto = Varasto(10, alku_saldo=20)

        self.assertAlmostEqual(varasto.saldo,10)

    def test_ota_virheellisesti(self):
        
        #negatiivisilla luvuilla ei oteta
        self.assertAlmostEqual(self.varasto.ota_varastosta(-5),0)

    def test_ota_liikaa(self):
        self.varasto.lisaa_varastoon(5)

        #otetaan kaikki mitä voidaan
        self.assertAlmostEqual(self.varasto.ota_varastosta(100),5)
    
    def test_str_toimii(self):
        output = "saldo = 0, vielä tilaa 10"

        self.assertEqual(self.varasto.__str__(),output )



    