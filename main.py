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
#scorers = scorer_name1 + ' ' + str(goal_0) + ", " + scorer_name2 + ' ' + str(goal_1)
scorers = f'{scorer_name1} {goal_0}, {scorer_name2} {goal_1}'
report = f'{scorer_name1} scored in the {goal_0}nd minute\n{scorer_name2} scored in the {goal_1}th minute'
#report = scorer_name1 + ' scored in the ' + str(goal_0)+'nd' + ' minute' + ' ' + scorer_name2 + \
' scored in the ' + str(goal_1)+'th' + ' minute'
print(report)

player= 'Ronald Koeman'
x = player.find(' ')
first_name = player[:x]
#first_name = player[:player.find(" ")]
print(first_name)
last_name = player[-x:]
#last_name = player[player.find(" "):]
print (last_name)
last_name_len = len(player[-x:])
print (last_name_len)
name_short = first_name[0] +". " + last_name
chant = len(first_name) * (first_name + "! ")
chant = chant.rstrip ( )
good_chant = chant[-1] != " "
print (chant)
