#Create an 3x4 (3 rows x 4 columns) pandas DataFrame in which the columns are named Eleanor, Chidi, Tahani, and Jason. Populate each of the 
# 12 cells in the DataFrame with a random integer between 0 and 100, inclusive.
#Output the following:
#the entire DataFrame
#the value in the cell of row #1 of the Eleanor column

import pandas as pd
import numpy as np

columns = ['Eleanor', 'Chidi', 'Tahani', 'Jason']
data = np.random.randint(0, 101, size=(3, 4))

tgp_df = pd.DataFrame(data, columns=columns)

print(tgp_df)
print(tgp_df['Eleanor'][1])