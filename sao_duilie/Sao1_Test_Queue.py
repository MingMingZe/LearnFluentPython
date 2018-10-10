from unittest import TestCase

from sao_duilie.Sao1_Queue import MyQueue, Full, Empty


class TestSaoQueue(TestCase):
    def test_push(self):
        mq = MyQueue(maxsize=3)
        for i in range(3):
            mq.push(i)
        self.assertEqual(3, len(mq))
        self.assertRaises(Full, mq.push, 4)

    def test_pop(self):
        mq = MyQueue(maxsize=3)
        for i in range(3):
            mq.push(i)
        self.assertEqual(0, mq.pop())
        self.assertEqual(1, mq.pop())
        self.assertEqual(2, mq.pop())
        self.assertRaises(Empty, mq.pop)

