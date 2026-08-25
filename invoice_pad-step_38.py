# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: InvoicePad
import unittest


class TestEdgeCases(unittest.TestCase):
    def setUp(self):
        from invoicepad import InvoicePad
        self.pad = InvoicePad()

    def test_invalid_client_id(self):
        self.assertIsNone(self.pad.get_client("999"))

    def test_invalid_invoice_id(self):
        self.assertIsNone(self.pad.get_invoice("999"))

    def test_invalid_payment_id(self):
        self.assertIsNone(self.pad.get_payment("999"))

    def test_invalid_note_id(self):
        self.assertIsNone(self.pad.get_note("999"))

    def test_empty_note(self):
        self.assertIsNone(self.pad.get_note(None))

    def test_empty_invoice(self):
        self.assertIsNone(self.pad.get_invoice(None))

    def test_empty_payment(self):
        self.assertIsNone(self.pad.get_payment(None))

    def test_empty_client(self):
        self.assertIsNone(self.pad.get_client(None))

    def test_invalid_due_date(self):
        self.assertIsNone(self.pad.get_due_date("2024-13-01"))

    def test_invalid_due_date_2(self):
        self.assertIsNone(self.pad.get_due_date("2024-00-01"))

    def test_invalid_due_date_3(self):
        self.assertIsNone(self.pad.get_due_date("2024-32-01"))

    def test_invalid_due_date_4(self):
        self.assertIsNone(self.pad.get_due_date("abc"))

    def test_invalid_due_date_5(self):
        self.assertIsNone(self.pad.get_due_date(""))

    def test_invalid_due_date_6(self):
        self.assertIsNone(self.pad.get_due_date(None))

    def test_zero_due_days(self):
        self.assertEqual(self.pad.get_due_date("2024-01-01", 0), "2024-01-01")

    def test_negative_due_days(self):
        self.assertEqual(self.pad.get_due_date("2024-01-01", -1), "2023-12-31")

    def test_leap_year_due_date(self):
        self.assertEqual(self.pad.get_due_date("2024-02-28", 1), "2024-02-29")

    def test_leap_year_due_date_2(self):
        self.assertEqual(self.pad.get_due_date("2024-02-28", 2), "2024-03-01")


if __name__ == "__main__":
    unittest.main()
