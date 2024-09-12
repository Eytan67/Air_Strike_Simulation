
def read_txt_file(path: str) -> str:
    my_file = open(path, "r", newline='')

    data = my_file.read()

    my_file.close()

    return data