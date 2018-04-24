import logging
from abc import abstractmethod, ABCMeta


class PreprocessBase(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.logger = logging.getLogger(("{0} [Preprocess]".format(self.__class__.__name__)))

    @abstractmethod
    def process(self, data):
        """ Process the data

        Parameters
        ----------
        data: pd.DataFrame
            Input dataframe

        Returns
        -------
        pd.DataFrame
        """
        raise NotImplementedError("{0} doesn't has a transform method.".format(self.__class__.__name__))
