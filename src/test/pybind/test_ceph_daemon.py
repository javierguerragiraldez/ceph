#!/usr/bin/nosetests --nocapture
# -*- mode:python; tab-width:4; indent-tabs-mode:t -*-
# vim: ts=4 sw=4 smarttab expandtab
#
"""
Copyright (C) 2015 Red Hat

This is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public
License version 2, as published by the Free Software
Foundation.  See file COPYING.
"""

from StringIO import StringIO

from unittest import TestCase

from ceph_daemon import DaemonWatcher


class TestDaemonWatcher(TestCase):
    def test_format(self):
        dw = DaemonWatcher(None)

        self.assertEqual(dw.format_dimless(1, 4), "  1 ")
        self.assertEqual(dw.format_dimless(1000, 4), "1.0k")
        self.assertEqual(dw.format_dimless(3.14159, 4), "  3 ")
        self.assertEqual(dw.format_dimless(1400000, 4), "1.4M")

    def test_col_width(self):
        dw = DaemonWatcher(None)

        self.assertEqual(dw.col_width("foo"), 4)
        self.assertEqual(dw.col_width("foobar"), 6)

    def test_supports_color(self):
        dw = DaemonWatcher(None)
        # Can't count on having a tty available during tests, so only test the false case
        self.assertEqual(dw.supports_color(StringIO()), False)
