import random
import json 

def gradecheck():
    total = 0
    for grade in seznamzaku[name]:
        total += grade
        
    avg = total/(len(seznamzaku[name]))
    if avg < 2:
        print(f"zak {name} ma prumer {avg}. ucitel je stestny")
    if avg > 2 and avg <4:
            print(f"zak {name} ma prumer {avg}. ucitel je spokojeny")
    else:
        print(f"zak {name} ma prumer {avg}. ucitel je smutny af")
        
def writetodb():
    y = json.dumps(seznamzaku)
    with open("seznam.json", "w") as f:
        f.write(y)


while True:
    with open("seznam.json") as f:
        seznamzaku = json.load(f)
    naseznamu = False

    
    username = input("input your username ")
    if username == "admin":
        admin = True
    else:
        admin = False
        
    name = input("jmeno studenta: ")

    for jmeno in seznamzaku:
        if jmeno == name:
            naseznamu = True
        
    if naseznamu == True:
        gradecheck()

        if admin == True:
            answ = input("do you want to add them another grade? write number or no")
            if input == "no":
                pass
            else:
                seznamzaku[name].append(int(answ))
                gradecheck()
                writetodb()
            

    elif admin == True:
        nameadd = input("tento zak neexistuje. chcete ho pridat? Y/N ")

        if nameadd == "Y":
            newname = input("napiste jmeno zaka ")
            newgrade = input("napiste znamku zaka ")
            seznamzaku[newname] = newgrade
            writetodb()
            

