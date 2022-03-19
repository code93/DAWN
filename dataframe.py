import ast
import pandas as pd
import matplotlib.pyplot as plt

with open('fishList.txt') as f:
   data = f.read()

d = ast.literal_eval(data)

df = pd.DataFrame(d)

df =df.T

print(df[0])

df.plot(layout=(12,12))
plt.show()
