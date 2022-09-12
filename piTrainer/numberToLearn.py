from time import sleep


class numberToLearn():
    def __init__(self) -> None:
        pass

    def start(self,window,fileToLearn):
        modes={
            1:("pi.txt","Pi"),
            2:("euler.txt","e"),
            3:("sqrt2.txt","sqrt(2)"),
            4:("other.txt","other lol")
        }
        yCordOfOpt=4
        window.addstr(yCordOfOpt,3,"Select Mode")
        for key in modes:
            text= str(key)+') '+modes.get(key)[1]
            yCordOfOpt +=1
            window.addstr(yCordOfOpt,3,text)
        
        a=''
        while not a.isdigit():
            a = window.getkey()
            if a=='q':
                return
        filename=modes.get(int(a))[0]
        
        #filename="euler.txt"
        return (True,filename)