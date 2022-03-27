# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
from distutils.command.build_scripts import first_line_re
from gettext import find


scorer_0 = "Ruud Gullit"
scorer_1 = "Marco van Basten"
goal_0 = 32
goal_1 = 54
scores = scorer_0 + str(goal_0), scorer_1 + str(goal_1)
print(scores)
scorers = scorer_0 + " " + str(goal_0) + " ," + scorer_1 + " " + str(goal_1)
print(scorers)
scorers = scorer_0 + " " + str(goal_0) + ", " + scorer_1 + " " + str(goal_1)
print(scorers)
scorers_del = scorer_0 + " " + str(goal_0), scorer_1 + " " + str(goal_1) # comma's veroorzaken blijkbaar haakjes en single qoutes???
print(scorers_del)
print(scorers)
scorers = f"{scorer_0} {goal_0}, {scorer_1} {goal_1}" 
print(scorers)
report = f"{scorer_0} scored in the {goal_0}nd minute\n{scorer_1} scored in the {goal_1}th minute" 
print(report)
name1="Frank"
k = name1.find("k")
print(k)
name1[0:5:2]
print(name1[0:5:2])
print(len(name1))
player = "Frank Rijkaard"
first_name = player[:player.find(" Rijkaard")]
print(first_name)
# einde opdracht first name
first_name_del = player.find("R")
print(player[player.find("R"):len(player)])
# einde last name
last_name_len = len("Rijkaard")
print(last_name_len)
# einde last name len
name_short = "F. Rijkaard"
chant = (" Frank!")*5
print(chant)
chant = ("Frank! ")*4 + ("Frank!")
print(chant)
# end chant
good_chant = ("Frank! ")*5 != chant
print(good_chant)
