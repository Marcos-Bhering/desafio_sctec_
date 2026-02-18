import pandas as pd

df = pd.read_csv('Ice Cream Sales - temperatures.csv')
print(df)

ordenacao_df = df.sort_values(by='Temperature',ascending=True)
print(ordenacao_df)

print('Testando se o develope está funcionando')