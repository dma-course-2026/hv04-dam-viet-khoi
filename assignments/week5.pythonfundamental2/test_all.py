import math
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from group1.bai01_so_ban_trong_lop import tinh_so_ban
from group1.bai02_phep_toan_so_hoc import tinh_phep_toan
from group1.bai03_hoan_doi import hoan_doi
from group1.bai04_so_gap_doi import so_gap_doi
from group1.bai05_noi_quy import tinh_chi_phi
from group1.bai06_dien_tich_khu_vuon import dien_tich_con_lai
from group1.bai07_diem_so import xet_diem
from group1.bai08_kiem_tra_ky_tu import la_alphabet
from group1.bai09_tinh_tien_dien import tinh_tien_dien
from group1.bai10_doc_so_3_chu_so import tach_chu_so

from group2.bai11_hinh_vuong import hinh_vuong
from group2.bai12_hinh_chu_nhat import hinh_chu_nhat
from group2.bai13_hinh_tron import hinh_tron
from group2.bai14_hinh_tam_giac import tam_giac
from group2.bai15_tam_giac_deu import la_tam_giac_deu
from group2.bai16_tam_giac_can import la_tam_giac_can
from group2.bai17_tam_giac_vuong import la_tam_giac_vuong
from group2.bai18_pt_bac_1 import giai_pt_bac_1
from group2.bai19_bpt_bac_1 import giai_bpt_bac_1
from group2.bai20_pt_bac_2 import giai_pt_bac_2
from group2.bai21_kiem_tra_chan_le import la_so_chan
from group2.bai22_cung_tinh_chan_le import cung_tinh_chan_le
from group2.bai23_uoc_so_cua_nhau import kiem_tra_uoc
from group2.bai24_min_2_so import tim_min_2
from group2.bai25_max_3_so import tim_max_3
from group2.bai26_max_4_so import tim_max_4
from group2.bai27_min_5_so import tim_min_5
from group2.bai28_thuc_hien_phep_toan import thuc_hien_phep_toan
from group2.bai29_so_ngay_trong_nam import so_ngay_trong_nam
from group2.bai30_doi_gio_phut_giay import doi_gio_phut_giay
from group2.bai31_dong_ho_dien_tu import dong_ho_sau_1_giay
from group2.bai32_he_pt_bac_1_hai_an import giai_he_pt_bac_1
from group2.bai33_diem_thuoc_duong_tron import vi_tri_diem_duong_tron

from group3.bai34_in_so_le import cac_so_le
from group3.bai35_tong_1_den_n import tong_1_den_n
from group3.bai36_tong_so_chan import tong_so_chan
from group3.bai37_tong_so_le import tong_so_le
from group3.bai38_giai_thua import giai_thua
from group3.bai39_luy_thua import luy_thua
from group3.bai40_tong_chia_het_3_hoac_5 import tong_chia_het_3_hoac_5


class TestGroup1(unittest.TestCase):
    def test_bai01(self):
        self.assertEqual(tinh_so_ban(35), 34)
        self.assertEqual(tinh_so_ban(1), 0)
        self.assertEqual(tinh_so_ban(0), 0)

    def test_bai02(self):
        res = tinh_phep_toan(12, 4)
        self.assertEqual(res["tong"], 16)
        self.assertEqual(res["hieu"], 8)
        self.assertEqual(res["tich"], 48)
        self.assertEqual(res["thuong"], 3.0)
        with self.assertRaises(ZeroDivisionError):
            tinh_phep_toan(5, 0)

    def test_bai03(self):
        self.assertEqual(hoan_doi(5, 8), (8, 5))

    def test_bai04(self):
        self.assertEqual(so_gap_doi(7), 14)
        self.assertEqual(so_gap_doi(3.5), 7.0)

    def test_bai05(self):
        self.assertEqual(tinh_chi_phi(1500, 2500, 4000, 2, 4, 1), 17000)

    def test_bai06(self):
        self.assertAlmostEqual(dien_tich_con_lai(10, 20, 3.14), 121.50, places=2)

    def test_bai07(self):
        dtb, kq = xet_diem(5.0, 7.5, 8.5)
        self.assertAlmostEqual(dtb, 7.0, places=1)
        self.assertEqual(kq, "Đậu")
        dtb2, kq2 = xet_diem(3.0, 4.0, 4.5)
        self.assertEqual(kq2, "Rớt")

    def test_bai08(self):
        self.assertTrue(la_alphabet("g"))
        self.assertTrue(la_alphabet("Z"))
        self.assertFalse(la_alphabet("1"))
        self.assertFalse(la_alphabet("@"))
        self.assertFalse(la_alphabet("abc"))

    def test_bai09(self):
        self.assertEqual(tinh_tien_dien(1500, 1580), 460.0)
        self.assertEqual(tinh_tien_dien(0, 50), 250.0)
        self.assertEqual(tinh_tien_dien(0, 200), 1500.0)

    def test_bai10(self):
        self.assertEqual(tach_chu_so(456), (4, 5, 6))


class TestGroup2(unittest.TestCase):
    def test_bai11(self):
        self.assertEqual(hinh_vuong(6), (36.0, 24.0))

    def test_bai12(self):
        self.assertEqual(hinh_chu_nhat(8, 5), (40.0, 26.0))

    def test_bai13(self):
        dt, cv = hinh_tron(3.5, pi=3.14)
        self.assertAlmostEqual(dt, 38.465, places=2)
        self.assertAlmostEqual(cv, 21.98, places=2)

    def test_bai14(self):
        hop_le, cv, dt = tam_giac(3, 4, 5)
        self.assertTrue(hop_le)
        self.assertEqual(cv, 12.0)
        self.assertEqual(dt, 6.0)
        self.assertFalse(tam_giac(1, 2, 10)[0])

    def test_bai15(self):
        self.assertTrue(la_tam_giac_deu(5, 5, 5))
        self.assertFalse(la_tam_giac_deu(5, 5, 6))

    def test_bai16(self):
        self.assertTrue(la_tam_giac_can(5, 5, 8))
        self.assertFalse(la_tam_giac_can(3, 4, 5))

    def test_bai17(self):
        self.assertTrue(la_tam_giac_vuong(3, 4, 5))
        self.assertFalse(la_tam_giac_vuong(5, 5, 5))

    def test_bai18(self):
        self.assertEqual(giai_pt_bac_1(2, -4), ("MOT_NGHIEM", 2.0))
        self.assertEqual(giai_pt_bac_1(0, 0), ("VO_SO_NGHIEM", None))
        self.assertEqual(giai_pt_bac_1(0, 5), ("VO_NGHIEM", None))

    def test_bai19(self):
        self.assertEqual(giai_bpt_bac_1(3, -9), ("NGHIEM", "x >= 3.0"))
        self.assertEqual(giai_bpt_bac_1(-2, 4), ("NGHIEM", "x <= 2.0"))
        self.assertEqual(giai_bpt_bac_1(0, 5), ("VO_SO_NGHIEM", "Đúng với mọi x"))
        self.assertEqual(giai_bpt_bac_1(0, -5), ("VO_NGHIEM", "Vô nghiệm"))

    def test_bai20(self):
        tt1, ng1 = giai_pt_bac_2(1, -3, 2)
        self.assertEqual(tt1, "HAI_NGHIEM")
        self.assertEqual(ng1, [2.0, 1.0])
        tt2, ng2 = giai_pt_bac_2(1, -2, 1)
        self.assertEqual(tt2, "NGHIEM_KEP")
        self.assertEqual(ng2, [1.0])
        tt3, ng3 = giai_pt_bac_2(1, 0, 1)
        self.assertEqual(tt3, "VO_NGHIEM")
        self.assertEqual(ng3, [])

    def test_bai21(self):
        self.assertFalse(la_so_chan(7))
        self.assertTrue(la_so_chan(8))

    def test_bai22(self):
        self.assertTrue(cung_tinh_chan_le(6, 8))
        self.assertFalse(cung_tinh_chan_le(5, 8))

    def test_bai23(self):
        self.assertEqual(kiem_tra_uoc(6, 18), (True, False))
        self.assertEqual(kiem_tra_uoc(0, 5), (False, True))
        self.assertEqual(kiem_tra_uoc(0, 0), (False, False))

    def test_bai24(self):
        self.assertEqual(tim_min_2(15, 8), 8)

    def test_bai25(self):
        self.assertEqual(tim_max_3(10, 22, 15), 22)

    def test_bai26(self):
        self.assertEqual(tim_max_4(10, 22, 15, 45), 45)

    def test_bai27(self):
        self.assertEqual(tim_min_5(3.5, 1.2, 4.8, -2.5, 0.0), -2.5)

    def test_bai28(self):
        self.assertEqual(thuc_hien_phep_toan(10, 5, "+"), 15.0)
        self.assertEqual(thuc_hien_phep_toan(10, 5, "-"), 5.0)
        self.assertEqual(thuc_hien_phep_toan(10, 5, "*"), 50.0)
        self.assertEqual(thuc_hien_phep_toan(10, 5, "/"), 2.0)
        self.assertEqual(thuc_hien_phep_toan(10, 0, "/"), "Không thể chia cho 0")

    def test_bai29(self):
        self.assertEqual(so_ngay_trong_nam(2024), 366)
        self.assertEqual(so_ngay_trong_nam(2023), 365)
        self.assertEqual(so_ngay_trong_nam(2000), 366)
        self.assertEqual(so_ngay_trong_nam(1900), 365)

    def test_bai30(self):
        self.assertEqual(doi_gio_phut_giay(3665), (1, 1, 5))

    def test_bai31(self):
        self.assertEqual(dong_ho_sau_1_giay(23, 59, 58), (23, 59, 59))
        self.assertEqual(dong_ho_sau_1_giay(23, 59, 59), (0, 0, 0))

    def test_bai32(self):
        tt, sol = giai_he_pt_bac_1(2, 3, 8, 4, -1, -1)
        self.assertEqual(tt, "NGHIEM_DUY_NHAT")
        self.assertIsNotNone(sol)
        x, y = sol
        self.assertAlmostEqual(x, 5 / 14, places=3)
        self.assertAlmostEqual(y, 17 / 7, places=3)

    def test_bai33(self):
        self.assertEqual(vi_tri_diem_duong_tron(0, 0, 5, 3, 4), "TRON")
        self.assertEqual(vi_tri_diem_duong_tron(0, 0, 5, 1, 1), "TRONG")
        self.assertEqual(vi_tri_diem_duong_tron(0, 0, 5, 6, 6), "NGOAI")


class TestGroup3(unittest.TestCase):
    def test_bai34(self):
        self.assertEqual(cac_so_le(9), [1, 3, 5, 7, 9])
        self.assertEqual(cac_so_le(10), [1, 3, 5, 7, 9])

    def test_bai35(self):
        self.assertEqual(tong_1_den_n(10), 55)

    def test_bai36(self):
        self.assertEqual(tong_so_chan(10), 30)

    def test_bai37(self):
        self.assertEqual(tong_so_le(10), 25)

    def test_bai38(self):
        self.assertEqual(giai_thua(5), 120)
        self.assertEqual(giai_thua(0), 1)

    def test_bai39(self):
        self.assertEqual(luy_thua(2, 10), 1024)

    def test_bai40(self):
        self.assertEqual(tong_chia_het_3_hoac_5(10, 20), 75)


if __name__ == "__main__":
    unittest.main()
