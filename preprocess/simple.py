import pandas as pd

from preprocess.base import PreprocessBase


class AddColumn(PreprocessBase):
    def __init__(self, col_name, col_data):
        """Add a new column to the data

        Parameters
        ----------
        col_name: str
            Column name
        col_data:
            Column data
        """

        super(self.__class__, self).__init__()
        self.col_name = col_name
        self.col_data = col_data

    def process(self, data):
        if self.col_name not in data.columns:
            data[self.col_name] = self.col_data
        return data


class CustomSimple(PreprocessBase):

    def __init__(self, df_function, **kwargs):
        """Process with a pd.DataFrame function

        Parameters
        ----------
        df_function:
            A pd.DataFrame function
        kwargs:
            Arguments of 'df_function'
        """

        super(self.__class__, self).__init__()
        self.function = df_function
        self.kwargs = kwargs

    def process(self, data):
        return self.function(data, **self.kwargs)


class EasyOneHot(PreprocessBase):
    def __init__(self, col_names):
        """One hot encode selected columns based on all existing categorical values

        Parameters
        ----------
        col_names: list
            List of names of the columns to one hot encode
        """
        super(self.__class__, self).__init__()
        if isinstance(col_names, list):
            raise TypeError("Argument 'col_names' has to be type 'list'")
        self.columns = col_names  # type: list

    def process(self, data):
        for col in self.columns:
            if col not in data.columns:
                self.logger.warning("Column '{}' is not in the data".format(col))
                self.columns.remove(col)

        return pd.get_dummies(data, columns=self.columns)
