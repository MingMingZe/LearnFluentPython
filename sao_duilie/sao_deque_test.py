from unittest import TestCase

from sao_duilie.SaoDLL import Full, Empty
from sao_duilie.sao_deque import Sao_deque


class sao_deque_test(TestCase):
    def test_de_append(self):
        sdq = Sao_deque(maxsize=3)
        for i in range(3):
            sdq.de_append(i)
        self.assertEqual([0, 1, 2], [n for n in sdq.iter_node()])
        self.assertRaises(Full, sdq.append, 4)

    def test_de_appendleft(self):
        sdq = Sao_deque(maxsize=3)
        for i in range(3):
            sdq.de_append_left(i)
        self.assertEqual([2, 1, 0], [n for n in sdq.iter_node()])
        self.assertRaises(Full, sdq.de_append_left, 4)

    def test_de_pop(self):
        sdq = Sao_deque(maxsize=3)
        for i in range(3):
            sdq.de_append(i)
        self.assertEqual(2, sdq.de_pop())
        sdq.de_pop()
        sdq.de_pop()
        self.assertRaises(Empty, sdq.de_pop)

    def test_de_popleft(self):
        sdq = Sao_deque(maxsize=2)
        sdq.append(1)
        sdq.append(2)
        self.assertEqual(1, sdq.de_popleft())
        sdq.de_popleft()
        self.assertRaises(Empty, sdq.de_popleft())

