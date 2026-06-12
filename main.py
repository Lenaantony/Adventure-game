def argentina_path():
    pass
def brazil_path():
    pass
def portugal_path():
    pass
def intro():
    print("#### WELCOME TO WORLD CUP SEARCHING ADVENTURE GAME ####")
    player_name=input("Enter player name:")
    print("Countries\n1:Argentina\n2:Brazil\n3Portugal")
    country=input("Enter your country(number):")
    while True:
        if country==1:
            argentina_path()
        elif country==2:
            brazil_path()
        elif country==3:
            portugal_path()
        else:
            print("Invalid country")
            break
