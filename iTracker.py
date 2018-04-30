# Features to implement:
# -PC/NPC database
# -Cycle through initiative (use arrow keys) during combat.
#       ~During each turn, the stat block of the creature is displayed
#       ~Keep track of health
# -Unique file names (os.path.isfile('filename'))
# -3 combatant tie checker not even close dude.

# Error checking to implement:
# -line 95: more_enemies = input('More enemies? (y/n): ')
#       ~What happens if other characters are input? wtf does this mean
from Combatant import Combatant
from random import randint
import datetime # to get date for file name
import os.path
tester = 0

# Writing to .txt file of given name and output to terminal.
# Parameter: list of combatants.
def write_to_file(order):
    # comment out file stuff when testing
    today_date = datetime.date.today()
    filename = str(today_date) + '.txt'
    f = open(filename, 'w')
    for i in range(len(order)):
        f.write(order[i].name + ', ' + str(order[i].initiative) + '\n')
        print("{:<13s}".format(order[i].name) + "{:>2s}".format(str(order[i].initiative)) + ' | ' + str(order[i].initiative_bonus))
        # "{:>10s}".format(s)

# If new_combatant has higher init_bonus, swap with order[i].initiative
# Parameter: list of combatants
# Returns: updated list of combatants
def tie_checker(order):
    index_dict = {}
    start = 0
    end = 0
    is_num = False
    # 1 on 1 battle (only 2 combatants)
    if len(order) == 2:
        if order[0].initiative == order[1].initiative:
            if (order[0].pc == True) or (order[1].pc == True):
                print('=====TIE DETECTED=====')
                print('Initiative roll tie!')
                print('\tTIEBREAKER between: ', end='')
                for i in range(len(order)):
                    # print those who are tied
                    if i == len(order)-1:
                        print(order[i].name)
                    else:
                        print(order[i].name + ', ', end='')

                print('\tEnter initiative bonus to break tie:')

                while(is_num == False):
                    try:
                        if order[0].pc == True:
                            order[0].initiative_bonus = int(input('\t' + order[0].name + ': '))
                        if order[1].pc == True:
                            order[1].initiative_bonus = int(input('\t' + order[1].name + ': '))
                        is_num = True
                    except ValueError:
                        print('>>> Invalid input.')
                        print('>>> You must enter an integer.')

                if order[0].initiative_bonus < order[1].initiative_bonus:
                    temp = Combatant()
                    temp = order[0]
                    order[0] = order[1]
                    order[1] = temp
                elif order[0].initiative_bonus == order[1].initiative_bonus:
                    print('\t\tInitiative bonus tie detected!')
                    print('\t\tRoll a d20 to break tie:')

                    is_num = False
                    while is_num == False:
                        try:
                            order[0].roll_off = int(input('\t\t' + order[0].name + ': '))
                            order[1].roll_off = int(input('\t\t' + order[1].name + ': '))
                            is_num = True
                        except ValueError:
                            print('>>> Invalid input.')
                            print('>>> You must enter an integer.')

                    if order[0].roll_off < order[1].roll_off:
                        temp = Combatant()
                        temp = order[0]
                        order[0] = order[1]
                        order[1] = temp
    # 3 combatants
    elif len(order) == 3:
        ties = []
        tie = False
        if order[0].initiative == order[1].initiative:
            ties.append(order[0])
            print('add maxi')
            ties.append(order[1])
            print('add leah')
            tie = True
        if (order[0].initiative == order[2].initiative):
            if order[0] not in ties:
                ties.append(order[0])
            ties.append(order[2])
            tie = True
        if (order[1].initiative == order[2].initiative):
            if order[1] not in ties:
                ties.append(order[1])
                tie = True
            if order[2] not in ties:
                ties.append(order[2])
                tie = True
        if tie == True:
            print('=====TIE DETECTED=====')
            print('Initiative roll tie!')
            print('\tTIEBREAKER between: ', end='')

            for i in range(len(ties)):
                # print those who are tied
                if i == len(ties)-1:
                    print(ties[i].name)
                else:
                    print(ties[i].name + ', ', end='')

            print('\tEnter initiative bonus to break tie:')
            for i in range(len(ties)):
                if ties[i].pc == True:
                    is_num = False
                    while is_num == False:
                        try:
                            order[i].initiative_bonus = int(input('\t' + order[i].name + ': '))
                            is_num = True
                        except ValueError:
                            print('>>> Invalid input.')
                            print('>>> You must enter an integer.')
            # check for init bonus ties
            # store them in bonus_ties
            bonus_ties = []
            if ties[0].initiative_bonus == ties[1].initiative_bonus:
                bonus_ties.append(ties[0])
                bonus_ties.append(ties[1])
            if len(ties) > 2:
                if (ties[0].initiative_bonus == ties[2].initiative_bonus):
                    if ties[0] not in bonus_ties:
                        bonus_ties.append(ties[0])
                    bonus_ties.append(ties[2])
                if (ties[1].initiative_bonus == ties[2].initiative_bonus):
                    if ties[1] not in bonus_ties:
                        bonus_ties.append(ties[1])
                    if ties[2] not in bonus_ties:
                        bonus_ties.append(ties[2])
            # for i in range(len(bonus_ties)):
            #     print(bonus_ties[i].name)
            if len(bonus_ties) > 1:
                # reorder bonus_ties according to tiebreaker rolls
                print('\t\tInitiative bonus tie!')
                print('\t\tRoll a d20 to break tie:')
                for i in range(len(bonus_ties)):
                    is_num = False
                    while is_num == False:
                        try:
                            bonus_ties[i].roll_off = int(input('\t\t' + bonus_ties[i].name + ': '))
                            is_num = True
                        except ValueError:
                            print('>>> Invalid input.')
                            print('>>> You must enter an integer.')
                for i in range(0, len(bonus_ties)-1):
                    for j in range(0, len(bonus_ties)-1-i):
                        if bonus_ties[j].roll_off < bonus_ties[j+1].roll_off:
                            bonus_ties[j], bonus_ties[j+1] = bonus_ties[j+1], bonus_ties[j]
                for i in range(len(bonus_ties)):
                    if order[i] in bonus_ties:
                        order[i] = bonus_ties[i]
            else:
                for i in range(0, len(ties)-1):
                    for j in range(0, len(ties)-1-i):
                        if ties[j].initiative_bonus < ties[j+1].initiative_bonus:
                            ties[j], ties[j+1] = ties[j+1], ties[j]
                for i in range(len(ties)):
                    order[i] = ties[i]

    # encounters with 4 or more combatants
    else:
        # index_dict is used to store the start and end indices of separate matching pairs of numbers
        # e.g. 17 16 16 12 11 11
        # index_dict = {1: 2, 4: 5, start: end}
        for i in range(len(order)):
            if i != 0 and i != len(order)-1:
                # write special case for when list size == 2 and 3
                if i == 1: # special case: beginning of list
                    if order[0].initiative == order[1].initiative:
                        start = 0
                    elif order[1].initiative == order[2].initiative:
                        start = 1
                    if (order[0].initiative == order[1].initiative) and (order[1].initiative != order[2].initiative):
                        end = 1
                elif i == len(order)-2: # special case: end of list
                    if order[len(order)-2].initiative == order[len(order)-1].initiative:
                        end = len(order)-1
                    elif order[len(order)-2].initiative == order[len(order)-3].initiative:
                        end = len(order)-2
                    if (order[len(order)-2].initiative == order[len(order)-1].initiative) and (order[len(order)-2].initiative != order[len(order)-3].initiative):
                        start = len(order)-2
                else: # anything in between
                    if (order[i].initiative == order[i+1].initiative) and (order[i].initiative != order[i-1].initiative):
                        start = i
                    if (order[i].initiative != order[i+1].initiative) and (order[i].initiative == order[i-1].initiative):
                        end = i
                # use this to detect initiative roll ties
                if start != end:
                    index_dict[start] = end

        # Each key, value pairing in the dictionary (index_dict) represents
        # the start and end positions of tied initiative rolls.
        # Now must sort ties within list (order) by initiative bonus
        ties = {}
        ties_hi_to_lo = []
        if len(index_dict) != 0:
            print('=====TIE DETECTED=====')
            print('Initiative roll tie!')
            for key, value in index_dict.items():

                print('\tTIEBREAKER between: ', end='')
                # Print combatants in this tiebreaker
                for i in range(key, value+1):
                    if i == value:
                        print(order[i].name)
                    else:
                        print(order[i].name + ', ', end='')

                pc_in_dict = False
                for i in range(key, value+1):
                    if order[i].pc == True:
                        pc_in_dict = True
                if pc_in_dict == True:
                    # Only need to print if pc is part of this tiebreaker
                    print('\tEnter initiative bonus to break tie:')

                for i in range(key, value+1):
                    if order[i].pc == True:
                        is_num = False
                        while is_num == False:
                            try:
                                order[i].initiative_bonus = int(input('\t' + order[i].name + ': '))
                                is_num = True
                            except ValueError:
                                print('>>> Invalid input.')
                                print('>>> You must enter an integer.')
                # Now that we have all initiatives bonuses
                # we can sort all ties according to them.
                order[key:value+1] = sorted(order[key:value+1], key=lambda x: x.initiative_bonus, reverse=True)
                # Will have to deal with initiative bonus ties
                ties.clear()
                for i in range(key, value+1):
                    for j in range(key, value+1):
                        if (order[i].initiative_bonus == order[j].initiative_bonus) and (i != j):
                            if order[i] not in ties:
                                # print('Adding to ties:', order[i].name)
                                ties[order[i]] = 0
                            if order[j] not in ties:
                                # print('Adding to ties:', order[j].name)
                                ties[order[j]] = 0
                # Resolve initiative bonus ties with a d20 roll off.
                # There will be no ties as a result of a roll off. If 2 or more
                # rolls are equal, they must be rerolled.
                if len(ties) != 0:
                    dict_len = 0
                    print('\tInitiative bonus tie!')
                    print('\t\tROLL OFF between: ')
                    print('\t\t', end='')
                    for k,v in ties.items():
                        if dict_len == len(ties)-1:
                            print(k.name)
                        else:
                            print(k.name + ', ', end='')
                        dict_len+=1

                    print('\t\tRoll a d20 to break tie:')
                    for k, v in ties.items():
                        is_num = False
                        while is_num == False:
                            try:
                                if k.pc == False:
                                    # An "issue" with this method is that
                                    # multiple enemies may roll the same number.
                                    # If real issue, revert to manual rolls for
                                    # the enemies.
                                    rand_num = randint(1,20)
                                    ties[k] = rand_num
                                    print('\t\t%s: %d' % (k.name, rand_num))
                                else:
                                    ties[k] = input('\t\t%s: ' % k.name)
                                is_num = True
                            except ValueError:
                                print('>>> Invalid input.')
                                print('>>> You must enter an integer.')
                        k.swap = True

                    # Correctly order combatants with same init bonuses based on their tiebreaker rolls.
                    # They are stored in correct order in ties_hi_to_lo.
                    # They should replace the existing order inside order.
                    while len(ties) != 0:
                        highest = 0
                        for k, v in ties.items():
                            if int(v) > highest:
                                highest = int(v)
                                next_to_add = k
                        ties_hi_to_lo.append(next_to_add)
                        del ties[next_to_add]

        # Move combatants in proper order from ties_hi_to_lo to order
        for x in range(len(order)):
            if order[x].swap == True:
                order[x].swap = False
                order[x] = ties_hi_to_lo[0]
                del ties_hi_to_lo[0]

    return order

# Ensure initiative entered for an ally combatant is an integer.
# Parameter: a single friendly combatant.
def get_initiative(ally):
    try:
        ally.initiative = int(input('Initiative: '))
        # ally.initiative = 12 # for testing
    except ValueError:
        print('>>> ' + ally.name + ' not added.')
        print('>>> You must enter an integer.')
        get_initiative(ally)

# Create instance of class Combatant. An ally in this case.
# Gather all necessary information for this combatant and append to array of combatants.
# Parameter: array of combatants
def create_ally(order):
    new_combatant = Combatant()
    new_combatant.name = input('Ally name: ')
    new_combatant.pc = True

    # For testing purposes!
    # global tester
    # tester+=1
    # new_combatant.name = 'tester' + str(tester)

    get_initiative(new_combatant)
    order.append(new_combatant)
    print(new_combatant.name + ' added!')

# Create instance of class Combatant. An enemy in this case.
# Gather all necessary information for this combatant and append to array of combatants.
# Initiative rolls are automatically generated using randint and added to initiative bonus.
# Parameters: array of combatants, name of combatant, initiative bonus.
def create_enemy(order, enemy_name, init_bonus):
    new_combatant = Combatant()
    new_combatant.name = enemy_name
    new_combatant.initiative_bonus = init_bonus
    # roll = randint(1,20)
    roll = 12 # for testing
    new_combatant.initiative = roll+init_bonus
    order.append(new_combatant)

# Control number of allies to be added.
# Parameter: list of combatants.
def set_ally_init(order):
    try:
        num_of_allies = int(input('Number of allies: '))
        for i in range(num_of_allies):
            create_ally(order)
    except ValueError:
        print('>>> You must enter an integer.')
        set_ally_init(order)

# Control number of one type of enemy to be added.
# Also, get name and initiative bonus of certain type of enemy.
# Appropriatly adds a number to the end of an enemies name when added to list for easier tracking.
# Parameter: list of combatants.
def set_enemy_init(order):
    name = input('Name an enemy: ')
    try:
        init_bonus = int(input('Initiative bonus: '))
        if name[len(name)-1] is 's':
            num_of_enemies = int(input('Number of %ses: ' % name))
        else:
            num_of_enemies = int(input('Number of %ss: ' % name))
        for i in range(num_of_enemies):
            if num_of_enemies is 1:
                enemy_name = name
            else:
                enemy_name = name + str(i+1)
            create_enemy(order, enemy_name, init_bonus)
            print(enemy_name + ' added.')
    except ValueError:
        print('>>> ' + name + ' not added.')
        print('>>> You must enter an integer.')
        set_enemy_init(order)

# Main function; gets the ball rolling.
# Checks if more enemies should be added.
# Sorts list of combatants in descending order according to initiative
def main():
    order = []
    print('=====ALLIES=====')
    set_ally_init(order)

    print('=====ENEMIES=====')
    while True:
        set_enemy_init(order)
        more_enemies = input('More enemies? (y/n): ')
        more_enemies = more_enemies.lower()
        if more_enemies == 'n' or more_enemies == 'no':
            break
    order.sort(key=lambda x: int(x.initiative), reverse=True)
    order = tie_checker(order)
    print('=====INITIATIVE ORDER=====')
    write_to_file(order)

if __name__ == "__main__":
   main()
