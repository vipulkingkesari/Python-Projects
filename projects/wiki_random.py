import wikipedia,webbrowser


def getpage():
    wikipage=wikipedia.random(1)
    wikiload=wikipedia.page(wikipage)

    userchoice = input("Would you like to read about {} (Y/N/Q):".format(wikipage)).lower().strip()

    if(userchoice=="Y" or userchoice=="yes"):
        print("\n summary:\n-------------\n")
        print(wikiload.summary)
        wikiopen=input("\nOpen wiki page in browser ?(Y/N):").lower().strip()
        if(wikiopen=="yes" or wikiopen =="y"):
            webbrowser.open(wikiload.url,new=2)
        else:
            getpage()
        exit(0)

    elif(userchoice=="q" or userchoice=="quit"):
        exit(0)
    else:
        getpage()


if __name__ == "__main__":
    getpage()