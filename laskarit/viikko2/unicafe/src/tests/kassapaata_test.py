import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self) -> None:
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)
    
    def test_luotu_paate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)
    
    def test_parametrit_alussa_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisosto_toimii_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_kateinen_ei_riita_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella(0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_kateisosto_toimii_maukas(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kateinen_ei_riita_maukas(self):
        self.kassapaate.syo_maukkaasti_kateisella(0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_syo_maukkasti_kortilla_toimii(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(str(self.maksukortti), "saldo: 6.0")
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti))
    
    def test_kortilla_ei_saldoa_syo_maukkaasti(self):
        self.maksukortti.saldo = 100
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(str(self.maksukortti), "saldo: 1.0")
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti))


    def test_syo_edullisesti_kortilla_toimii(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(str(self.maksukortti), "saldo: 7.6")
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti))

    def test_kortilla_ei_saldoa_syo_edullisesti(self):
        self.maksukortti.saldo = 100
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(str(self.maksukortti), "saldo: 1.0")
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti))

    def test_rahan_lataaminen_toimii(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)
        self.assertEqual(str(self.maksukortti), "saldo: 20.0")

    def test_ei_voi_ladata_negatiivista_summaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")
