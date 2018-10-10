from unittest import TestCase

from sao_duilie.SaoDLL import Sao_DLL, Full, Empty, Node


class Test_SaoDLL(TestCase):
    def test_append(self):
        dll = Sao_DLL(maxsize=3)
        for i in range(3):
            dll.append(i)
        self.assertEqual(3, dll.len())
        self.assertRaises(Full, dll.append, 4)

    def test_appendleft(self):
        dll = Sao_DLL(maxsize=3)
        for i in range(3):
            dll.appendleft(i)
        self.assertEqual(3, dll.len())

    def test_remove(self):
        dll = Sao_DLL(maxsize=3)
        dll.append(0)
        self.assertEqual(0, dll.remove(0))
        dll.append(1)
        dll.append(2)
        self.assertEqual(1, dll.remove(1))
        self.assertEqual(1, dll.len())

    def test_reverse(self):
        dll = Sao_DLL(maxsize=3)
        for i in range(3):
            dll.append(i)
        self.assertEqual([2, 1, 0], [j for j in dll.iter_reverse()])