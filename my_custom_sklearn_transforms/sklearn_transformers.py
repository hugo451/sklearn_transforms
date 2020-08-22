from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        data = pd.DataFrame(data)
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')
    
class DropUselessRows(BaseEstimator, TransformerMixin):
    def __init__(self, columns, value):
        self.columns = columns
        self.value = value

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        
        data = pd.DataFrame(data)
        
        for i in range(0, len(data)):
            try:
                flag = 0
                for column in self.columns:
                    if data.iloc[i][column] == self.value:
                        flag += 1
                    
                if flag == len(self.columns):
                    data = data.drop(i)
            except:
                continue
        
        # Retornamos um novo dataframe sem as linhas indesejadas
        return data
