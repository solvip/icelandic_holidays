#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2013 Sölvi Páll Ásgeirsson
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from distutils.core import setup

setup(name = "icelandic_holidays",
      version = "0.6",
      author = "Sölvi Páll Ásgeirsson",
      author_email = "solvip@gmail.com",
      url = "http://github.com/solvip/icelandic_holidays",
      description = "A Python library written to determine if a day is an Icelandic holiday or a business day.",
      long_description = open("README.md").read(),
      py_modules = ["icelandic_holidays"]
    )
