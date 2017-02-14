import load as LD
import Placer_class as PLC

#input_adress = 'Examples/cm138a.txt'
#input_adress = 'Examples/e64.txt'
input_adress = 'Examples/apex4.txt'
chip1 = LD.load_input(input_adress, verbose=0)
#chip1.cell_net_incidence()

sa_agent = PLC.sa_placer_agent(chip1, 10**6, verbose = 2)


sa_agent.anneal()
