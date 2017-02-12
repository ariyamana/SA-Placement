''' This module imports the input information from an input file.'''

def load_input(filename):

    # Initializing variables:
    net_list =[]
    net_blocks = []
    num_cells = 0
    num_conns = 0
    num_rows  = 0
    num_cols  = 0

    # Openning the input file:
    f = open(filename, "r")

    # Reading the content of the file:
    file_content = f.readlines()

    # pars the first line of the input line that includes:
    # the number of cells to be placed, the number of connections between the
    # cells, and the number of rows and columns upon which the circuit should be
    # placed.
    first_line = file_content[0].split()

    num_cells = int(first_line[0])
    num_conns = int(first_line[1])
    num_rows  = int(first_line[2])
    num_cols  = int(first_line[3])

    # Loop over the 2nd line to the last line of the file to populate the
    # net list info:
    for net in range(1,num_conns+1):
        
        # Clear the net_list temporary container:
        net_blocks = []

        # Read the line in the input file associated with net list "net":
        net_info =  file_content[net].split()

        # the first number in the line is the number of blocks
        net_num_block = int(net_info[0])

        # Append the blocks to the net block list:
        for i in range(1, net_num_block+1):
            net_blocks.append(int(net_info[i]))

        # Append this net to the master net list:
        net_list.append(net_blocks)

    # Display the imported data:
    print 'Opened a file for a chip:'
    print 'number of cells = ', num_cells
    print 'number of nets = ', num_conns
    print 'number of rows and columns = ', num_rows,'x', num_cols
    print 'net list is:'
    print net_list



if __name__ == "__main__":

    input_adress = 'Examples/cm138a.txt'
    load_input(input_adress)
