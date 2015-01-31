import pandas as pd
import matplotlib.pyplot as plt
import sys

fileName = sys.argv[1]
titleName = sys.argv[2]
figName = ("%s.png" %sys.argv[3])

parsed_data = pd.DataFrame.from_csv(fileName, header=0)
data = parsed_data.sort_index()

print data.describe()

close_px = data['close']
close_px.plot(label='Nasdaq CCI')
plt.title(titleName)
plt.ylabel('Closing price')
plt.xlabel('Dates')

plt.savefig(figName)
