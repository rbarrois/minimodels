# -*- coding: utf-8 -*-
# Copyright (c) 2013 Raphaël Barrois
# This code is published under the two-clause BSD License


from . import base


class DictBackend(base.BaseBackend):
    def serialize(self, fields):
        return dict(fields)

    def deserialize(self, raw):
        return dict(raw)
