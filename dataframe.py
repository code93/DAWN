import ast
import pandas as pd

with open('fishList.txt') as f:
   data = f.read()

d = ast.literal_eval(data)

df = pd.DataFrame(d)

print(df)