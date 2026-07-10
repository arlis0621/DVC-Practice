
import pandas as pd
import os

data={
    'Name':['John', 'Alice', 'Bob', 'Eve'],

    
    'Age':[28, 24, 35, 22],
    'City':['New York', 'Los Angeles', 'Chicago', 'Houston']
    }

new_row={'Name':'Charlie', 'Age':30, 'City':'San Francisco'}
new_row_1={'Name':'David', 'Age':27, 'City':'Seattle'}
df=pd.DataFrame(data)
df.loc[len(df)] = new_row
df.loc[len(df)] = new_row_1


data_dir="data"
os.makedirs(data_dir, exist_ok=True)
file_path=os.path.join(data_dir, "sample_data.csv")
df.to_csv(file_path, index=False)

print(f"DataFrame saved to {file_path}")
