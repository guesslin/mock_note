#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mock
import unittest

from mymodule import RemovalService


class RemovalServiceTestCase(unittest.TestCase):
    """Test cases for RemovalService"""

    def setUp(self):
        self.path = '/tmp'

    @mock.patch('mymodule.os.path')
    @mock.patch('mymodule.os')
    def test_tm(self, mock_os, mock_path):
        reference = RemovalService()
        mock_path.isfile.return_value = False

        reference.rm(self.path)
        self.assertFalse(mock_os.remove.called,
                         'Failed to not remove the file if not present')

        mock_path.isfile.return_value = True

        reference.rm(self.path)

        mock_os.remove.assert_called_with(self.path)
