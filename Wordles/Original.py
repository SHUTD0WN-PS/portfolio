# Hello, this is my wordle.
# Of course, I couldn't do this by myself.
# I had to do research to find out how to get a random english word.
# And I also had some help from my friend, Kie Ren Siew. He is also applying for HCI DSA Infocomm.









import random
import time
import sys
from urllib.request import urlopen

idealans = ["Green", "Green", "Green", "Green", "Green"]
chancesleft = 6
foundans = False
notriesleft = False
youlost = False
word = ''

def splt(word):
    return [char for char in word]

def chanceleft():
    if(chancesleft != 0 and foundans != True):
        print("You have " + str(chancesleft) + " chances left.")
        print("")
    
def guess(ans, response):
    global chancesleft
    global foundans
    
    if(chancesleft != 0 and foundans != True and youlost == False):
        if(len(response) != 5 or response not in word):
            if(response == "quit"):
                foundans = True
                chancesleft = 0
                sys.exit()

            elif(response == "showans"):
                print(ranword)

            elif(response == "fritz" or response == "waqfs" or response == "vodht"):
                pass

            else:
                print("Enter 5 letters only, and make sure it is an ENGLISH word.")

        else:
            
            clues = [None, None, None, None, None]
    
            sa = splt(ans)
            #print(sa) # To delete later

            sr = splt(response)
            #print(sr) # To delete later

            # CHECKING
            x = 0
    
            while x < len(ranword):
                if sr[x] == sa[x]:
                    clues[x] = "Green"
                elif sr[x] in sa:
                    clues[x] = "Yellow"
                else:
                    clues[x] = "Black"
            
                x += 1

            if clues == idealans:
                print("Correct!")
                foundans = True
                chancesleft = 0
    
            chancesleft -= 1
            
            if(chancesleft < 0):
                chancesleft = 0
                
            return clues
    else:
        print("NOO YOU RAN OUT OF TRIES")
        notriesleft = True
        youlose = True

word_site = "http://www.instructables.com/files/orig/FLU/YE8L/H82UHPR8/FLUYE8LH82UHPR8.txt"
thing = urlopen(word_site)
txt = thing.read()
WORDS = txt.splitlines()
ranwordb = (random.choice(WORDS))

for x in WORDS:
    word += x.decode('utf-8')

while len(ranwordb) != 5:
    ranwordb = (random.choice(WORDS))

ranword = ranwordb.decode("UTF-8")

print("Type quit to quit.")

#print(ranword) # To delete later
while chancesleft != 0:
    if(foundans != True):
        print(guess(ranword, input("Take your wordle guess: ")))
        chanceleft()
    else:
        print("You either found the answer, or you quit.")
        break
    
while youlost != False:
    if(notriesleft):
        print("YOU RAN OUT OF TRIES")
        print("The word was " + ranword)

time.sleep(3)
