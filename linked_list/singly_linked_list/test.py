import unittest

from .singly_linked_list import SinglyLinkedList


class TestSinglyCycleLinkedList(unittest.TestCase):
    def setUp(self):
        self.linked_list = SinglyLinkedList()

    def test_is_empty(self):
        self.assertTrue(self.linked_list.is_empty())

    def test_not_is_empty(self):
        self.linked_list.add(0)
        self.assertFalse(self.linked_list.is_empty())

    def test_length(self):
        self.linked_list.add(0)
        self.linked_list.add(1)
        self.assertEqual(2, self.linked_list.length())

    def test_length_zero(self):
        self.assertEqual(0, self.linked_list.length())

    def test_length_one(self):
        self.linked_list.add(1)
        self.assertEqual(1, self.linked_list.length())

    def test_add(self):
        self.linked_list.add(0)
        self.linked_list.add(1)
        self.assertListEqual([1, 0], self.linked_list.to_list())

    def test_append(self):
        self.linked_list.append(0)
        self.linked_list.append(1)
        self.linked_list.append(2)
        self.assertListEqual([0, 1, 2], self.linked_list.to_list())

    def test_insert_head_empty(self):
        """空链表头部插入"""
        self.linked_list.insert(0, 0)
        self.assertListEqual([0], self.linked_list.to_list())

    def test_insert_head_not_empty(self):
        """非空链表头部插入"""
        self.linked_list.add(0)
        self.linked_list.insert(0, 1)
        self.assertListEqual([1, 0], self.linked_list.to_list())

    def test_insert_pos(self):
        """链表的中间位置插入"""
        self.linked_list.add(2)
        self.linked_list.add(0)
        self.linked_list.insert(1, 1)
        self.assertListEqual([0, 1, 2], self.linked_list.to_list())

    def test_insert_tail(self):
        """链表末尾插入"""
        self.linked_list.add(0)
        self.linked_list.insert(1, 1)
        self.assertListEqual([0, 1], self.linked_list.to_list())

    def test_remove_head(self):
        """删除头部结点"""
        self.linked_list.add(1)
        self.linked_list.add(0)
        self.linked_list.remove(0)
        self.assertListEqual([1], self.linked_list.to_list())

    def test_remove_pos(self):
        """删除中间任意位置结点"""
        self.linked_list.add(2)
        self.linked_list.add(1)
        self.linked_list.add(0)
        self.linked_list.remove(1)
        self.assertListEqual([0, 2], self.linked_list.to_list())

    def test_remove_tail(self):
        """删除尾结点"""
        self.linked_list.add(1)
        self.linked_list.add(0)
        self.linked_list.remove(1)
        self.assertListEqual([0], self.linked_list.to_list())

    def test_remove_not_exist(self):
        """删除一个不存在的值"""
        self.linked_list.add(0)
        self.linked_list.remove(1)

    def test_search(self):
        """查找指定结点"""
        self.linked_list.add(0)
        self.assertTrue(self.linked_list.search(0))

    def test_travel(self):
        self.linked_list.add(0)
        self.linked_list.travel()
