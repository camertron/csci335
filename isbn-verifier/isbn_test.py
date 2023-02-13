import unittest
from isbn import check_isbn

class IsbnTest(unittest.TestCase):
  def test_check_standard_isbns(self):
    self.assertEqual(check_isbn('0-198-53453-1'), 0)
    self.assertEqual(check_isbn('0-19-852663-6'), 0)
    self.assertEqual(check_isbn('1-86197-271-7'), 0)
    self.assertEqual(check_isbn('8-175-25766-0'), 0)

  def test_check_isbn_with_x(self):
    self.assertEqual(check_isbn('3-598-21507-X'), 0)
    self.assertEqual(check_isbn('0-8044-2957-X'), 0)
    self.assertEqual(check_isbn('0-9752298-0-X'), 0)

  def test_check_isbn_with_lowercase_x(self):
    self.assertEqual(check_isbn('3-598-21507-x'), 0)
    self.assertEqual(check_isbn('0-8044-2957-x'), 0)
    self.assertEqual(check_isbn('0-9752298-0-x'), 0)

  def test_check_isbn_without_dashes(self):
    self.assertEqual(check_isbn('0198534531'), 0)
    self.assertEqual(check_isbn('359821507X'), 0)

  def test_check_isbn_lots_of_dashes(self):
    self.assertEqual(check_isbn('0-1-9-8-5-3-4-5-3-1'), 0)
    self.assertEqual(check_isbn('3-5-9-8-2-1-5-0-7-X'), 0)

  def test_check_isbn_invalid(self):
    self.assertEqual(check_isbn('0-198-53453-2'), 1)
    self.assertEqual(check_isbn('0-19-852663-7'), 1)
    self.assertEqual(check_isbn('1-86197-271-8'), 1)
    self.assertEqual(check_isbn('8-175-25766-1'), 1)

  def test_check_isbn_too_short(self):
    with self.assertRaises(RuntimeError):
      check_isbn('123')

  def test_check_isbn_too_long(self):
    with self.assertRaises(RuntimeError):
      check_isbn('0-198-53453-10')

  def test_check_isbn_invalid_char(self):
    with self.assertRaises(RuntimeError):
      check_isbn('0-K98-A3453-1')

if __name__ == '__main__':
  unittest.main()
