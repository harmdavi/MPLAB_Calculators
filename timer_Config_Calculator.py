'''
David Harmon
6-18-21

This calculator is for the use of aiding in the configuration of a PIC16F883's
timer prescale and postscale values. This will allow for the user to calculate
a prescale and postscale value that will be a round value with refference to
seconds.
'''

global Lowest_Answer
Lowest_Answer = 300.00

Crystal_Frequency = 4  #this will be in MHz

Time_To_Interrupt =  0.02   #this will be in terms of seconds



Clock_Time = 1 / ((Crystal_Frequency * 1000000) / 4)

Max_Interrupt_TimePPPRCV = Clock_Time * 255 * 16 * 16 * 255
'''
PPPRCV stands for Prescale Postscale PRx Counter Value. This is if the user
were to use a counter inside of the interrupt to add to the scaling time
even though it is not something that is accounted for in the setup operations
of the chip.
'''

Max_Interrupt_TimePPPR = Clock_Time * 255 * 16 * 16

'''
This value is the same as before but does not include the incremented COUNTER
that would need to be coded into the interrupt in software. this value purely
shows what the setup is going to do
'''
'''
print(Clock_Time)
print(Max_Interrupt_TimePPPRCV)
print(Max_Interrupt_TimePPPR)

print(bin(hex(5555))
'''
result_increment = int(0)
'''
possibilities = [
[0,1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],
[0,1,2,3]
]
'''
possibilities = [
[0,1,2,3],
[0,1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
]



for register in range(1,256):
    for postscaler in range(1,16):
        for PR2 in range(1,255):
            for prescaler in range(1,3):

                if prescaler == 1:
                    result = 1 * register * postscaler * PR2 * prescaler * Clock_Time
                elif prescaler == 2:
                    result = 4 * register * postscaler * PR2 * prescaler * Clock_Time
                elif prescaler == 3:
                    result = 16 * register * postscaler * PR2 * prescaler * Clock_Time
                else:
                    print("Something went wrong in the prescaler loop")

                    if (Time_To_Interrupt - result) < Lowest_Answer:
                        Lowest_Answer = input
                        Closest_Values [0] =  prescaler
                        Closest_Values [1] =  postscaler
                        Closest_Values [2] =  PR2
                        Closest_Values [3] =  register
                        Closest_Values [0] =  result

                if result == Time_To_Interrupt:
                    print("********************")
                    print(f'Register value = {register}')
                    print(f'Postscaler value = {postscaler}')
                    print(f'Prescaler value = {prescaler}')
                    print(f'PR2 value = {PR2}')
                    print(f'Clock Time value = {Clock_Time}')
                    print(f'Result = {result}')
                    print("********************")



print(f'Max time with just setup = {Max_Interrupt_TimePPPR}')
print(f'Max time with setup and register maxed out = {Max_Interrupt_TimePPPRCV}')
