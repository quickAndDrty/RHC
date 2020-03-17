import random

class Knapsack:


    def __init__(self, n, values, we, w):
        self.n = n
        self.values = values
        self.we = we
        self.x = []
        self.w = w

    def randomGeneratorSolution(self):
        self.x = []
        for i in range(int(self.n)):
            self.x.append(random.randint(0,1))
        #print(self.x)
        return self.x

    def fitness(self,v):
        s = 0
        for i in range(1, int(self.n)+1):
            #print (v[i-1])
            #print(self.values[i-1])
            s=s+v[i-1]*self.values[i-1]
        return s

    def validate(self,v):
        s = 0
        for i in range (1, int(self.n)+1):
            s = s + v[i-1]*self.we[i-1]
        if (s <= int(self.w)):
            return 1
        return 0

    def readFromFile(self):
        #f = open("givenValues.txt", "r")
        #file with 20
        #f = open("lab1Values.txt", "r")
        #f = open("lab1Live.txt", "r")
        #file with 200
        f = open("lab1Values2.txt", "r")
        self.n = f.readline()
        self.values = []
        self.we = []
        for i in range(1, int(self.n)+1):
            line = f.readline()
            elements = line.split()
            #print (elements[1])
            self.values.append(int(elements[1]))
            self.we.append(int(elements[2]))
        self.w = f.readline()

    #asta a fost pt o cerita live de la lab1
    def findKSolution(self, k):
        best = 0
        g =open("results.txt", "w");
        while (k>0):
            sol = self.randomGeneratorSolution()
            if (self.validate(sol) == 1):
                #print (sol)

                if (self.fitness(sol) > best):
                    best = self.fitness(sol)
                    bestSol = sol
                g.write(str(sol).strip('[]'))
                g.write("  ")
                g.write(str(self.fitness(sol)))
                g.write("\n")
                #print(self.fitness(sol))
                k=k-1
        g.write("best values are   ")
        g.write(str(bestSol))
        g.write("  ")
        g.write(str(best).strip('[]'))
        #print("best values are:")
        #print(best)
        #print(bestSol)


    def bestSolution(self):
        k = 0
        #for best solution
        k = int(pow(2, int(self.n)-1))
        result = self.randomGeneratorSolution()
        for i in range(1, int(k + 1)):
            sol = self.randomGeneratorSolution()
            if (self.fitness(sol) > self.fitness(result) and self.validate(sol) == 1):
                result = sol
        g = open("bestResult.txt", "w");
        g.write("best result for random search is   ")
        g.write(str(result))
        g.write("  ")
        g.write(str(self.fitness(result)))


    def vecin(self, new):
        #print("sol initiala este", new)
        index = random.randint(0, int(self.n)-1)
        while (new[index] == 1):
            index = random.randint(0, int(self.n) - 1)
        #print("indexul este ", index)
        new[index] = 1
        return new

    def RHC(self, k):
        c = self.randomGeneratorSolution()
        while (self.validate(c) == 0):
            c = self.randomGeneratorSolution()
        #print ("solutia initiala este ", c)
        #print("cu fitness ul ", self.fitness(c))
        #k = pow(2, int(self.n)-1)
        restartValue = k/5
        #for restarting
        count = 0

        for i in range (k):
            x = self.vecin(c[:])
            count = count + 1
            if (self.validate(x)==1 and self.fitness(x) > self.fitness(c) ):
                c = x
                count = 0
                #print("vecinul valid este ", x)
            if count > restartValue:
                c = self.randomGeneratorSolution()
                while (self.validate(c) == 0):
                    c = self.randomGeneratorSolution()

            #print("cel mai bun fitness", self.fitness(c))

        return self.fitness(c)
