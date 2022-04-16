class PiFileReader:
    def __init__(self) -> None:
        pass

    def has_numbers(self,inputString):
        return any(char.isdigit() for char in inputString)

    def readPifileToLines(self,filename):
        pifile = open(filename)
        lines=[]
        
        while True:
            # Get next line from file
            line = pifile.readline()
        # if line is empty
        # end of file is reached
            if not line:
                break
            if self.has_numbers(line) and "-" not in line and " " in line:
                cleanedLine = ''
                for c in line:
                    if c != ' ' and c.isdigit():
                        cleanedLine = cleanedLine+c
                #print("Line{}: {}".format(count, line.strip()))
                lines.append(cleanedLine)
        pifile.close()
        return lines