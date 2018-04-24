import logging
from abc import ABCMeta, abstractmethod


class PipelineBase(object):
    __metaclass__ = ABCMeta

    def __init__(self, name, components):
        self.logger = logging.getLogger("{0} [{1}]".format(name, self.__class__.__name__))
        self.name = name
        self.components = components
        if not self.is_valid():
            raise ValueError("Pipeline components are not valid!")

    @abstractmethod
    def is_valid(self):
        raise NotImplementedError("{0} doesn't have is_valid method.".format(self.__class__.__name__))

