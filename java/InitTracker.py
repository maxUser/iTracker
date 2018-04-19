
# Need to number multiple enemies. 
# e.g. Hill Giant 1, Hill Giant 2

class Combatant:
    def __init__(self, name, initiative):
        self.name = name
        self.initiative = initiative
# INSERT COMBATANTS INTO LIST
numberOfEnemies = input('Number of enemies: ')
numberOfAllies = input('Number of allies: ')
totalCombatants = []
iterateEnemy = 0
while iterateEnemy < numberOfEnemies:
    print('===================')
    enemyName = raw_input('Enemy name: ')
    enemy_initBonus = input('Dexterity bonus: ')
    numberOfEachEnemy = input('Number of %(enemyName)ss: ' %{'enemyName':enemyName})
    j = 0
    iterateEnemy += numberOfEachEnemy
    while j < numberOfEachEnemy:
        from random import randint
        enemy_initiative = (randint(1,20))
        enemy_initiative += enemy_initBonus
        combatant = Combatant(enemyName, enemy_initiative)
        totalCombatants.append(combatant)
        j += 1
iterateAlly = 0
while iterateAlly < numberOfAllies:
    print('===================')
    allyName = raw_input('Ally name: ')
    allyInit = input('Initiative: ')
    combatant = Combatant(allyName, allyInit)
    totalCombatants.append(combatant)
    iterateAlly += 1
# SORT LIST
def selectionSort(totalCombatants):
    temp = Combatant('noname', -1);
    for i in range(0, len(totalCombatants)):
        temp = totalCombatants[i]
        j = i
        while j > 0 and totalCombatants[j-1].initiative < temp.initiative:
            totalCombatants[j] = totalCombatants[j-1]
            j -= 1
        totalCombatants[j] = temp
selectionSort(totalCombatants)
# PRINT LIST TO CONSOLE
print "~~~Combat Order~~~"
for i in range (0, len(totalCombatants)):
    print totalCombatants[i].name, totalCombatants[i].initiative
# PRINT LIST TO FILE
f = open('initiative_order.txt', 'w')
for i in range (0, len(totalCombatants)):
    f.write(totalCombatants[i].name + ' ' + str(totalCombatants[i].initiative) + '\n')
f.close()
