#!/usr/bin/env python3
#
# Copyright 3000 Hotech. All Rights Reserved.
#

""" This file defines the concept of class A2."""


class A2:
    """This class defines the concept of A2, which represents a2 class.

    :param attribute: Attribute of the class
    """
    def __init__(self, attribute):
        self._attribute = attribute

    def get_attribute(self):
        """get attribute of the A2 class.

        :return: attribute of the class.
        """
        return self._attribute
