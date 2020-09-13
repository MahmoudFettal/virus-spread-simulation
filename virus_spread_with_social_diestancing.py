# This program simulates the spread of a virus in society
# the society is an oriented object set of class and every individual have random connection and permanent connection
# the import section 
'''# nothing big all we need is matplotlib.pyplot and random 
   # due to the use of randint and choices we will import them separately so the code can be a bit easier to read'''
import matplotlib.pyplot    as plt
import matplotlib.style     as style
import matplotlib.animation as animation
import random
from matplotlib import style
from random     import randint # randint gives a random value between two number a and b the edges included
from random     import choice # choices give a list of random values from a given list
from random     import randint
from random     import choice
from society    import Student
from society    import Baby
from society    import Teacher
from society    import Doctor
from society    import Worker
from society    import Old
style.use('fivethirtyeight')
# the class  section 
''' we are going to use 6 class 
    the Baby 
    the Student 
    the Teacher (have more interactions than normal worker)    
    the Doctor  (he have a less chance to infect people or to get infected because he is so worried about the virus (it is only my way of seeing the problem))
    the Worker  (the normal worker have less contact than the teacher and less worried about the virus)
    the old     (have a high mortalaty rate due to the virus) '''

# starting variables  
pop = 10000   # here we give the size of our population (it is better to have it as a 10 power)
f = pop//100  # since the first calculation were made in 100 pop the f can keep the same job for the other pops 
# the functions section
'''# and old trick from the book 
   # to make possibilties we give 1000 number and we take a random number from 0 to 999 if the number is < (possibilty * 1000) it is true is not it is false
   # i did 1000 cuz the moratality rate is so small for children '''
def possibility(p):
    per = int(p*1000)
    randoms = randint(0,999)
    if randoms <= per:
        return True
    else:
        return False
# the randomf stands for random families it makes random families a worker couple and 1 or 2 children for each family 
def randomf():
    pops = [i for i in range(50*f)]
    kids = [1 for i in range(8*f)] + [2 for i in range(17*f)]
    sons = [i for i in range(42*f)]
    families = []
    while pops != []:
        a,c = choice(pops),kids.pop(randint(0,len(kids)-1))
        pops.pop(pops.index(a))
        b = choice(pops) 
        pops.pop(pops.index(b))
        family = [a,b]
        for _ in range(c):
            d = choice(sons)
            family.append(d)
            sons.pop(sons.index(d))
        families.append(family)
    return families
# random connection is a function double random to make contact between random people
def randomConnections(types,b):
    a = randint(0,randint(0,b))
    connections = random.sample(range(len(connect)),a) 
    if types == 'w':
        connections = [connect[i] for i in connections]
    elif types == 's':
        l = connections[len(connections)//2:]
        connections = [students[i%(38*f)] for i in connections[:len(connections)//2]]
        connections = connections + [connect[i] for i in l]
    elif types == 'o':
        connections = [connect[i] for i in connections]
    return connections
# setting up a society 
''' # now with real data we are going to devide the age of the people but we are going to make some randomness in ages within categories 
    #the data we have is from "https://www.un.org/en/development/desa/population/events/pdf/expert/25/2016-EGM_Nicole%20Mun%20Sam%20Lai.pdf"
    # a child is 0-14, young 15-24, worker 25-64, old +65
    # we are going to have 260 child ,160 young ,500 worker and 80 old
    # to give every young and child a mother and dad 250 worker have one child and 170 have 2 
    # every worker have 16% chance to have one parent 
    # a small change was made to the data for adapatatie reasons
    # we now have in 1000 there is 40 baby 380 student 50 teacher 50 doctor 400 normal worker 80 old 
    # in the defintion it is made with the f to keep it true for every pop needed '''
babies     =  [Baby(i) for i in range(1,4*f+1)]
students   =  [Student(i) for i in range(1,38*f+1)]
teachers   =  [Teacher(i) for i in range(1,5*f+1)]
doctors    =  [Doctor(i) for i in range(1,5*f+1)]
workers    =  [Worker(i) for i in range(1,40*f+1)]
olds       =  [Old(i) for i in range(1,8*f+1)]
population =  babies + students + teachers + doctors + workers + olds 
tworkers   =  teachers + doctors + workers
kids       =  babies + students 
connect    =  students + tworkers + olds # the babies have less interaction with the world so let's leave them out of connections
classrooms  = list()
for i in range(len(students)//20):
    classrooms.append([students[i] for i in range(i*20 ,(i+1)*20)])
# and now assign each classe with a teacher
for i in range(5*f):
    teachers[i].ccontact += classrooms[i%len(classrooms)] # every teacher have only one classroom but every 
    k = 0
    for j in classrooms[i%len(classrooms)]:
        copyclasse = classrooms[i%len(classrooms)].copy()
        copyclasse.pop(k) 
        classe = copyclasse + [teachers[i]]
        j.ccontact += classe
        k=k+1
families = randomf() 
for i in families:
    parents = i[:2]
    children = i[2:]
    for j in parents:
        ch = []
        for k in children:
            ch.append(kids[k])
        tworkers[j].pcontact += ch
    if len(children) == 1:
        kids[children[0]].pcontact += [tworkers[i[0]],tworkers[i[1]]]
    else:
        kids[children[0]].pcontact += [tworkers[i[0]],tworkers[i[1]],kids[children[1]]]
        kids[children[1]].pcontact += [tworkers[i[0]],tworkers[i[1]],kids[children[0]]]
# we now have families made 
# the virus infections starts from here 
b    = 15 # is the limit of random contacts 
zero = randint(4*f,pop-1) # the patient zero
population[zero].infected = True # we change his statue of course
population[zero].days     = 1 # we count his days of infection 
days     = 1 # the pandamic days
cases    = 1 # the number of tatal cases
deaths   = 0 # the number of total deaths
recoverd = 0 # the number of total recoveries
casesl   = []# newcases in a list for the plot
casest   = []# cases in a list for the plot
deathsl  = []# newdeaths in a list for the plot
deathst  = []# deaths in a list for the plot
recoverl = []# newrecovery in a list for the plot
recovert = []# recovery in a list for the plot
popl     = []# the population number -1 if someone dies
print(len(population))
# it end when cases == deaths + recovered 
while cases != deaths + recoverd:
    newcases    = 0 # the daily cases
    newdeaths   = 0 # the daily deaths
    newrecovery = 0 # the daily recovery
    # everyday there is random contact
    for i in tworkers:
        i.rcontact += randomConnections('w',b) 
    for i in students:
        i.rcontact += randomConnections('s',b-2)
    for i in olds:
        i.rcontact += randomConnections('o',b-1)
    for p in population:
    # if the person is infected and alive and not recovered (he recovered he won't get sick again) and more than 5 days of the infection(let the virus spread in the body)
    # and in the 10th day he go to the hospital (just supposition)
        if p.infected and p.alive :
            p.days += 1
            # when the cases surpasse 500 we close schools and we limit the contact
            if (p.type == 'student' or p.type == 'teacher') and cases < 500 :
                contact = p.pcontact + p.rcontact + p.ccontact
            else:
                b = 2
                contact = p.pcontact + p.rcontact
            for j in contact : 
                if possibility(p.spreadrate) and possibility(j.poss) and j.infected == False  and not(j.recoverd) and 5 < p.days <=10:
                    j.infected  = True 
                    p.dailyinf += 1
                    p.totalinf += 1
                    newcases   += 1
                    cases      += 1
            if p.days == 15:
                if possibility(p.mrate):
                    newdeaths  += 1
                    deaths     += 1
                    p.alive     = False      # soooo saaad
                else:
                    newrecovery += 1
                    recoverd    += 1 
                    p.recoverd   = True      # lucky him he recovered
                    p.infected   = False     # lucky him he recovered
    casesl.append(newcases)
    deathsl.append(newdeaths)
    recoverl.append(newrecovery)
    casest.append(cases)
    deathst.append(deaths)
    recovert.append(recoverd)
    if days == 1:
        popl.append(pop)
    else:
        popl.append(popl[-1]-newdeaths)
    print('day: ',days)
    print('newdata: ', newcases,newdeaths,newrecovery)    
    print('alldata: ',cases,deaths,recoverd) 
    person = population[0]
    if newcases != 0:
        persontype,dailyinf = person.type,person.dailyinf
        for i in population:
            if i.dailyinf>dailyinf:
                persontype = i.type
                dailyinf   = i.dailyinf
            i.rcontact = []
            i.dailyinf = 0
        print('the most infaction were by a ',persontype, 'and he infected ',dailyinf,' people')
    days +=1 
old, olds    = 0,0
adult,adults = 0,0
young,youngs = 0,0
baby,babys   = 0,0 # the deed and not infected at all
person = population[0]
for i in population:
    if not(i.infected) and not(i.recoverd):
        if i.type == 'old':
            olds += 1
        elif i.type == 'worker' or i.type == 'teacher' or i.type == 'doctor':
            adults += 1
        elif i.type == 'baby':
            babys += 1
        else:
            youngs +=1 
    elif i.totalinf > person.totalinf:
        person = i
    if not(i.alive):
        if i.type == 'old':
            old += 1
        elif i.type == 'worker' or i.type == 'teacher' or i.type == 'doctor':
            adult += 1
        elif i.type == 'baby':
            baby += 1
        else:
            young +=1 
print('the most infacting: ',person.type , 'and he infected ',person.totalinf,' people')
if olds + babys + youngs + adults != 0:
    print('the not infected liste: ')
    print('old people :',olds)
    print('babies :',babys)
    print('young people :',youngs)
    print('adults :',adults)
print('the deaths liste: ')
print('old people make :',(old/(old+young+baby+adult))*100)
print('babies make :',(baby/(old+young+baby+adult))*100)
print('young people make :',(young/(old+young+baby+adult))*100)
print('adults make :',(adult/(old+young+baby+adult))*100)
fig,axs  = plt.subplots(2,3)
file = open('cases.txt','w') 
casesl = casesl.copy()
file.write(str(1)+' '+str(casesl.pop(0))+' '+str(deathsl.pop(0))+' '+str(recoverl.pop(0))+' '+str(casest.pop(0))+' '+str(deathst.pop(0))+' '+str(recovert.pop(0))+'\n')
file.close()
def animate(i):
    graphs_data = open('cases.txt','r')
    lines = graphs_data.read()
    lines = lines.split('\n')
    days = []
    ys   = []
    zs   = []
    ts   = []
    sa   = []
    bs   = []
    cs   = []
    for line in lines:
        if len(line) > 1:
            x,y,z,t,a,b,c= line.split(' ')
            days.append(int(x))
            ys.append(int(y))
            zs.append(int(z))
            ts.append(int(t))
            sa.append(int(a))
            bs.append(int(b))
            cs.append(int(c))
    axs[0,0].clear()
    axs[0,1].clear()
    axs[0,2].clear()
    axs[1,0].clear()
    axs[1,1].clear()
    axs[1,2].clear()
    axs[0,0].plot(days, ys,'orange')  
    axs[0,1].plot(days, zs,'red') 
    axs[0,2].plot(days, ts,'green') 
    axs[0,0].set_xlabel('days')
    axs[0,0].set_ylabel('daily cases')
    axs[0,1].set_xlabel('days')
    axs[0,1].set_ylabel('daily deaths')
    axs[0,2].set_xlabel('days')
    axs[0,2].set_ylabel('daiy recovery')
    axs[1,0].plot(days, sa,'orange')  
    axs[1,1].plot(days, bs,'red') 
    axs[1,2].plot(days, cs,'green') 
    axs[1,0].set_xlabel('days')
    axs[1,0].set_ylabel('cases')
    axs[1,1].set_xlabel('days')
    axs[1,1].set_ylabel('deaths')
    axs[1,2].set_xlabel('days')
    axs[1,2].set_ylabel('recovery')
    if casesl != []:
        graphs_data = open('cases.txt','a')
        graphs_data.write(str(int(days[-1])+1)+' '+str(casesl.pop(0))+' '+str(deathsl.pop(0))+' '+str(recoverl.pop(0))+' '+str(casest.pop(0))+' '+str(deathst.pop(0))+' '+str(recovert.pop(0))+'\n')
        file.close()
animation = animation.FuncAnimation(fig, animate, interval=200)
plt.show()