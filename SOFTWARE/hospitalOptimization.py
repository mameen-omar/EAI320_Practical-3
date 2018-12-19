#Mohamed Ameen Omar
#u16055323
#EAI Practical 3
#2018
import math
import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import sys
import random
import matplotlib
from mpl_toolkits.mplot3d import Axes3D
class member:
    def __init__(self,location):
        #stored as binary
        self.row = location[0]
        self.col = location[1]
class hospitalOptimization:
    def __init__(self):
        #river is at index 7!!!!!!!!!!
        self.grid = np.array(
                            [[2, 1, 7, 9, 1, 9, 3, 12, 12, 2, 13, 12, 11, 10, 8, 12],
                            [ 1, 1, 2, 4, 8, 6, 2, 12, 5, 4, 17, 16, 8, 6, 10, 8],
                            [ 4, 1, 7, 12, 6, 10, 1, 2, 2, 2, 7, 4, 15, 1, 5, 10],
                            [ 7, 12, 7, 2, 6, 6, 13, 9, 12, 4, 23, 14, 15, 12, 1, 8],
                            [ 10, 11, 8, 7, 8, 7, 8, 7, 16, 15, 2, 15, 3, 14, 6, 10],
                            [ 8, 1, 4, 1, 7, 6, 2, 9, 3, 13, 10, 15, 6, 3, 8, 7],
                            [ 5, 8, 5, 5, 10, 6, 8, 10, 2, 8, 12, 10, 1, 8, 8, 10],
                            [ 6, 12, 5, 5, 12, 2, 7, 2, 2, 11, 3, 5, 6, 10, 10, 7],
                            [ 11, 4, 8, 12, 10, 4, 5, 12, 1, 4, 6, 1, 6, 2, 9, 12],
                            [ 8, 1, 7, 4, 6, 11, 8, 7, 10, 6, 5, 2, 5, 1, 12, 2],
                            [ 4, 5, 8, 6, 1, 11, 5, 12, 6, 5, 7, 4, 12, 6, 8, 11],
                            [ 7, 10, 2, 6, 12, 6, 4, 8, 7, 8, 11, 11, 6, 2, 11, 2],
                            [ 11, 8, 8, 11, 5, 8, 4, 2, 8, 12, 5, 12, 10, 12, 2, 10],
                            [ 2, 6, 10, 1, 10, 10, 5, 1, 11, 4, 8, 6, 8, 12, 11, 6],
                            [ 11, 12, 5, 10, 11, 2, 1, 1, 2, 10, 12, 12, 11, 12, 12, 8],
                            [ 2, 1, 5, 7, 11, 7, 5, 2, 4, 7, 11, 1, 4, 12, 4, 5]])
        self.minimumCost = -1
        self.minLocation = []
        self.bridge1 = [2,7] #bridge locations
        self.bridge2 = [9,7] #bridge locations
        self.myPopulation = [] #does not include any locations in river
        self.populationSize = 120
        self.numGenerations = 10
        self.mutationRate = 0.50       
        np.random.seed(int(time.time() ))
    
    #get the distance between two blocks
    def getDistance(self,row,col,row1,col1):
        if(self.sameSide(col,col1) == True):
            return self.getEuclideanDistance(row,col,row1,col1)
        else:
            return self.getDistanceViaBridge(row,col,row1,col1)
     
    #returns a boolean whether blocks are on the same side of the river
    def sameSide(self,col,col1):
        if( ( (col <= 7) and (col1 <= 7) )  or ( (col >= 7) and (col1 >= 7) ) ):
            return True
        else:
            return False
    
    #gets Euclidean distance between the two
    def getEuclideanDistance(self,row,col,row1,col1):
        distance = 0        
        if(row > row1):
            temp = row-row1
            distance += (temp*temp)        
        else:
            temp = row1-row
            distance += (temp*temp)
        if(col > col1):
            temp = col-col1
            distance += (temp*temp)        
        else:
            temp = col1-col
            distance += (temp*temp)        
        return(math.sqrt(distance))
        
    #get the distance between two points via a bridge
    def getDistanceViaBridge(self,row,col,row1,col1):
        temp1 = self.getEuclideanDistance(row,col,self.bridge1[0],self.bridge1[1]) 
        temp1 += self.getEuclideanDistance(self.bridge1[0],self.bridge1[1],row1,col1)        
        temp2 = self.getEuclideanDistance(row,col,self.bridge2[0],self.bridge2[1]) 
        temp2 += self.getEuclideanDistance(self.bridge2[0],self.bridge2[1],row1,col1)        
        if(temp1 > temp2):
            return temp2
        else:
            return temp1
    
    def getClosestBridge(self,row):
        #if distance from my row to bridge1 is greater than didtance to bridge2
        if( math.fabs(row-self.bridge1[0])  > math.fabs(row - self.bridge2[0]) ):
            return self.bridge2
        else:
            return self.bridge1
    
    #a fucntion that gives the totalCost for a particular location as a hospital
    def costFunction(self, row,col):
        totalCost = 0
        for i in range(0,16):
            for j in range(0,16):
                totalCost += ( self.grid[i][j] * (self.averageResponseTime(i,j,row,col) ) )
        if(self.minimumCost == -1):            
            if(col != 7):
                self.minLocation = [row,col]
                self.minimumCost = totalCost
        #minimum must not be in the river or be a bridge
        elif( (self.minimumCost > totalCost) and (col != 7) ):
            self.minLocation = [row,col]
            self.minimumCost = totalCost  
        return totalCost
    
    #average repsonse time equation given to us
    def averageResponseTime(self, row,col,row1,col1):
        dist = self.getDistance(row,col,row1,col1)
        temp = 2.4 + (4.5 * dist)
        return( temp )
         
    def plotCostSurface(self):
        #row = x
        #col = y
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        x = y = np.arange(0, 16, 1)
        Xmesh, Ymesh = np.meshgrid(x, y)
        z = np.array( [self.costFunction(x, y) for x, y in zip(np.ravel(Xmesh), np.ravel(Ymesh) )] )
        Zmesh = z.reshape(Ymesh.shape)
        ax.plot_surface(Xmesh, Ymesh, Zmesh, rstride=1, cstride=1, cmap=cm.spectral,
                        linewidth=0, antialiased=True)        
        ax.set_xlabel('X-Coordinate')
        ax.set_ylabel('Y-Coordinate')
        ax.set_zlabel('Cost')
        ax.set_title("COST SURFACE PLOT\n")
        print("OPTIMAL LOCATION IS :", self.minLocation)
        print("OPTIMAL COST IS: ", self.minimumCost)
        sys.stdout.flush()
    
    #gets best location for the hospital
    def getPrimeLocation(self):
        for i in range(0,16):
            for j in range(0,16):
                self.costFunction(i,j)
        
    def getInitialPopulation(self):
        for x in range(0,self.populationSize):
            loc = self.getRandomBlock()
            loc = self.verifyLocation(loc) #not repeated
            self.myPopulation.append( member(loc) ) 
    
    #gets a random location for the population       
    def getRandomBlock(self):
        return [self.getRandomRow(),self.getRandomCol()]
    #in binary
    def getRandomRow(self):
        row = "{0:b}".format(np.random.randint(0, 16))
        while(len(row) < 8):
            row = "0"+row
        return row
    #in binary
    def getRandomCol(self):
        col = np.random.randint(0,16)        
        while(col == 7):
            col = np.random.randint(0,16)
        col = "{0:b}".format(col)
        while(len(col) < 8):
            col = "0" + col
        return col
    
    #verifies a location is not repeated
    def verifyLocation(self,loc):
        again = True
        if(self.myPopulation != []):
            while(again == True):
                for x in range(0,len(self.myPopulation)):
                    if( (self.myPopulation[x].row == loc[0]) and self.myPopulation[x].col == loc[1] ):
                        loc = self.getRandomBlock()
                        break
                again = False        
        return loc
    
    def binaryToInt(self, b = "{0:b}"):
        return int(b,2)        
        
    #prints the population
    def printPopulation(self):
        for x in range(0,len(self.myPopulation)):
            print(self.binaryToInt(self.myPopulation[x].row), end="")
            print(",",end="")
            print(self.binaryToInt(self.myPopulation[x].col))
  
    def geneticAlgorithm(self): 
        run = 20
        success = 0
        for z in range(0,run):            
            self.myPopulation = []
            self.getPrimeLocation()
            for x in range(0,self.numGenerations):
                sys.stdout.flush()
                if(self.myPopulation == []):
                    self.getInitialPopulation()
                invertedCosts = self.sortFitness() #a list of highest to lowest cost
                pairs = self.getBreedingPairs(self.getProbabilities(invertedCosts))#breedingPairs,consecutive not repeated
                newPop = self.breedPairs(pairs)#next generation has been proudued
                self.myPopulation = newPop
            self.sortFitness()
            print("This is run number",z+1)
            print("Best solution found is:", end = "")
            print("[", end = "")
            print(self.binaryToInt(self.myPopulation[0].row), end = "")
            print(",", end = "")
            print(self.binaryToInt(self.myPopulation[0].col), end = "")
            print("]")
            if(self.binaryToInt(self.myPopulation[0].row) == 9 and self.binaryToInt(self.myPopulation[0].col) == 8):
                success += 1
        #self.printPopulation()        
        print("The result of running GA", run, end = "")
        print(" times:", (success/run)*100, end = "")
        print("% success rate")

    #returns a list of "new" costs assosiated with the "new" pop
    def sortFitness(self):
        list = []        
        for x in range(0,len(self.myPopulation)):
            row = self.binaryToInt(self.myPopulation[x].row)
            col = self.binaryToInt(self.myPopulation[x].col)
            cost = self.costFunction(row,col)
            list.append((cost,self.myPopulation[x]))   
        #its in order of lowest to highest cost
        list = self.sortList(list)
        newPop = []
        invertedCosts = []
        y = len(list) -1
        for x in range(0,len(list)):
            newPop.append( (list[x])[1] )#sort my population in asceding order of cost
            invertedCosts.append( (list[y])[0] )
            y = y-1            
        self.myPopulation = newPop
        #mypoualtion[0] is now the location with the lowest cost
        return invertedCosts      
    
    #sorts a list of tuples in ascending order
    def sortList(self,list):
        sorted = False        
        while(sorted == False):
            swap = False
            for x in range(0,len(list) -1):
                if(list[x][0] > list[x+1][0]):
                    swap = True
                    temp = list[x]
                    list[x] = list[x+1]
                    list[x+1] = temp
            if(swap == False):
                sorted = True
        return list
    
    #get probabilities based off weighted avergae
    def getProbabilities(self, costs):
        sum = 0
        for x in range(len(costs)):
            sum+= costs[x]
        probs = []
        for x in range(len(costs)):
            prob = costs[x]
            prob = (costs[x]/sum) #probility
            probs.append(prob)
        return probs
  
    #get random breeding pairs based off of probilities with no repeated in a pair
    def getBreedingPairs(self,probs):
        pairs = []
        pairs = np.random.choice(self.myPopulation,self.populationSize,True,probs) 
        x = 0
        while(x < len(pairs)-1):
            while( (pairs[x].row == pairs[x+1].row) and (pairs[x].col == pairs[x+1].col) ):
                pairs[x] = np.random.choice(self.myPopulation,1,True,probs)[0]
            x = x+2
        return pairs
    
    #breed the pairs
    def breedPairs(self,pairs):
        x = 0
        list = []
        while(x<len(pairs)):
            rows = self.crossRows(self.myPopulation[x].row,self.myPopulation[x+1].row,np.random.randint(0,7))
            cols = self.crossCols(self.myPopulation[x].col,self.myPopulation[x+1].col,np.random.randint(0,7))   
            newMember = member( [ rows[0],cols[0] ] )
            if(self.shouldMutate() == True):
                newMember = self.mutate(newMember)
            newMember2 = member( [rows[1],cols[1] ])   
            if(self.shouldMutate() == True):
                newMember2 = self.mutate(newMember2)
            list.append(newMember)
            list.append(newMember2)
            x = x+2
        return list
    
    #choose a random position, thats where to cross
    def crossRows(self,row1,row2, index = 7):
        newRow1 = self.getString(row1,row2,index)            
        newRow2 = self.getString(row2,row1,index)    
        while(self.binaryToInt(newRow1) > 15 or self.binaryToInt(newRow2) > 15):
            index = int( np.random.randint(1,7) )
            newRow1 = self.getString(row1,row2,index)            
            newRow2 = self.getString(row2,row1,index) 
        return([newRow1,newRow2])
        
    def crossCols(self,col1,col2,index = 7):
        newCol1 = self.getString(col1,col2,index)          
        newCol2 = self.getString(col2,col1,index)
        while(self.binaryToInt(newCol1) == 7 or self.binaryToInt(newCol2) == 7):
             index = np.random.randint(1,7)
             newCol1 = self.getString(col1,col2,index)          
             newCol2 = self.getString(col2,col1,index) 
        while(self.binaryToInt(newCol1) > 15 or self.binaryToInt(newCol1) > 15):
             again = False
             index = np.random.randint(1,7)
             newCol1 = self.getString(col1,col2,index)          
             newCol2 = self.getString(col2,col1,index) 
             again = self.binaryToInt(newCol1) == 7 or self.binaryToInt(newCol1) == 7
             while(again == True):
                 index = np.random.randint(1,7)
                 newCol1 = self.getString(col1,col2,index)          
                 newCol2 = self.getString(col2,col1,index) 
                 again = self.binaryToInt(newCol1) == 7 or self.binaryToInt(newCol1) == 7
        return([newCol1,newCol2])
     
    def getString(self,s1,s2,end = 5):
      newString = ""
      for x in range(0,end):
          newString = newString + s1[x]
      for x in range(end,len(s2)):
          newString = newString + s2[x]
      return newString
  
    def shouldMutate(self):
        return(random.randrange(0,100) < (self.mutationRate*100))
    
    def mutate(self,temp):
        if(random.randrange(0,100) < 50):
            temp.row = self.getRandomRow()
        else:
            temp.col = self.getRandomCol()
        return temp
    
q = hospitalOptimization()
#print(q.costFunction(9,7))
#q.plotCostSurface()
#q.getInitialPopulation()
#q.printPopulation()
print("Running Genetic Algorithm")
q.geneticAlgorithm()




