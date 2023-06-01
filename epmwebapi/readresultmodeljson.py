﻿"""
Elipse Plant Manager - EPM Web API
Copyright (C) 2018 Elipse Software.
Distributed under the MIT License.
(See accompanying file LICENSE.txt or copy at http://opensource.org/licenses/MIT)
"""

class ReadResultModelJSON(object):
  
  def __init__(self, items, diagnostics):
    self._items = items
    self._diagnostics = diagnostics

  def items(self):
    return list(zip(self._items, self._diagnostics))

  def values(self):
    return self._items

  def diagnostics(self):
    return self._diagnostics

