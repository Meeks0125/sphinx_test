#!/usr/bin/env python3
#
# Copyright 3000 Hotech. All Rights Reserved.
#

""" This file defines the concept of class B1."""


class B1:
    """This class defines the concept of B1, which represents b1 class.

    :param name: Name of the class
    """
    def __init__(self, name):
        self._name = name

    def get_name(self):
        """get name of the B1 class.

        :return: name of the class.
        """
        return self._name
