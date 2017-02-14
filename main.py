import load as LD
import Placer_class as PLC
from numpy import mean

# Initializing variables and benchmarks:
Benchmarks = ['Examples/cm138a.txt',
'Examples/cm150a.txt',
'Examples/cm151a.txt',
'Examples/cm162a.txt',
'Examples/alu2.txt',
'Examples/C880.txt',
'Examples/e64.txt',
'Examples/apex1.txt',
'Examples/cps.txt',
'Examples/paira.txt',
'Examples/pairb.txt',
'Examples/apex4.txt']

#Benchmarks = ['Examples/apex4.txt']

cost_vec=[]

# Main loop over all benchmarks:
for  input_adress in Benchmarks:

    # Load the chip information:
    chip1 = LD.load_input(input_adress, verbose=0)

    # Create a simulated annealing based placement
    sa_agent = PLC.sa_placer_agent(chip1, 5*10**5, verbose = 1)

    # Optimize the placement:
    final_cost =  sa_agent.anneal()

    # Display the result:
    print '-'*50
    print 'Placement Done for chip at', input_adress
    print 'with final cost:', final_cost

    # Store the cost for stats:
    cost_vec.append(final_cost)

# Calculating the stats:
AVG_cost = mean(cost_vec)

# Display Final results:
print '='*50
print "Experiment done with average cost:", AVG_cost
