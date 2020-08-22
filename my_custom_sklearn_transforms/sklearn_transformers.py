from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.impute import SimpleImputer


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
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
        
        si = SimpleImputer(
        missing_values=np.nan,  # os valores faltantes são do tipo ``np.nan`` (padrão Pandas)
        strategy='constant',  # a estratégia escolhida é a alteração do valor faltante por uma constante
        fill_value=0,  # a constante que será usada para preenchimento dos valores faltantes é um int64=0.
        verbose=0,
        copy=True
        )
        
        si.fit(X=data)

        data = pd.DataFrame.from_records(
            data=si.transform(
                X=data
            ),  # o resultado SimpleImputer.transform(<<pandas dataframe>>) é lista de listas
            columns=data.columns  # as colunas originais devem ser conservadas nessa transformação
        )
        
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
