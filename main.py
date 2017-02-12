import load as LD

input_adress = 'Examples/cm138a.txt'
chip1 = LD.load_input(input_adress, verbose =1)

chip1.display()


if chip1.swap_delta_cost(0,10)<0:
    chip1.swap_cells(0,10)
else:
    print 'the cost is: ', chip1.swap_delta_cost(0,10)

chip1.display()
