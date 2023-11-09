import pandas as pd


def filtro(df, coluna, op, operando):
    if coluna not in df:
        print('Esta coluna não existe neste DataFrame')
        return None

    if op == '==':
        return df[df[coluna] == operando]
    elif op == '<=':
        return df[df[coluna] <= operando]
    elif op == '>=':
        return df[df[coluna] >= operando]
    elif op == '<':
        return df[df[coluna] < operando]
    elif op == '>':
        return df[df[coluna] > operando]
    elif op == '!=':
        return df[df[coluna] != operando]
    else:
        print('Operação inválida')
        return None


df = pd.read_csv('df_ex.csv')
result = filtro(df, 'Preenchimento', '==', 'Residência')
print(result)
