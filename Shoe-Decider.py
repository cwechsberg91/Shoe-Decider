print("Hello there, welcome to the Shoe Decider. What is your name?")
MyName = input()
print ("Nice to meet you " + MyName)
print ("Will it be Hot or Cold?")

answer = input()
if answer is 'Hot':
    print("Nice. You should wear Sneakers or Sandals!")
elif answer != 'Cold':
    print ("Okay. You should wear Sneakers or Boots.")
while answer != 'Hot':
    print ("Okay. You should wear Sneakers or Boots.")
    break

print ("Are you wearing Dark or Light clothing?")

color = input()
if answer is 'Dark':
    print("Nice. Your shoes should be Black or Brown!")
elif answer != 'Light':
    print ("Okay. Your shoes should be white!")
