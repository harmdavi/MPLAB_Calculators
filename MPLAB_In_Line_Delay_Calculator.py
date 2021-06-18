'''
David Harmon
5-24-21

this calculator is used for the purpose of allowing a user to enter in hardware
calculations into this program for MPLAB and have the calculator calculate
what registers should be used and the values to create the delay needed.
'''

'''
FUNCTIONS
'''

'''
this function takes an input from the user and rounds it to the nearest specified
value. This is used in MPLAB becuase all commands are at least 4 q states long
(see PIC16F883 PG 227 Each cycle = 4 qstates). This important to get precice
because in line delays are the most precice way to delay
'''
def To_The_Nearest(nearest,input):
    if str(input).find(".") != -1:
        input = (input // 1) + 1        #This lops off the decimal and adds one

    for number in range(1 , (nearest + 1)):
        result = input / nearest
        result_string = str(result)
        if (result_string.find(".0") + 2) == len(result_string):
            break
        input += 1
    return(input)

def Simple_Loop_Calculatons(Q_states):

    Add_Message("***SIMPLE LOOP RESULTS***")

    pre_nops = Q_states / 256
    #print("pre_nops = " + str(pre_nops))
    Add_Message(f'pre_nops = {pre_nops}')

    if pre_nops < 12:
        round_pre_nops = To_The_Nearest(12, pre_nops)
    else:
        round_pre_nops = To_The_Nearest(4, pre_nops)
    #print("round_pre_nops = " + str(round_pre_nops))
    Add_Message(f'round_pre_nops = {round_pre_nops}')

    nops = (round_pre_nops - 12) / 4
    #print("nops = " + str(nops))
    Add_Message(f'nops = {nops}')
    equasion_string.insert(3,str(nops))

    Counter_Value = (Q_states / round_pre_nops) // 1
    #print("Counter_Value = " + str(Counter_Value))
    Add_Message(f'Counter_Value = {Counter_Value}')
    equasion_string.insert(4,str(Counter_Value))

    simple_q_equasion =(((nops * 4) + 4 + 8) * Counter_Value - 4 + 4 + 4)
    Add_Message(f'simple_q_equasion = {simple_q_equasion}')
    final_equasion.insert(2,simple_q_equasion)

    Left_Over_Q = (Q_states - (((nops * 4) + 4 + 8) * Counter_Value - 4 + 4 + 4))
    Add_Message(f'Left_over_Q = {Left_Over_Q}')
    final_equasion.insert(3,Left_Over_Q)

    Left_Over_Nops = (Q_states - (((nops * 4) + 4 + 8) * Counter_Value - 4 + 4 + 4)) / 4
    Add_Message(f'Left_Over_Nops = {Left_Over_Nops}')
    equasion_string.insert(5,str(Left_Over_Nops))

    simple_result = [nops,Counter_Value,Left_Over_Nops]
    #print("simple_result = " + str(simple_result))
    Add_Message(f'simple_result = {simple_result}')

    #print("SIMPLE LOOP\n" + "\tMOVLW" + "\t\tD'" + str(simple_result[1]) + "'")
    #Add_instruction("SIMPLE LOOP\n" + "\tMOVLW" + "\t\tD'" + str(int(simple_result[1])) + "'")
    Add_instruction(f'SIMPLE LOOP\n\tMOVLW' + "\t\tD'" + str(int(simple_result[1])) +"'")

    #print(f'\tMOVWF\t\tCOUNTERX\n\tLOOPX')
    Add_instruction(f'\tMOVWF\t\tCOUNTERX\n\tLOOPX')

    for i in range(0,int(simple_result[0])):
        #print(f'\tNOP')
        Add_instruction(f'\tNOP')

    #print("\tDECFSZ\t\tCOUNTERX\n\tGOTO\t\tLOOPX")
    Add_instruction("\tDECFSZ\t\tCOUNTERX\n\tGOTO\t\tLOOPX")

    nop_counter = 0
    for i in range (0,int(simple_result[2])):
    #for i in range (0,int(Left_Over_Q)):
        #print(f'\tNOP')
        Add_instruction(f'\tNOP')

    #print("\tRETURN")
    Add_instruction("\tRETURN")

    Add_Message("***END SIMPLE LOOP RESULTS***")

    return simple_result

def Nested_Loop_Calculations(Q_states):

    Add_Message("***NESTED LOOP RESULTS***")

    pre_nops = Q_states / (256 * 256)
    #print("Nested_pre_nops = " + str(pre_nops))
    Add_Message("Nested_pre_nops = " + str(pre_nops))

    if pre_nops < 12:
        round_pre_nops = To_The_Nearest(12, pre_nops)
    else:
        round_pre_nops = To_The_Nearest(4, pre_nops)

    #print("Nested_round_pre_nops = " + str(round_pre_nops))
    Add_Message("Nested_round_pre_nops = " + str(round_pre_nops))

    nops = (round_pre_nops - 12) / 4
    #print("Nested_nops = " + str(nops))
    Add_Message("Nested_nops = " + str(nops))
    equasion_string.insert(1,str(nops))

    equasion_one = ((nops * 4 + 4 + 8 ) * 256 - 4 + 4 + 4 + 4 + 8)
    #print(f'one_nest_iteration = {equasion_one}')
    Add_Message(f'one_nest_iteration = {equasion_one}')

    how_many_iterations = (Q_states / equasion_one) // 1
    #print(f'how_many_iterations = {how_many_iterations}')
    Add_Message(f'how_many_iterations = {how_many_iterations}')
    equasion_string.insert(2,str(how_many_iterations))

    equasion_two = (((nops * 4 + 4 + 8 ) * 256 - 4 + 4 + 4 + 4 + 8) \
    * how_many_iterations - 4 + 4 + 4)
    final_equasion.insert(1,equasion_two)
    #print(f'equasion_two = {equasion_two}')
    Add_Message(f'equasion_two = {equasion_two}')

    left_over = Q_states - equasion_two
    #print(f'left_over = {left_over}')
    Add_Message(f'left_over = {left_over}')

    Add_instruction(f'NESTED lOOP\n\tMOVLW' +"\t\tD'" + \
    str(int(how_many_iterations)) + "'")

    Add_instruction(f'\tMOVWF\t\tCOUNTER(X+1)\nLOOP(X+1)\n\tMOVLW\t\t0X00 \
    \n\tMOVWF\t\tCOUNTERX\nLOOPX')

    for i in range(0,int(nops)):
        Add_instruction(f'\tNOP')

    Add_instruction(f'\tDECFSZ\t\tCOUNTERX,1\n\tGOTO\t\tLOOPX\n\tDECFSZ \
    COUNTER(X+1),1\n\tGOTO\t\tLOOP2')

    Add_Message("***END NESTED LOOP RESULTS***")

    Simple_Loop_Calculatons(left_over)




def Add_Message(Message_string):
    #info_list.insert(message_inc + 1, Message_string)
    info_list.append(Message_string)

def Add_instruction(Instruction_String):
    instruction_list.append(Instruction_String)


def Delay_Calc(Crystal_Frequency,Time_To_Wait):

    global message_inc
    message_inc = 0
    global info_list
    info_list = []
    global instruction_list
    instruction_list = []
    global final_equasion
    final_equasion = []
    global equasion_string
    equasion_string = []


    #print("crystal Frequency = " + str(Crystal_Frequency) + "MHz")
    info_list.insert(message_inc,f'Crystal Frequency = {Crystal_Frequency} MHz')
    #print("seconds to wait " + str(Time_To_Wait) + " Seconds")
    Add_Message(f'Seconds to Wait = {Time_To_Wait} Seconds')
    #info_list.insert((message_inc + 1), f'Seconds to Wait = {Time_To_Wait} Seconds')

    Crystal_Frequency = Crystal_Frequency * 1000000

    One_Q_State = 1 / Crystal_Frequency

    #print("One Q State = " + str(One_Q_State) + "seconds")
    Add_Message(f'One Q State = {One_Q_State} Seconds')

    Total_Q_States = Time_To_Wait / One_Q_State
    final_equasion.insert(0,Total_Q_States)
    equasion_string.insert(0,str(Total_Q_States))

    #print("Total Q States = " + str(Total_Q_States))
    Add_Message(f'Total Q States = {Total_Q_States}')

    #print("Total Q states / 256 = " + str((Total_Q_States / 256)))
    Add_Message(f'Total Q states / 256 = {(Total_Q_States / 256)}')
    #print("Total Q states / (256 * 256) = " + str(Total_Q_States / (256 * 256)))
    Add_Message(f'Total Q states / (256 * 256) = {Total_Q_States / (256 * 256)}')

    if (Total_Q_States / 256) < 256:
        #print("You need a simple loop")
        Add_Message(f'You need a simple loop')
        simple_result = Simple_Loop_Calculatons(Total_Q_States)
        #simple_result = Simple_Loop_Calculatons(28876)

    elif (Total_Q_States / (256 * 256)) < 256:
        #print("You need a nested loop")
        Add_Message(f'You need a nested loop')

        nested_result = Nested_Loop_Calculations(Total_Q_States)

    #END NESTED LOOP SUBROUTINE
    else:
        #print("This value is too large for the calculator")
        Add_Message(f'This value is too large for the calculator')
'''
END FUNCTIONS
'''
'''
BEGIN MAIN FUNTION OF CODE (USER INTERFACE)
'''
# Put the crystal frequency in MHz since it will be converted later
Crystal_Frequency = 3
#put the wait time in terms of seconds. This will not be converted to anything
#else later
Time_To_Wait = 0.40

Delay_Calc(Crystal_Frequency,Time_To_Wait)

for i in range(len(info_list)):
    print(info_list[i])

for i in range(len(instruction_list)):
    print(instruction_list[i])

print(f'{equasion_string[0]} - (((({equasion_string[1]} * 4 + 4 + 8) \
* 256 - 4 + 4 + 4 + 4 + 8) * {equasion_string[2]} - 4 + 4 + 4) + \
(({equasion_string[3]} * 4 + 4 + 8) * {equasion_string[4]} - 4 + 4 + 4) \
+ ({equasion_string[5]} * 4))')

final_equasion_result = final_equasion[0] - (final_equasion[1] + final_equasion[2] + final_equasion[3])

print(f'final_equasion_result = {final_equasion_result}')

'''
END MAIN FUNTION OF CODE (USER INTERFACE)
'''
