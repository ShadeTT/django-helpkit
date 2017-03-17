# coding=utf-8
import os
import unittest

from kit.utils import chunked_path_handler

__author__ = 'shade'


class UtilsTestCase(unittest.TestCase):

    def test_chunked_path(self):
        cls_name = 'cls_name'
        filename = 'aabbccdd.jpg'

        result = chunked_path_handler(cls_name, filename)
        self.assertTrue(result.startswith('%s/' % cls_name))

        generated_filename = os.path.basename(result)
        self.assertTrue(generated_filename.endswith('.jpg'))

        path = result.strip(cls_name).strip(generated_filename).replace('/', '')
        self.assertEqual(path, os.path.splitext(generated_filename)[0])
