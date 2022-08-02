"""wap to function a elevator.
1.ask user to input the floor number where they want to go and assign it to the variable destination.
2.declare  a variable named current floor and assign it with the value 0.
   0=ground floor
   1=first floor 
   2= second floor
   3=third floor.
3. current floor has a value 0,ie, you are on the ground floor
4.if you press 1 it will takeyou to the first floor, hence the current floor will get changed to 1
   
"""


import winsound
destination=int(input("enter the floor you want to go "))

currentfloor=0#(you are on the ground floor )
while destination!="out":
  if currentfloor==0 :#(when the lift is on the ground floor)
    if destination==1:#(destination is firstfloor)
        print(0)
        print("\n\n")
        print(1)
        winsound.Beep(440,500)
        winsound.Beep(440,500)
        winsound.Beep(440,500)
        print("you are on the first floor")
        currentfloor=destination# once you reached the first floor first floor will be the currenbt floor
        destination=int(input("enter the floor you want  to go "))

    elif destination==2:
        print(0)
        print("\n\n")
        print(1)
        print("\n\n")
        print(2)
        winsound.Beep(440,500)
        winsound.Beep(440,500)
        winsound.Beep(440,500)
        print("you are on the second floor")
        currentfloor=destination
        destination=int(input("enter the floor you want  to go "))
    elif destination==3:  
        print(0)
        print("\n\n")
        print(1)
        print("\n\n")
        print(2)
        print("\n\n")
        print(3)
        winsound.Beep(440,500)
        winsound.Beep(440,500)
        winsound.Beep(440,500)
        print("you are on the third floor")
        currentfloor=destination
        destination=int(input("enter the floor you want  to go "))
    else:
        winsound.Beep(440,500)
        winsound.Beep(440,500)
        winsound.Beep(440,500)
        destination=int(input("enter the floor you want  to go "))

  elif currentfloor==1:
     if destination==0:
        print(1)
        print("\n\n")
        print(0)
        winsound.Beep(440,500)
        winsound.Beep(440,500)
        winsound.Beep(440,500)
        print("you are on the first floor")
        currentfloor=destination
        destination=int(input("enter the floor you want  to go "))
     elif destination==2:
        print(1)
        print("\n\n")
        print(2)
        print("\n\n")
        winsound.Beep(440,500)
        winsound.Beep(440,500)
        winsound.Beep(440,500)
        print("you are on the second floor")
        currentfloor=destination
        destination=int(input("enter the floor you want  to go "))
     elif destination==3:  
        print(1)
        print("\n\n")
        print(2)
        print("\n\n")
        print(3)
        print("\n\n")
        winsound.Beep(440,500)
        winsound.Beep(440,500)
        winsound.Beep(440,500)
        print("you are on the third floor")
        currentfloor=destination
        destination=int(input("enter the floor you want  to go "))
     else:
        winsound.Beep(440,500)
        winsound.Beep(440,500)
        winsound.Beep(440,500)
        destination=int(input("enter the floor you want  to go "))


  elif currentfloor==2:
     if destination==0:
        print(2)
        print("\n\n")
        print(1)
        print("\n\n")
        print(0)
        winsound.Beep(440,500)
        winsound.Beep(440,500)
        winsound.Beep(440,500)
        print("you are on the first floor")
        currentfloor=destination
        destination=int(input("enter the floor you want  to go "))
     elif destination==1:
        print(2)
        print("\n\n")
        print(1)
        print("\n\n")
        winsound.Beep(440,500)
        winsound.Beep(440,500)
        winsound.Beep(440,500)
        print("you are on the second floor")
        currentfloor=destination
        destination=int(input("enter the floor you want  to go "))
     elif destination==3:  
        print(2)
        print("\n\n")
        print(3)
        print("\n\n")
        winsound.Beep(440,500)
        winsound.Beep(440,500)
        winsound.Beep(440,500)
        print("you are on the third floor")
        currentfloor=destination
        destination=int(input("enter the floor you want  to go "))
     else:
        winsound.Beep(440,500)
        winsound.Beep(440,500)
        winsound.Beep(440,500)
        destination=int(input("enter the floor you want  to go "))
  elif currentfloor==3:
     if destination==1:
        print(3)
        print("\n\n")
        print(2)
        print("\n\n")
        print(1)
        winsound.Beep(440,500)
        winsound.Beep(440,500)
        winsound.Beep(440,500)
        print("you are on the first floor")
        currentfloor=destination
        destination=int(input("enter the floor you want  to go "))
     elif destination==2:
        print(3)
        print("\n\n")
        print(2)
        print("\n\n")
        winsound.Beep(440,500)
        winsound.Beep(440,500)
        winsound.Beep(440,500)
        print("you are on the second floor")
        currentfloor=destination
        destination=int(input("enter the floor you want  to go "))
     elif destination==0:  
        print(3)
        print("\n\n")
        print(2)
        print("\n\n")
        print(1)
        print("\n\n")
        print(0)
        winsound.Beep(440,500)
        winsound.Beep(440,500)
        winsound.Beep(440,500)
        print("you are on the ground  floor")
        currentfloor=destination
        destination=int(input("enter the floor you want  to go "))
     else:   
        winsound.Beep(440,500)
        winsound.Beep(440,500)
        winsound.Beep(440,500)  
        destination=int(input("enter the floor you want  to go "))