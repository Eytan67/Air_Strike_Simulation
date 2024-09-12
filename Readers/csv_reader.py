import  csv

def read_csv_files_into_dict(path:str) -> str:
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        return reader