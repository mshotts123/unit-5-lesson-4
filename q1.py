import bs4
import pandas as pd
import requests
import matplotlib.pyplot as plt

tables = pd.read_html(
    "https://en.wikipedia.org/wiki/Minnesota",
    match = "Historical population"
)
table = tables[0]
df = table[["Census", "Pop."]]
df = df.iloc[0:-2].astype("int")
df.plot(x = "Census", y = "Pop.")
plt.show()