#
#Name: Noel Treese
#Student-ID: ntreese
#Date: 9/21/18
#
#Lab 0
#Section 14
#Purpose: Investigate command line prompts and modifying variables
#

def weight_on_planets():
   # write your code here
   given_weight = float(input('What do you weigh on earth? '))
   mars_weight = given_weight*0.38
   jupiter_weight = given_weight*2.34

   print('')
   print('On Mars you would weigh {} pounds.'.format(mars_weight))
   print('On Jupiter you would weigh {} pounds.'.format(jupiter_weight)) 
   
if __name__ == '__main__':
   weight_on_planets()
