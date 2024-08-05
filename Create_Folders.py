import shutil
import os
from pathlib import Path
import pandas as pd 
files_to_copy = [r"D:\New_Journey\Coding\Solutions_VS\Hackerrank_practice\Best_stock_2\Best_stock_2\Approach.txt",r"D:\New_Journey\Coding\Solutions_VS\Hackerrank_practice\Best_stock_2\Best_stock_2\main_file.py",r"D:\New_Journey\Coding\Solutions_VS\Hackerrank_practice\Path_sum\testingMain.py",r"D:\New_Journey\Coding\Solutions_VS\Hackerrank_practice\Best_stock_2\Best_stock_2\Best_solution.py"]
data = pd.read_excel(r"D:\New_Journey\Coding\Solutions_VS\Hackerrank_practice\LeetCode\Main_Final_Results.xlsx")
for given_name,level in zip(data['Name'],data['Level']):
    number,name = given_name.split('.')
    print(number,level)
    if level == "Easy":
        folder_path = Path(r"D:\New_Journey\Coding\Solutions_VS\Hackerrank_practice\LeetCode\Easy")
    elif level == "Hard":
        folder_path = Path(r"D:\New_Journey\Coding\Solutions_VS\Hackerrank_practice\LeetCode\Hard")
    elif level == "Medium":
        folder_path = Path(r"D:\New_Journey\Coding\Solutions_VS\Hackerrank_practice\LeetCode\Medium")
    else: 
        continue
    folder_path = folder_path / number
    folder_path.mkdir(parents=True, exist_ok=True)
    # Copy each file to the new folder
    for file_path in files_to_copy:
        file_name = os.path.basename(file_path)
        shutil.copy(file_path, os.path.join(folder_path, file_name))

