import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    "Student":["Ali","John","Sara","Mike","Anna"],
    "Marks":[78,85,90,66,88]
}

df = pd.DataFrame(data)

# statistics
print("Average:", df["Marks"].mean())
print("STD:", df["Marks"].std())

# using loc (label based)
print(df.loc[0:2])   # first three students

# graph
df.plot(x="Student", y="Marks", kind="bar", title="Student Marks")
plt.show()