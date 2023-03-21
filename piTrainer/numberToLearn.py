from time import sleep
import random
import string

class numberToLearn():
    def __init__(self) -> None:
        pass

    def start(self,window,fileToLearn):
        modes={
            1:("pi.txt","Pi"),
            2:("euler.txt","e"),
            3:("sqrt2.txt","sqrt(2)"),
            4:("random.txt","Random"),
            5:("custom.txt","Custom (place custom.txt)")
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
        if filename == 'random.txt':
            with open(filename,'w') as f:
                lines=[]
                for d in range(10):#       
                    line="1"
                    blocks=[]
                    for n in range(10):
                        blocks.append("".join([random.choice(string.digits) for _ in range(10)]))
                    line=" ".join(blocks)
                    lines.append(line)
                f.write("\n".join(lines))
        #filename="euler.txt"
        
        return (True,filename)