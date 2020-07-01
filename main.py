import sys

print("Welcome to {name} CLI")
print("Press CRT + C Twice to exit @ anytime.")
while True:
    d1a = input ("Are you a: A) Member B) Admin [A/B]? : ")
    # check if d1a is equal to one of the strings, specified in the list
    if d1a in ['A', 'B']:
        # if it was equal - break from the while loop
        break
# process the input
if d1a == "A": 
    print ("Welcome to the Member Zone") 

# Member Zone CLI.


while True:
    d1a = input ("Do you need a: A) Help B) Login [A/B]? : ")
    # check if d1a is equal to one of the strings, specified in the list
    if d1a in ['A', 'B']:
        # if it was equal - break from the while loop
        break

if d1a == "A": 
    print("Ok, So you need help, What do you need help with?") 


# ASK

while True:
    d1a = input ("Do you need help with: A) The Website B) {b} [A/B]? : ")
    if d1a == "A":
        print ("{help for the website") & exit()
    elif d1a == "B":
        print ("Help for {B}") & exit()
    elif dia == "Q":
        break
exit()

# END ASK


if d1a == "B": 
    print("Login?") & exit()


# End Of Member Zone CLI

# ADMIN ZONE CLI

if d1a == "B": 
    print ("Welcome to the Admin Zone")
    import getpass
p = getpass.getpass(prompt='You Must Enter The Passcode to access the admin Center. ')
if p.lower() == 'passcode':
    print ('Right!!')
    print ("Updates: None!!")
else:
    print ('Sorry Incorrect Password..')



    
