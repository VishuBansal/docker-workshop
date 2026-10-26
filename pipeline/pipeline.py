import sys
import pandas as pd  # type: ignore[reportMissingModuleSource]

df = pd.DataFrame({"A" : [1,2], "B" : [3,4]})
print(df.head())