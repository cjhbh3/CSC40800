'''
Name: CJ Hess
Class: CSC 40800 - Organization of Programming Languages
Date: 4/2/2023
Homework 4
Answer 1

'''

# Constants
EOF = -1
INT_LIT = 10
IDENT = 11
ASSIGN_OP = 20
ADD_OP = 21
SUB_OP = 22
MULT_OP = 23
DIV_OP = 24
LEFT_PAREN = 25
RIGHT_PAREN = 26
SEMICOLON = 27

# Global Variables
charClass = 0
lexLen = 0
token = 0
nextToken = 0
lexeme = ""
nextChar = ''
in_fp = open(r"/home/FrontIn1.txt", "r")

# Character classes
LETTER = 0
DIGIT = 1
UNKNOWN = 99

def addChar():
    global lexeme
    global lexLen
    if lexLen <= 98:
        lexeme = lexeme + nextChar
        lexLen=+1
    else:
        print("Error - Lexeme is too long \n")

def getChar():
    global nextChar
    global charClass
    nextChar = in_fp.read(1)
    if nextChar:
        if nextChar.isalpha():
            charClass = LETTER
        elif nextChar.isdigit():
            charClass = DIGIT
        else:
            charClass = UNKNOWN
    else:
        charClass = EOF


def getNonBlank():
    global nextChar
    while nextChar.isspace():
        getChar()

def lex():
    global lexLen
    global nextToken
    global lexeme
    lexLen = 0
    lexeme = ""
    getNonBlank()
    if charClass == LETTER:
        addChar()
        getChar()
        while charClass == LETTER or charClass == DIGIT:
            addChar()
            getChar()
        nextToken = IDENT
    elif charClass == DIGIT:
        addChar()
        getChar()
        while charClass == DIGIT:
            addChar()
            getChar()
        nextToken = INT_LIT
    elif charClass == UNKNOWN:
        nextToken = lookup(nextChar)
        getChar()
    elif charClass == EOF:
        nextToken = EOF
        lexeme = "EOF"
    
    print("Next token is: " + str(nextToken) + ", Next lexeme is " + lexeme)
    return nextToken



def lookup(ch):
    if ch == '(':
        addChar()
        nextToken = LEFT_PAREN
    elif ch == ')':
        addChar()
        nextToken = RIGHT_PAREN
    elif ch == '+':
        addChar()
        nextToken = ADD_OP
    elif ch == '-':
        addChar()
        nextToken = SUB_OP
    elif ch == '*':
        addChar()
        nextToken = MULT_OP
    elif ch == '/':
        addChar()
        nextToken = DIV_OP
    elif ch == '=':
        addChar()
        nextToken = ASSIGN_OP
    elif ch == ';':
        addChar()
        nextToken = SEMICOLON
    else:
        addChar()
        nextToken = EOF
    
    return nextToken

def main():
    getChar()
    while nextToken != EOF:
        lex()
    in_fp.close()
    
    

if __name__ == "__main__":
    main()
