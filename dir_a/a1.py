#!/usr/bin/env python3
#
# Copyright 3000 Hotech. All Rights Reserved.
#

""" This file defines the concept of class A1."""


class A1:
    """
    This class defines the concept of A1, which represents a1 class.

    :param name: Name of the class
    """
    def __init__(self, name):
        self._name = name

    def get_name(self):
        """
        get name of the A1 class.

        :return: name of the class.
        """
        return self._name

    def calcuate(self, a):
        """
        calculate.
        :param a: the value
        :return: calculated value
        """
        return a * 2
