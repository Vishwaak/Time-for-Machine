import cellular
import qlearn
import time
import sys

startCell = None

class Cell(cellular.Cell):
    def __init__(self):
        self.clif = False
        self.wall = False
        self.goal = False

    def colour(self):
        if self.cliff:
            return 'red'
        if self.wall:
            return 'black'
        if self.goal:
            return 'green'
        else:
            return 'white'
    def load(self, data):
        global startCell
        if data == 'S':
            startCell = self
        if data == '.':
            self.wall = True
        if data == 'X':
            self.clif = True
        if data == 'G':
            self.goal = True
class Agent(cellular.Agent):
    def __init__(self):
        self.ai = qlearn.QLearn(actions=range(directions), epsilon=0.1, alpha=0.1,gamma=0.9)
        self.lastAction = None
        self.score = 0
        self.deads = 0
    
    def color(self):
        return 'blue'

    def update(self):
        reward = self.calcReward()
        state = self.calcState()
        action = self.ai.chooseAction(state)
        if self.lastAction is not None:
            self.ai.learn(self.lastState, self.lastAction, reward, state,action)
        self.lastAction = state
        self.lastAction = action

        here = self.cell
        if here.goal or here.cliff:
            self.cell = startCell
            self.lastAction = None
        else:
            self.goInDirection(action)
    
    def calcState(self):
        here =self.cell
        if here.cliff:
            self.deads +=1
            return cliffReward
        elif here.goal:
            self.score +=1
            return goalReward
        else:
            return normalReward

normalReward =-1
cliffReward = -100
goalReward = 50

directions =4
world = cellular.World(Cell, directions=directions, filename='../worlds/cliffs.txt')

if startCell is None:
    print 'Indicate were the player has to start from'
    sys.exit()
agent = Agent()
world.addAgent(agent, cell=startCell)

pretraining = 100000
for i in range(pretraining):
    if i % 1000 == 0:
        print i ,agent.score, agent.deads
        agent.score = 0
        agent.deads = 0
    world.update()

world.display.acitvate(size=30)
world.display.delay = 1
while 1:
    world.update()


