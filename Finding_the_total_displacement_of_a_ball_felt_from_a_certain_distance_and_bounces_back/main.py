while True:
    try:
            x:int = int(input("Enter the distance from which the ball is felt:--->> "))
            a:int = int(input("Enter the percentage the ball bounces back to the privious hight:--->> "))
            break
    except ValueError:
            print("Please enter a valid integer")
            continue


total_displacement = (100+a)*x/(100-a)
print(f"The total displacement of the ball is:--->> {total_displacement}")
