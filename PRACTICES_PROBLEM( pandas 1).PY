import pandas as pd

data = {"name": ["banana", "apple", "orange"],
        "age": [11, 12, 14]}

df = pd.DataFrame(data)

print(df)

print("---------------------------------------------------------------")
import pandas as pd

data = {
    "Name": ["Spongebob", "Patrick", "Squidward"],
    "Age": [30, 35, 50]
}

# Adding custom index labels
df = pd.DataFrame(data, index=["Employee 1", "Employee 2", "Employee 3"])

print(df)
