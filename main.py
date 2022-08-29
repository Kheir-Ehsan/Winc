# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

from gettext import find


scorer_name1 = 'Ruud Gullit'
scorer_name2 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54
# str () - converts to string
# int () - converts to integer
# eg. print (scorer_name1 +' scored the first goal in ' + str (goal_0) + " minutes")
scorers = scorer_name1 + ' ' + str (goal_0) + ", " + scorer_name2 + ' ' + str (goal_1)
report = scorer_name1 + ' scored in the ' + str(goal_0) +'nd' + ' minute' + ' ' + scorer_name2 + ' scored in the ' + str(goal_1) +'th' + ' minute'


last_name = 'Koeman' 
player = 'RonaldKoeman'
first_name = player[0:6] # slice and store first name. Here we isolate letter 0 to 6 tot get the first name
last_name_len = len(last_name) # Here we store the length of the var. last_name
name_short = first_name[0] +". " + last_name
chant = first_name + "!" + ' '
print (chant * len(first_name))
