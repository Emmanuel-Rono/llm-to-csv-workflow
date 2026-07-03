import csv
from pyclbr import Class


class WriteLLmResponseToCSV:
   def __init__(self,response,csv_file):
    self.csv_file = csv_file
    self.response = response
    
   def writesResponsToCSV(self):
    with open(self.csv_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([self.response])
    return f"Response written to {self.csv_file}"
