import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")
    
    def test_lataaminen_toimii(self):
        self.maksukortti.lataa_rahaa(500)
        self.assertEqual(str(self.maksukortti), "saldo: 15.0")

    def test_nostaminen_toimii_saldo_riittaa(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(str(self.maksukortti), "saldo: 5.0")
    
    def test_nostaminen_toimii_saldo_ei_riita(self):
        self.maksukortti.ota_rahaa(1500)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")   
    
    def test_nostaminen_onnistuu_true(self):
        self.assertTrue(self.maksukortti.ota_rahaa(1))
        self.assertFalse(self.maksukortti.ota_rahaa(10**9))