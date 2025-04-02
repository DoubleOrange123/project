import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt

date = ['02.12.2025', '04.12.2025', '06.12.2025']
amount = [5,6,7]

ser = pd.Series(date, index = amount)
print(ser)
plt.pie(ser.index, labels = ser.values)
plt.show()



markets_labels = [1, 2, 3]
markets_colors = ['red', 'blue', 'green']

plt.title("Прибыль магазинов")
plt.bar(['h', 't', 'q'], [2000, 50000, 3000], label=markets_labels, color=markets_colors)

# размер текста на графике
plt.legend(title='Магазины')

plt.show()