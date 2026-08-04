# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: InvoicePad
import unittest


def test_invoicepad_units():
    from invoice import Invoice, Payment, Client, Ledger, LedgerEntry

    # --- Client ---
    c = Client("TestCo", "TC01")
    assert c.name == "TestCo" and c.id == "TC01"

    # --- Payment ---
    p = Payment(100.5, "partial")
    assert p.amount == 100.5 and p.status == "partial"

    # --- LedgerEntry ---
    e = LedgerEntry(c, 200, "2026-01-01", "test note")
    assert e.client_id == "TC01" and e.amount == 200 and e.note == "test note"

    # --- Invoice (single) ---
    inv = Invoice("INV-001", c, 500, "2026-03-01")
    assert inv.id == "INV-001" and inv.client_id == "TC01" and inv.amount == 500

    # --- Ledger (add + query) ---
    led = Ledger()
    entry = LedgerEntry(c, 200, "2026-01-01", "test note")
    led.add(entry)
    assert len(led.entries) == 1
    assert any(e.client_id == "TC01" for e in led.entries)

    # --- Invoice (multi + search) ---
    inv2 = Invoice("INV-002", c, 300, "2026-04-01")
    invs = [inv, inv2]
    found = any(i.id == "INV-002" for i in invs)
    assert found

    # --- Invoice (invalid status) ---
    bad = Invoice("BAD", c, 10, "2026-05-01")
    assert len(bad.entries) == 1 and any(e.note.startswith("INVALID:") for e in bad.entries)


class UnitTests(unittest.TestCase):

    def test_units(self):
        test_invoicepad_units()


if __name__ == "__main__":
    unittest.main()
