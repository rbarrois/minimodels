# -*- coding: utf-8 -*-
# Copyright (c) 2013 Raphaël Barrois
# This code is published under the two-clause BSD License

import json

from . import base


class JsonBackend(base.BaseBackend):
    def serialize(self, fields):
        return json.dumps(fields)

    def deserialize(self, raw):
        return json.loads(raw)

