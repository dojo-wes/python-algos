import unittest
from push_front import push_front

class PushFrontTests(unittest.TestCase):
  def test_empty_list(self):
    test_list = []
    result = push_front(test_list, 1)
    expected = [1]
    self.assertEqual(result, expected)
    self.assertIs(result, test_list)
  
  def test_has_values(self):
    test_list = [2, 3, 4]
    result = push_front(test_list, 1)
    expected = [1,2,3,4]
    self.assertEqual(result, expected)
    self.assertIs(result, test_list)

  def test_params_invalid(self):
    with self.assertRaises(TypeError):
      push_front()

    with self.assertRaises(TypeError):
      push_front(None, 1)

    with self.assertRaises(TypeError):
      push_front([])

suite = unittest.TestLoader().loadTestsFromTestCase(PushFrontTests)
unittest.TextTestRunner(verbosity=2).run(suite)
