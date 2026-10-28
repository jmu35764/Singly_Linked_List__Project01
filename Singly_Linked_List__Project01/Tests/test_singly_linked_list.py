import unittest
from SinglyLinkedList import SinglyLinkedList
from SinglyLinkedList import node

class TestSinglyLinkedList(unittest.TestCase):
    def test_contains(self):
        sl1 = SinglyLinkedList()
        sl1.append(5)
        sl1.append(6)
        sl1.append(11)

        self.assertTrue(sl1.contains(6))
        self.assertFalse(sl1.contains(10))

if __name__ == '__main__':
    unittest.main()
