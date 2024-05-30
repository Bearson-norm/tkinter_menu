import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

data1 = {'Country':['A','B','C','D','E'],
        'gdp_per_capita':[45000,42000,52000,49000,47000]
        }
df1 = pd.DataFrame(data1)
root = tk.Tk()

figure1 = plt.Figure(figsize=(6,5), dpi = 500)
ax1 = figure1.add_subplot(111)
bar1 = FigureCanvasTkAgg(figure1, root)
bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
df1 = df1[['Country','gdp_per_capita']].groupby('Country').sum()
df1.plot(kind='bar', legend = True, ax = ax1)
ax1.set_title('Country Vs. GDP Per Capita')

root.mainloop()