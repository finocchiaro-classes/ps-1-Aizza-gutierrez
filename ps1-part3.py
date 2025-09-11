# function that is a target heart rate calculator 
def heart_rate(age, goal):

  # calculate max heart rate 
    max_HR = 220 - age 
    print(f' Your maximum age heart rate is: {max_HR}')
  # determine target heart range 
  if goal == 'S':
    low = max_HR * 0.80
    high = max_HR * 1.00
  elif goal == 'E':
    low = max_HR * 0.60
    high = max_HR * 0.60
  else: 
    # in case invalid input is given
    print(f'Invalid goal entered.')
    return 
  print('Your target heart rate is between {low} and {high}')

# main program
user_age = int(input("What is your age?") )
user_goal = input("Is your goal speed {S{ or endurance {E}")

heart_rate(user_age, user_goal) 
