import random
import math

class Qlearn:
    def __init__(self,actions,epsilon=0.1,alpha=0.2,gamma=0.9):
        self.q = {}
        self.epsilon = epsilon
        self.gamma = gamma
        self.actions = actions
        self.alpha = alpha
    
    def getQ(self,state,action):
        return self.q.get((state,action),0.0)

    def learnQ(self,state,action,reward,value):
        oldv = self.q.get((state,action), None)
        if oldv is None:
            self.q[(state,action)] = reward
        else:
            self.q[(state, action)] = oldv + self.alpha * (value -oldv)
    
    def chooseAction(self, state, return_q=False):
        q = [self.getQ(state, a) for a in self.actions]
        maxQ = max(q)

        if random.random() < self.epsilon:

            minQ = min(q); mag = max(abs(minQ), abs(maxQ))
            q = [q[i] + random.random() * mag - .5 * mag for i in range(len(self.actions))]
            maxQ = max(q)
        count = q.count(maxQ)

        if count > 1:
            best = [i for i in range(len(self.actions)) if q[i] == maxQ]
            i = random.choice(best)
        else:
            i = q.index(maxQ)
        action = self.actions[i]
        if return_q:
            return action, q
        return action

    def learn(self, state1, action1, reward,state2):
        maxqnew = max([self.getQ(state2,a)for a in self.actions])
        self.learnQ(state1, action1,reward, reward + self.gamma*maxqnew)

def ff(f,n):
    fs = "{:f}".format(f)
    if len(fs) < n:
        return ("(:"+n+"s}").format(fs)
    else:
        return fs[:n]