class Baby():
    def __init__(self , ide ):
        self.ide = ide
        self.rcontact = [] # it is not needed for the baby but it can reduce some conditions (not treat the baby differently)
        self.pcontact = [] # stands for permanent contact and it is familly contact for the baby 
        self.poss = .1 # possibility of getting infected (this factor takes in concideration waching hands and protection factors)
        self.spreadrate = .1 # the baby is likely to infect his parents if one of them infected him and siblings
        self.infected = False # True or False 
        self.recoverd = False # you can't recover if you are not sick
        self.mrate = .001 # mortality rate
        self.alive = True # it is usefull is he died even if chances are so low
        self.days = 0 # how many days he was infected 
        self.dailyinf = 0 # how many person he infected in one day
        self.totalinf = 0 # how many infaction he caused
        self.type = 'baby' # it serves the purpose  
class Student():
    def __init__(self , ide ):
        self.ide = ide
        self.pcontact = [] # stands for permanent contact and it is familly contact and classroom contact
        self.rcontact = [] # some random action in the street in public transport 
        self.ccontact = [] # the class contact 
        self.poss = .4
        self.spreadrate = .4
        self.infected = False 
        self.recoverd = False
        self.mrate = .009
        self.alive = True
        self.days = 0
        self.dailyinf = 0
        self.totalinf = 0
        self.type = 'student'
class Teacher():
    def __init__(self , ide ):
        self.ide = ide
        self.pcontact = []
        self.rcontact = []
        self.ccontact = [] # the class contact 
        self.poss = .3
        self.spreadrate = .3
        self.infected = False 
        self.recoverd = False
        self.mrate = .015
        self.alive = True
        self.days = 0     
        self.dailyinf = 0
        self.totalinf = 0
        self.type = 'teacher'
class Doctor():
    def __init__(self , ide ):
        self.ide = ide
        self.pcontact = []
        self.rcontact = []
        self.poss = .3
        self.spreadrate = .1
        self.infected = False 
        self.recoverd = False
        self.mrate = .015
        self.alive = True
        self.days = 0
        self.dailyinf = 0
        self.totalinf = 0
        self.type = 'doctor'
class Worker():   
    def __init__(self , ide ):
        self.ide = ide
        self.pcontact = []
        self.rcontact = []
        self.poss = .3
        self.spreadrate = .3
        self.infected = False 
        self.recoverd = False
        self.mrate = .015
        self.alive = True
        self.days = 0
        self.dailyinf = 0
        self.totalinf = 0
        self.type = 'worker'
class Old():   
    def __init__(self , ide ):
        self.ide = ide
        self.pcontact = []
        self.rcontact = []
        self.poss = .5
        self.spreadrate = .5
        self.infected = False  
        self.recoverd = False
        self.mrate = .20
        self.alive = True
        self.days = 0   
        self.dailyinf = 0
        self.totalinf = 0
        self.type = 'old'