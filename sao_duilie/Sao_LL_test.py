import unittest
from sao_duilie.Sao_LL import Linklist


class TestLinkedList(unittest.TestCase):

    def test_len(self):
        ll = Linklist(maxsize=5)
        for i in range(5):
            ll.append(value=i)
        self.assertEqual(5, ll.len())

    def test_append(self):
        ll = Linklist(maxsize=5)
        for i in range(5):
            ll.append(i)
        self.assertRaises(Exception, ll.append, 6)

    def test_find(self):
        ll = Linklist(maxsize=5)
        for i in range(5):
            ll.append(i)
        self.assertEqual(2, ll.find(2))
        self.assertEqual(2, ll.find(3), "find error")

    def test_popleft(self):
        ll = Linklist(maxsize=3)
        for i in range(3):
            ll.append(i)
        self.assertEqual(0, ll.popleft())

    def test_appendleft(self):
        ll = Linklist(maxsize=3)
        for i in range(3):
            ll.appendleft(i)
        self.assertEqual(2, ll.popleft())

    def test_clear(self):
        ll = Linklist(maxsize=3)
        for i in range(3):
            ll.append(i)
        ll.clear()
        self.assertEqual(0, ll.len())
        self.assertEqual(None, ll.root.value)
        self.assertEqual(None, ll.root.next)

    def test_remove(self):
        ll = Linklist(maxsize=3)
        for i in range(3):
            ll.append(i)
        self.assertEqual(2, ll.remove(2))
        self.assertEqual(2, ll.len())

    def test_iter(self):
        ll = Linklist(maxsize=3)
        for i in range(3):
            ll.append(i)
        self.assertEqual([0, 1, 2], [i for i in ll.iter_node()])
