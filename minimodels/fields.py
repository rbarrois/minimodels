# -*- coding: utf-8 -*-
# Copyright (c) 2013 Raphaël Barrois
# This code is published under the two-clause BSD License


class Field(object):
    def hydrate(self, value, backend):
        return value

    def dehydrate(self, value, backend):
        return value


class StringField(object):
    pass


class IntegerField(object):
    def hydrate(self, value, backend):
        return int(value)


class SubField(Field):
    def __init__(self, contained, **kwargs):
        self.contained_class = contained
        super(ListField, self).__init__(**kwargs)

    def hydrate(self, value, backend):
        value.

    def dehydrate(self, value, backend):
        return [backend.dehydrate(self.contained_field, item) for item in value]


class ListField(object):
    def __init__(self, contained, **kwargs):
        self.contained_field = contained
        super(ListField, self).__init__(**kwargs)

    def hydrate(self, value, backend):
        # TODO

    def dehydrate(self, value, backend):
        return [backend.dehydrate(self.contained_field, item) for item in value]
