
import requests
import pandas as pd

response = requests.get('https://jsonplaceholder.typicode.com/users')

data=response.json()

df=df.DataFrame(data)

df=df[['id','name','email']]

print('Transformed user data: ')
print(df)

