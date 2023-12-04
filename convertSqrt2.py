
def main(input, output):
    with open(input, "r") as pifile:
        lines = []
        line = pifile.read().replace("\n", "")
        #line=lines[0][3:103]
        #print(line[3:103])
        print(len(line))
        for i in range(int(len(line)/100)+1):
            lines.append(line[2+((i-1)*100):2+i*100])
        lines.append(line[-1*(len(line)%100)+2:])
        lines.pop(0)
        with open(output, "w+") as outputfile:
            for l in lines:
                t=''
                for i in range(len(l)):
                    if i%10==0:
                        t=t+' '
                    t=t+l[i]
                        
                outputfile.write(t+"\n")






if __name__== '__main__':
    main("sqrt22.txt","sqrt2.txt")