
import pandas as pd
import os

data={
    'Name':['John', 'Alice', 'Bob', 'Eve'],

    
    'Age':[28, 24, 35, 22],
    'City':['New York', 'Los Angeles', 'Chicago', 'Houston']
    }
df=pd.DataFrame(data)

data_dir="data"
os.makedirs(data_dir, exist_ok=True)
file_path=os.path.join(data_dir, "sample_data.csv")
df.to_csv(file_path, index=False)

print(f"DataFrame saved to {file_path}")
