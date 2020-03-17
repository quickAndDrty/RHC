import random
from Knapsack import *

def main():

    #a = Knapsack(3, [60, 100, 120], [10, 20, 30], 50)
    #print(a.values)
    #1st solution generated
    #print(a.bestSolution())
    #print (a.fitness(a.bestSolution()))
    #print(a.validate(a.bestSolution()))

    #g = open("resultsLive.txt", "w")
    #file with 20 values
    #g = open("results1.txt", "w")
    #file with 200 values
    g = open("results2.txt", "w")

    b = Knapsack(0, 0, 0, 0)
    b.readFromFile()
    sum = 0
    best = 0

    for i in range (10):
        k = int(input ('introduceti nr iteratii:'))
        f = b.RHC(k)
        g.write("nr iteratii: ")
        g.write(str(k))
        g.write(" - fitness ")
        g.write(str(f))
        g.write("\n")
        if ( f > best ):
            best = f
        sum = sum + f

    g.write("best ")
    g.write(str(best))
    g.write(" | avg ")
    g.write(str(sum/10))


if __name__ == '__main__':
    main()
