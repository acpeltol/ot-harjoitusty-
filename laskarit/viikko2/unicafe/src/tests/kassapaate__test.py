import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_kassapaatteen_saldo_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edulliset_lounaat(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_maukkaat_lounaat(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisosto_edullinen_toimii(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(250), 10)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kateisosto_maukas_toimii(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(450), 50)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kateisosto_edullinen_ei_riita(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(230), 230)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kateisosto_maukas_ei_riita(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(390), 390)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kortti_toimii_edullinen(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)
        self.assertEqual(self.maksukortti.saldo, 760)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kortti_toimii_maukas(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)
        self.assertEqual(self.maksukortti.saldo, 600)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 1)    

    def test_kortti_ei_riita_edullinen(self):
        self.maksukortti.ota_rahaa(800)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), False)
        self.assertEqual(self.maksukortti.saldo, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kortti_ei_riita_maukas(self):
        self.maksukortti.ota_rahaa(800)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), False)
        self.assertEqual(self.maksukortti.saldo, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kortille_lataaminen_toimii(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(self.maksukortti.saldo, 2000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)

    def test_kortille_lataaminen_negatiivinen_summa_ei_toimi(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1000)
        self.assertEqual(self.maksukortti.saldo, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kassassa_rahaa_euroina(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
    
