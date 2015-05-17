__email__ = 'tramel.jones@gmail.com'
__author__ = 'Tramel Jones'
# Top Coder  Single Round Match 659 Round 1 - Division I, Level One
#
# Problem Statement
#     	Garth likes apples and oranges. Recently he bought N fruits, where each fruit was either an apple or an orange. Then he ate all N fruits in some order. You are given an int K. Garth observed that at every point in time, if he made a list of the last K fruits he ate, there were at most K/2 (rounded down) apples in this list.
#
#
#
# For each valid i, you know that the info[i]-th fruit Garth ate was an apple. (Fruits Garth ate are numbered starting from 1. For example, info[i]=1 means that the very first fruit Garth ate was an apple.)
#
#
#
# Please find and return the maximum number of apples Garth could have eaten.
#
# Definition
#
# Class:	ApplesAndOrangesEasy
# Method:	maximumApples
# Parameters:	int, int, int[]
# Returns:	int
# Method signature:	int maximumApples(int N, int K, int[] info)
# (be sure your method is public)
#
#
# Notes
# -	If Garth makes his list at a point in time when he ate fewer than K fruits, his list will have fewer than K fruits but the requirement will still be the same: there have to be at most K/2 apples in the list.
#
# Constraints
# -	N will be between 2 and 2,000, inclusive.
# -	K will be between 2 and N, inclusive.
# -	info will contain between 0 and N elements, inclusive.
# -	Each element of info will be between 1 and N, inclusive.
# -	The elements of info will be distinct.
# -	The elements of info will be consistent with Garth's observation.
#
# Examples
# 0)
#
# 3
# 2
# {}
# Returns: 2
# Garth ate N=3 fruites. The requirement is that any K=2 consecutive fruits may contain at most K/2 = 1 apple. As info is empty, you have no additional information about the fruits Garth ate.
#
#
#
# Garth might have eaten an apple, then an orange, then an apple. This satisfies the conditions:
# After eating the 1st fruit, the list is [apple].
# After eating the 2nd fruit, the list is [apple, orange].
# After eating the 3rd fruit, the list is [orange, apple].
# Each list contains at most 1 apple.
# 1)
#
# 10
# 3
# {3, 8}
# Returns: 2
# All fruits, except for the 3rd and the 8th, must have been oranges.
# 2)
#
# 9
# 4
# {1, 4}
# Returns: 5
# 3)
#
# 9
# 4
# {2, 4}
# Returns: 4
# 4)
#
# 23
# 7
# {3, 2, 9, 1, 15, 23, 20, 19}
# Returns: 10

class ApplesAndOrangesEasy:
    def ApplesAndOrangesEasy(self):
        self.n = 0
        self.k = 0
        self.info = []
    def maximumApples(self, n, k, info):
        #print "n: " + str(n)
        #print "k: " + str(k)
        #print "info: " + str(info)
        kmax = k/2
        #print "kmax: " + str(kmax)
        self.maxApples = 0
        self.fruit = []
        self.queue = []
        self.greedqueue = []
        for x in range(n):
            self.fruit.append(0)
        for apple in info:
            #print "apple: " + str(apple)
            #self.maxApples += 1
            #print "maxApples: " + str(self.maxApples)
            self.fruit[apple-1] = 1
        for x in range(n):
            if len(self.queue) == k:
                #print "deleting head. "
                del self.queue[0]
                del self.greedqueue[0]
            if self.fruit[x] == 1:
                if sum(self.queue)+sum(self.greedqueue) >= kmax:
                    count = len(self.queue)-1
                    for item in reversed(self.greedqueue):
                        if item == 1:
                            #print "Removing greedy insert"
                            self.greedqueue[count] = 0
                            self.maxApples -= 1
                            #print "maxApples: " + str(self.maxApples)
                            break
                        count -= 1
                #print "Info match. Appending 1"
                self.queue.append(1)
                self.greedqueue.append(0)
                self.maxApples+= 1
                #print "maxApples: " + str(self.maxApples)
            elif sum(self.queue)+sum(self.greedqueue) >= k/2:
                #print "K/2 limit reached. Appending 0"
                #if len(self.queue) >1:
                #    self.queue.pop()
                self.queue.append(0)
                self.greedqueue.append(0)
            else:
                #print "Greedy...Appending 1"
                self.queue.append(0)
                self.greedqueue.append(1)
                self.maxApples+= 1
                self.fruit[x] = -1
                #print "maxApples: " + str(self.maxApples)
            #print "queue: " + str(self.queue)
            #print "greedqueue: " + str(self.greedqueue)

        #print "fruites: " + str(self.fruit)
        #print "queue: " + str(self.queue)
        #print "greedqueue: " + str(self.greedqueue)
        return self.maxApples

def main():
    SomeApples = ApplesAndOrangesEasy()
    print "maximumApples(3, 2, [])  Expected value: 2"
    print "Actual value: " + str(SomeApples.maximumApples(3, 2, []))
    print "maximumApples(10, 3, [3, 8])  Expected value: 2"
    print "Actual value: " + str(SomeApples.maximumApples(10, 3, [3, 8]))
    print "maximumApples(9, 4, [1, 4])  Expected value: 5"
    print "Actual value: " + str(SomeApples.maximumApples(9, 4, [1, 4]))
    print "maximumApples(9, 4, [2, 4])  Expected value: 4"
    print "Actual value: " + str(SomeApples.maximumApples(9, 4, [2, 4]))
    print "maximumApples(23, 7, [3, 2, 9, 1, 15, 23, 20, 19])  Expected value: 10"
    print "Actual value: " + str(SomeApples.maximumApples(23, 7, [3, 2, 9, 1, 15, 23, 20, 19]))

if __name__ == "__main__":
    main()
#Requires a way to differentiate between guessed (greedy) apples vs real (given) apples
#Implemented solution uses a greedy queue to keep track of greedy inserts.