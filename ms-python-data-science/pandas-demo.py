# Panda => it's a library for data manipulation
import pandas as pd

print(pd.Series([1, 2, 3]))

area = pd.Series(['Albania', 23232])
population = pd.Series(['Albania', 545454])

countries = pd.DataFrame({'Area': area, 'Population': population})
print(countries)
