
class Roulette:
    def __init__(self,fitnessF):
        self.fitnessF=fitnessF
    def run(self,individuals,n_to_select,seed):

    def fitness_list(self,individuals):
        fits=[]
        for i in individuals:
            fits.append(self.fitnessF(i))
        return fits
    def sum_fitness_list(self,f_list):
        s=0
        for i in f_list:
            if(i>=0):
                sum+=s
        return s 
    def selected_individuals(fits,individuals,selected):
        c=0
        for i in range(0,len(individuals)):
            c+= fits[i]
            if c >=selected:
                return individuals[i]
        return null