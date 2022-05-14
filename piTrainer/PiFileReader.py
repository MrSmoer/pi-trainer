class PiFileReader:
    def __init__(self, filename) -> None:
        with open(filename) as pifile:
            self.lines=[]
            
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
                    self.lines.append(cleanedLine)

        #return self.lines

    def has_numbers(self,inputString):
        return any(char.isdigit() for char in inputString)

    def getDigit(self, n):
        linelength=len(self.lines[0])
        lineNum=self.getLineOfDigit(n)
        return self.lines[lineNum][self.getDigitOfLine(n)]

    def getLineOfDigit(self, n):
        linelength=len(self.lines[0])
        lineNum=int(n/linelength)
        return lineNum
    def getDigitOfLine(self, n):
        linelength=len(self.lines[0])
        return n%linelength
