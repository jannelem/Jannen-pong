import unittest
from maksukortti import Maksukortti
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(1000)
        self.koyhan_kortti = Maksukortti(100)

    def test_uuden_paatteen_saldo_oikein(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_uuden_paatteen_edulliset_oikein(self):
        self.assertEqual(self.kassa.edulliset, 0)

    def test_uuden_paatteen_maukkaat_oikein(self):
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_syo_edullisesti_kateisella_kasvattaa_saldoa(self):
        self.kassa.syo_edullisesti_kateisella(250)
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)

    def test_syo_edullisesti_kateisella_kasvattaa_lounaiden_maaraa(self):
        self.kassa.syo_edullisesti_kateisella(250)
        self.assertEqual(self.kassa.edulliset, 1)
    
    def test_syo_edullisesti_palauttaa_vaihtorahan_oikein(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(250), 10)
    
    def test_syo_edullisesti_kateisella_palauttaa_kaiken_jos_raha_ei_riita(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(230), 230)
    
    def test_syo_edullisesti_kateisella_ei_muuta_saldoa_jos_raha_ei_riita(self):
        self.kassa.syo_edullisesti_kateisella(230)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    
    def test_syo_edullisesti_kateisella_ei_muuta_maaraa_jos_raha_ei_riita(self):
        self.kassa.syo_edullisesti_kateisella(230)
        self.assertEqual(self.kassa.edulliset, 0)

    def test_syo_maukkaasti_kateisella_kasvattaa_saldoa(self):
        self.kassa.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)

    def test_syo_maukkaasti_kateisella_kasvattaa_lounaiden_maaraa(self):
        self.kassa.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassa.maukkaat, 1)
    
    def test_syo_maukkaasti_palauttaa_vaihtorahan_oikein(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(500), 100)
    
    def test_syo_maukkaasti_kateisella_palauttaa_kaiken_jos_raha_ei_riita(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(350), 350)
    
    def test_syo_maukkaasti_kateisella_ei_muuta_saldoa_jos_raha_ei_riita(self):
        self.kassa.syo_maukkaasti_kateisella(350)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    
    def test_syo_edullisesti_kateisella_ei_muuta_maaraa_jos_raha_ei_riita(self):
        self.kassa.syo_edullisesti_kateisella(350)
        self.assertEqual(self.kassa.maukkaat, 0)
    
    def test_syo_edullisesti_kortilla_vahentaa_kortin_saldoa(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 7.60 euroa")

    def test_syo_edullisesti_kortilla_palauttaa_true(self):
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.kortti), True)
    
    def test_syo_edullisesti_kortilla_kasvattaa_maaraa(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.edulliset, 1)
    
    def test_syo_edullisesti_kortilla_palauttaa_false(self):
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.koyhan_kortti), False)
    
    def test_syo_edullisesti_kortilla_ei_vahenna_saldoa(self):
        self.kassa.syo_edullisesti_kortilla(self.koyhan_kortti)
        self.assertEqual(str(self.koyhan_kortti), "Kortilla on rahaa 1.00 euroa")

    def test_syo_edullisesti_kortilla_ei_kasvata_maaraa(self):
        self.kassa.syo_edullisesti_kortilla(self.koyhan_kortti)
        self.assertEqual(self.kassa.edulliset, 0)
    
    def test_syo_maukkaasti_kortilla_vahentaa_kortin_saldoa(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 6.00 euroa")

    def test_syo_maukkaasti_kortilla_palauttaa_true(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(self.kortti), True)
    
    def test_syo_maukkaasti_kortilla_kasvattaa_maaraa(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.maukkaat, 1)
    
    def test_syo_maukkaasti_kortilla_palauttaa_false(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(self.koyhan_kortti), False)
    
    def test_syo_maukkaasti_kortilla_ei_vahenna_saldoa(self):
        self.kassa.syo_maukkaasti_kortilla(self.koyhan_kortti)
        self.assertEqual(str(self.koyhan_kortti), "Kortilla on rahaa 1.00 euroa")

    def test_syo_maukkaasti_kortilla_ei_kasvata_maaraa(self):
        self.kassa.syo_maukkaasti_kortilla(self.koyhan_kortti)
        self.assertEqual(self.kassa.edulliset, 0)

    def test_kassan_saldo_ei_muutu_kortilla(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.kassa.syo_maukkaasti_kortilla(self.kortti)  
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    
    def test_kortin_lataus_muuttaa_kassan_saldoa(self):
        self.kassa.lataa_rahaa_kortille(self.koyhan_kortti, 900)
        self.assertEqual(self.kassa.kassassa_rahaa, 100900)
    
    def test_kortin_lataus_muuttaa_kortin_saldoa(self):
        self.kassa.lataa_rahaa_kortille(self.koyhan_kortti, 900)
        self.assertEqual(str(self.koyhan_kortti), "Kortilla on rahaa 10.00 euroa")
    
    def test_negatiivinen_lataus_ei_muuta_kassan_saldoa(self):
        self.kassa.lataa_rahaa_kortille(self.koyhan_kortti, -10000)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_negatiivinen_lataus_ei_muuta_kortin_saldoa(self):
        self.kassa.lataa_rahaa_kortille(self.koyhan_kortti, -10000)
        self.assertEqual(str(self.koyhan_kortti), "Kortilla on rahaa 1.00 euroa")