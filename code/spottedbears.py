import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


url_github = 'https://raw.githubusercontent.com/DataSnowman/rv/main/data/RVshipmentsByYear.csv'
pd_df = pd.read_csv(url_github)
pd_df.head(5)
print(pd_df)

# plot the date in a bar chart
pd_df.plot.bar(x='year', y='shipments', rot=90)
plt.show()