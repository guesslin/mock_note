#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mymodule import rm

import mock
import unittest


class RmTestCase(unittest.TestCase):

    def setUp(self):
        self.path = '/home/iii/'

    @mock.patch('mymodule.os.path')
    @mock.patch('mymodule.os')
    def test_rm(self, mock_os, mock_path):
        mock_path.isfile.return_value = False
        rm("any path")
        # test that rm called os.remove with the right parameters
        self.assertFalse(mock_os.remove.called,
                         'Failed to not remove the file if not present')

        mock_path.isfile.return_value = True
        rm(self.path)
        mock_os.remove.assert_called_with(self.path)
