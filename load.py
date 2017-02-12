''' This module imports the input information from an input file.'''

def load_input(filename):
    f = open(filename, "r")

    file_content = f.readlines()

    print file_content


if __name__ == "__main__":

    input_adress = 'Examples/cm138a.txt'

    load_input(input_adress)
