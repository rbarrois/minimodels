# -*- coding: utf-8 -*-
# Copyright (c) 2013 Raphaël Barrois
# This code is published under the two-clause BSD License


class BaseModel(object):

    def __init__(self, **kwargs):
        for field in self._meta.fields:
            setattr(self, field.name, kwargs.get(field.name, field.default))

        super(BaseModel, self).__init__(**kwargs)

    class Meta:
        # Options for the model
        pass

    def serialize(self):
        for field in self._meta.fields:
            value = getattr(self, field.name)
   
