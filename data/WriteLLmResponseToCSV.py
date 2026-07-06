import csv
import os
from pyclbr import Class


class WriteLLmResponseToCSV:
   def __init__(self, csv_file):
    self.csv_file = csv_file
    if not os.path.exists(self.csv_file):
        with open(self.csv_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Prompt', 'Response'])
  
   def writesResponseToCSV(self, prompts, response):
    with open(self.csv_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([prompts,response])
    return f"Response written to {self.csv_file}"
