# -*- coding: utf-8 -*-
# Copyright (c) 2013 Raphaël Barrois
# This code is published under the two-clause BSD License


class BaseBackend(object):

    # TODO: handle serialization to/from a stream.

    def serialize(self, fields):
        """Serialize a mapping to wire format."""
        raise NotImplementedError()

    def deserialize(self, raw):
        """Deserialize wire format into a simple Python structure."""
        raise NotImplementedError()

    def hydrate(self, field, value):
        """Convert a wire value into a Python object."""
        return field.hydrate(value)

    def dehydrate(self, field, value):
        """Convert a Python object into a wire value."""
        return field.dehydrate(value)
