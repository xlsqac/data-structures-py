import unittest

from singly_cycle_linked_list import SinglyCycleLinkedList


class TestSinglyCycleLinkedList(unittest.TestCase):

    def setUp(self):
        self.linked_list = SinglyCycleLinkedList()

    def test_is_empty(self):
        self.assertTrue(self.linked_list.is_empty())

    def test_not_is_empty(self):
        self.linked_list.add(0)
        self.assertFalse(self.linked_list.is_empty())

    def test_length(self):

        pass

    def test_add(self):
        pass

    def test_append(self):
        pass

    def test_insert_head(self):
        pass

    def test_insert_pos(self):
        pass

    def test_insert_tail(self):
        pass

    def test_remove_head(self):
        pass

    def test_remove_pos(self):
        pass

    def test_remove_tail(self):
        pass
