#Copyright 2021 Pedro Bereilh Licensed under the Apache License, Version 2.0 
#(the "License"); you may not use this file except in compliance with the License. 
#You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless 
#required by applicable law or agreed to inwriting, software distributed under the License 
#is distributed on an "AS IS" BASIS,WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either 
#express or implied. See the License for the specific language governing permissions 
#and limitations under the License.

from random import * 

dice = randint (1,6)
print "First dice: %s" % (dice)
dice1 = randint(1,6)
print "Second dice: %s" % (dice1)

sumdices = dice + dice1

if sumdices == 7 or sumdices == 11:
  print "You won"
elif sumdices == 2 or sumdices == 3 or sumdices == 12:
  print "You lose"
else:
  print "You rolled a " + str(sumdices) + " Roll again"

#Run code python dice.py