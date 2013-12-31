#
# Takes in a genetic sequence and outputs the amino acid sequence encoded
#

class seqData() :
    
    def __init__ (self, infile=None) :
        print "file: ", infile
        
        if infile :
            self.fasta = self.fastaDict()
            
            self.file = infile
            
            self.text = self.getText(infile)
            print self.text
            
            self.text = self.removeSpace(self.text)
            print self.text
            
            self.rna = self.dnaToRNA()
            print self.rna
            
            self.getFrames()
            
            
            
    def getFrames(self):
        self.frame1 = self.toFastaPos(0)
        self.frame2 = self.toFastaPos(1)
        self.frame3 = self.toFastaPos(2)
        
        self.frame4 = self.toFastaNeg(0)
        self.frame5 = self.toFastaNeg(1)
        self.frame6 = self.toFastaNeg(2)


        print(self.frame1)
        print(self.frame2)
        print(self.frame3)
        print(self.frame4)
        print(self.frame5)
        print(self.frame6)
        
    def getText(self, doc):
        
        f = open(doc)
        
        text = ''
        for line in f.readlines():
            text = text + line
        
        #text = f.readlines()[0]
        f.close()
        
        return text
    
    def removeSpace(self, txt):
        
        text = ''
        for c in txt:
            if c != " " and c != "\n":
                text = text + c
                
        return text
        
    
    
        
    def fastaDict(self):
        
        dict = { 'uuu': 'F', 'uuc': 'F', 'uua': 'L', 'uug': 'L',
                 'cuu': 'L', 'cuc': 'L', 'cua': 'L', 'cug': 'L',
                 'auu': 'I', 'auc': 'I', 'aua': 'I', 'aug': 'M',
                 'guu': 'V', 'guc': 'V', 'gua': 'V', 'gug': 'V',
                 'ucu': 'S', 'ucc': 'S', 'uca': 'S', 'ucg': 'S',
                 'ccu': 'P', 'ccc': 'P', 'cca': 'P', 'ccg': 'P',
                 'acu': 'T', 'acc': 'T', 'aca': 'T', 'acg': 'T',
                 'gcu': 'A', 'gcc': 'A', 'gca': 'A', 'gcg': 'A',
                 'uau': 'Y', 'uac': 'Y', 'uaa': '-', 'uag': '-',
                 'cau': 'H', 'cac': 'H', 'caa': 'Q', 'cag': 'Q',
                 'aau': 'N', 'aac': 'N', 'aaa': 'K', 'aag': 'K',
                 'gau': 'D', 'gac': 'D', 'gaa': 'E', 'gag': 'E',
                 'ugu': 'C', 'ugc': 'C', 'uga': '-', 'ugg': 'W',
                 'cgu': 'R', 'cgc': 'R', 'cga': 'R', 'cgg': 'R',
                 'agu': 'S', 'agc': 'S', 'aga': 'R', 'agg': 'R',
                 'ggu': 'G', 'ggc': 'G', 'gga': 'G', 'ggg': 'G'}
        
        return dict
    
    
    def dnaToRNA(self):
        out = ""
        
        for c in self.text:
            c = c.lower() # in case DNA input is capitalized
            
            if c == 't':
                c = 'u'
            out += c
                
        return out
    

    def toFastaPos(self, start):
        out = ""
        i = start
        while i < len(self.rna):
            codon = self.rna[i:i+3]
            if len(codon) == 3:
                #print codon[2]
                #print codon
                out += self.fasta[codon]
                #print out
            i += 3
        return out
    
    
    def toFastaNeg(self, start):
        out = ""
        i = len(self.rna) - start
        while i > 0:
            anticodon = self.rna[i-3:i]
            if len(anticodon) == 3:
                codon = anticodon[2] + anticodon[1] + anticodon[0]
                codon = self.compliment(codon)
                out += self.fasta[codon]
            i -= 3
        return out

    def compliment(self, codon):
        
        out = ""
        
        for c in codon:
            if c == 'a':
                out += 'u'
            elif c == 'u':
                out += 'a'
            elif c == 'g':
                out += 'c'
            elif c == 'c':
                out += 'g'
        
        return out
                

    def saveToFile(self):
        f = open('seqOut.txt', 'wb')
         
        f.write(self.text)
        f.write(" \n")
        f.write("FRAMES:\n ")
        f.write('frame1: ' + self.frame1 + ' \n')
        f.write('frame2: ' + self.frame2 + ' \n')
        f.write('frame3: ' + self.frame3 + ' \n')
        f.write('frame4: ' + self.frame4 + ' \n')
        f.write('frame5: ' + self.frame5 + ' \n')
        f.write('frame6: ' + self.frame6 + ' \n')
         
        self.text;
        f.close()
     
