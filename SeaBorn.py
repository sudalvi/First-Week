import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = sb.load_dataset('titanic')
sb.barplot(X='sex', Y='servived', hue="class", data=df)
plt.show()
