def main():

  selection = input("Which tutorial would you like to run?\n\n[1] Window\n[2] Boat\n[3] Movement\n[4] Full game\n\nEnter selection: ")

  if selection == "1":
    import tut1_window
    tut1_window.play()
  elif selection == "2":
    import tut2_boat
    tut2_boat.play()
  elif selection == "3":
    import tut3_movement
    tut3_movement.play()
  elif selection == "4":
    import tut4_mechanics
    tut4_mechanics.play()
  else:
    print("Invalid input. Run program again.")

if __name__ == '__main__':
  main()