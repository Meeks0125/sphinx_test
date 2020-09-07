#!/usr/bin/env python3
#
# Copyright 3000 Hotech. All Rights Reserved.
#

""" This file defines the concept of class B2."""


class B2:
    """This class defines the concept of B2, which represents b2 class.

    :param attribute: Attribute of the class
    """
    def __init__(self, attribute):
        self._attribute = attribute

    def get_attribute(self):
        """get attribute of the B2 class.

        :return attribute of the class.
        """
        return self._attribute
