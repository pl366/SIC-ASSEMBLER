# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 18:56:27 2017

@author: PULKIT LUTHRA
"""

assembly_code=[]
SYMTAB={}
OPTAB={
'ADD':'18',
'AND' :'40',
'COMP':'28',
'DIV':'24',
'J' :'3C',
'JEQ':'30',
'JGT':'34',
'JLT':'38',
'JSUB':'48',
'LDA':'00',
'LDCH':'50',
'LDL':'08',
'LDX':'04',
'MUL':'20',
'OR':'44',
'RD':'D8',
'RSUB':'4C',
'STA':'0C',
'STCH':'54',
'STL':'14',
'STSW':'E8',
'STX':'10',
'SUB' :'1C',
'TD':'E0',
'TIX':'2C',
'WD':'DC'}
with open("test1.txt") as f:
    for line in f:
        assembly_code.append(line)

first_line = assembly_code[0].strip().split()
args = len(first_line)

LOCCTR=0
if args==3:
    label, opcode, operand = first_line
    if (opcode == 'START'):
        program_name = label
        LOCCTR = int(operand)
print ("PROGRAM NAME->",program_name)
LOCCTR=int(str(LOCCTR),16)

# PASS 1
for i in range(1,len(assembly_code)):
    line = assembly_code[i].strip().split()
    args = len(line)
    if args==3:
        label,opcode,operand=line

        if label not in list(SYMTAB.keys()):
            SYMTAB[label]=format(int(LOCCTR),'04x')
        if opcode in list(OPTAB.keys()):
            LOCCTR+=3
        elif opcode=='WORD':
            LOCCTR+=3
        elif opcode=='RESW':
            LOCCTR+=(3*int(operand))
        elif opcode=='RESB':
            LOCCTR+=(int(operand))
        elif opcode=='BYTE':
            le=len(operand)-3
               
            if operand[0]=='X':
                if (le%2==0):
                    LOCCTR+=le/2
                else:
                    
                    LOCCTR +=((le/2)+1)
                    
            elif operand[0]=='C':
                LOCCTR+=(le)
               
    if args==2:
        opcode,operand=line
        if (opcode=='END'):
            break
        if opcode in list(OPTAB.keys()):
            LOCCTR+=3
        
    if args==1:               #RSUB   
        LOCCTR+=3
    
        
print("SYMTAB ->",SYMTAB)

# PASS2
object_code=[]
for i in range(1,len(assembly_code)):
    line = assembly_code[i].strip().split()
    
    args = len(line)
    
    if args==3:
        p=''
        label,opcode,operand=line
        if opcode in list(OPTAB.keys()):
            for key,value in OPTAB.items():
                if key==opcode:
                    p=value
            l=''        
            for key,value in SYMTAB.items():
                if key==operand:
                    l=value
                    break
                else:
                    l='0000'
            object_code.append(p+l)
            
        elif opcode=='WORD':
            object_code.append(format(int(operand),'06x'))
        elif opcode=='BYTE':
            
            arr=operand.split('\'')
            if arr[0]=="X":
                object_code.append(arr[1])
            elif arr[0]=="C":
                chars=list(arr[1])
                
                s=''
                for char in chars:
                    asciiCode = format(ord(char), "x")
                    
                    s=s+asciiCode
                object_code.append(s)
                
    if args==2:
        opcode,operand=line
        if opcode=='END':
            break
        p=''
        for key,value in OPTAB.items():
                if key==opcode:
                    p=value
        l=''
        op = operand.split(',')
        le = len(op)
        if(le==2 and op[1]=="X"):              #checking for indexed addresing
            
            
            for key,value in SYMTAB.items():
                if key==op[0]:
                    l=value
                   
            st=l
            
            p1 = st[:1]
            p2 = st[1:]
            
            p1 = int(p1)
            p1 = p1 + 8
            
            p1 = str(format(int(p1),'01x'))
            
            l = p1+p2
            
            object_code.append(p+l)
            
            
        else:
            l=''    
		 
            for key,value in SYMTAB.items():
                if key==operand:
                    l=value
                    break
                else:
                    l='0000'
            object_code.append(p+l)
    if args==1:
       opcode=line[0]
       if opcode=='RSUB':
           object_code.append('4C0000')
            
            
print ("MACHINE CODE ->",object_code)        
                    
                
                    
                    
                
               
                    
        
                
                
                
    		
				
				
				
				
				
				
									
			
			           
               
                    
					           
				
				  
            
            
            
            
            
                    
                    
                    
                    
                    
        
        
    
                
            
        
        
            
             
            
        
        
            
        
        
    
    
            