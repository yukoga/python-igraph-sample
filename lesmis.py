#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
from igraph import *
from py2cytoscape.data.cyrest_client import CyRestClient
import os.path


class LesMis:

  def __init__(self, file='lesmis.gml'):
    root, ext = os.path.splitext(file)
    if ext != '.gml':
      raise IOError('You need to set .gml file as 1st arg.')
    self.__g = Graph.Read_GML(file)

  def getGraph(self):
    return self.__g

