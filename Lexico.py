# Generated from .\Lexico.g4 by ANTLR 4.13.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,40,246,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,3,1,3,
        1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,
        1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,9,1,9,1,9,1,9,
        1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,
        1,12,1,12,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,15,1,15,
        1,15,1,15,1,15,1,15,1,16,1,16,1,17,1,17,1,18,1,18,1,19,1,19,1,20,
        1,20,1,21,1,21,1,22,1,22,1,23,1,23,1,24,1,24,1,25,1,25,1,26,1,26,
        1,27,1,27,1,28,1,28,1,29,1,29,1,30,1,30,1,30,1,31,1,31,1,31,1,32,
        1,32,1,32,1,33,1,33,1,33,1,34,1,34,1,35,1,35,5,35,202,8,35,10,35,
        12,35,205,9,35,1,36,1,36,5,36,209,8,36,10,36,12,36,212,9,36,1,36,
        1,36,1,37,4,37,217,8,37,11,37,12,37,218,1,37,1,37,4,37,223,8,37,
        11,37,12,37,224,3,37,227,8,37,1,38,1,38,1,38,1,38,5,38,233,8,38,
        10,38,12,38,236,9,38,1,38,1,38,1,39,4,39,241,8,39,11,39,12,39,242,
        1,39,1,39,0,0,40,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,
        11,23,12,25,13,27,14,29,15,31,16,33,17,35,18,37,19,39,20,41,21,43,
        22,45,23,47,24,49,25,51,26,53,27,55,28,57,29,59,30,61,31,63,32,65,
        33,67,34,69,35,71,36,73,37,75,38,77,39,79,40,1,0,6,3,0,65,90,95,
        95,97,122,4,0,48,57,65,90,95,95,97,122,2,0,34,34,92,92,1,0,48,57,
        2,0,10,10,13,13,3,0,9,10,13,13,32,32,252,0,1,1,0,0,0,0,3,1,0,0,0,
        0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,
        15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,
        25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,
        35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,
        45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,
        55,1,0,0,0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,0,0,0,
        65,1,0,0,0,0,67,1,0,0,0,0,69,1,0,0,0,0,71,1,0,0,0,0,73,1,0,0,0,0,
        75,1,0,0,0,0,77,1,0,0,0,0,79,1,0,0,0,1,81,1,0,0,0,3,85,1,0,0,0,5,
        89,1,0,0,0,7,93,1,0,0,0,9,96,1,0,0,0,11,101,1,0,0,0,13,107,1,0,0,
        0,15,113,1,0,0,0,17,120,1,0,0,0,19,123,1,0,0,0,21,127,1,0,0,0,23,
        131,1,0,0,0,25,136,1,0,0,0,27,142,1,0,0,0,29,146,1,0,0,0,31,151,
        1,0,0,0,33,157,1,0,0,0,35,159,1,0,0,0,37,161,1,0,0,0,39,163,1,0,
        0,0,41,165,1,0,0,0,43,167,1,0,0,0,45,169,1,0,0,0,47,171,1,0,0,0,
        49,173,1,0,0,0,51,175,1,0,0,0,53,177,1,0,0,0,55,179,1,0,0,0,57,181,
        1,0,0,0,59,183,1,0,0,0,61,185,1,0,0,0,63,188,1,0,0,0,65,191,1,0,
        0,0,67,194,1,0,0,0,69,197,1,0,0,0,71,199,1,0,0,0,73,206,1,0,0,0,
        75,216,1,0,0,0,77,228,1,0,0,0,79,240,1,0,0,0,81,82,5,118,0,0,82,
        83,5,97,0,0,83,84,5,114,0,0,84,2,1,0,0,0,85,86,5,102,0,0,86,87,5,
        117,0,0,87,88,5,110,0,0,88,4,1,0,0,0,89,90,5,102,0,0,90,91,5,111,
        0,0,91,92,5,114,0,0,92,6,1,0,0,0,93,94,5,105,0,0,94,95,5,102,0,0,
        95,8,1,0,0,0,96,97,5,101,0,0,97,98,5,108,0,0,98,99,5,115,0,0,99,
        100,5,101,0,0,100,10,1,0,0,0,101,102,5,119,0,0,102,103,5,104,0,0,
        103,104,5,105,0,0,104,105,5,108,0,0,105,106,5,101,0,0,106,12,1,0,
        0,0,107,108,5,112,0,0,108,109,5,114,0,0,109,110,5,105,0,0,110,111,
        5,110,0,0,111,112,5,116,0,0,112,14,1,0,0,0,113,114,5,114,0,0,114,
        115,5,101,0,0,115,116,5,116,0,0,116,117,5,117,0,0,117,118,5,114,
        0,0,118,119,5,110,0,0,119,16,1,0,0,0,120,121,5,111,0,0,121,122,5,
        114,0,0,122,18,1,0,0,0,123,124,5,97,0,0,124,125,5,110,0,0,125,126,
        5,100,0,0,126,20,1,0,0,0,127,128,5,110,0,0,128,129,5,111,0,0,129,
        130,5,116,0,0,130,22,1,0,0,0,131,132,5,116,0,0,132,133,5,114,0,0,
        133,134,5,117,0,0,134,135,5,101,0,0,135,24,1,0,0,0,136,137,5,102,
        0,0,137,138,5,97,0,0,138,139,5,108,0,0,139,140,5,115,0,0,140,141,
        5,101,0,0,141,26,1,0,0,0,142,143,5,110,0,0,143,144,5,105,0,0,144,
        145,5,108,0,0,145,28,1,0,0,0,146,147,5,116,0,0,147,148,5,104,0,0,
        148,149,5,105,0,0,149,150,5,115,0,0,150,30,1,0,0,0,151,152,5,115,
        0,0,152,153,5,117,0,0,153,154,5,112,0,0,154,155,5,101,0,0,155,156,
        5,114,0,0,156,32,1,0,0,0,157,158,5,40,0,0,158,34,1,0,0,0,159,160,
        5,41,0,0,160,36,1,0,0,0,161,162,5,123,0,0,162,38,1,0,0,0,163,164,
        5,125,0,0,164,40,1,0,0,0,165,166,5,44,0,0,166,42,1,0,0,0,167,168,
        5,46,0,0,168,44,1,0,0,0,169,170,5,45,0,0,170,46,1,0,0,0,171,172,
        5,43,0,0,172,48,1,0,0,0,173,174,5,59,0,0,174,50,1,0,0,0,175,176,
        5,47,0,0,176,52,1,0,0,0,177,178,5,42,0,0,178,54,1,0,0,0,179,180,
        5,37,0,0,180,56,1,0,0,0,181,182,5,60,0,0,182,58,1,0,0,0,183,184,
        5,62,0,0,184,60,1,0,0,0,185,186,5,61,0,0,186,187,5,61,0,0,187,62,
        1,0,0,0,188,189,5,33,0,0,189,190,5,61,0,0,190,64,1,0,0,0,191,192,
        5,60,0,0,192,193,5,61,0,0,193,66,1,0,0,0,194,195,5,62,0,0,195,196,
        5,61,0,0,196,68,1,0,0,0,197,198,5,61,0,0,198,70,1,0,0,0,199,203,
        7,0,0,0,200,202,7,1,0,0,201,200,1,0,0,0,202,205,1,0,0,0,203,201,
        1,0,0,0,203,204,1,0,0,0,204,72,1,0,0,0,205,203,1,0,0,0,206,210,5,
        34,0,0,207,209,8,2,0,0,208,207,1,0,0,0,209,212,1,0,0,0,210,208,1,
        0,0,0,210,211,1,0,0,0,211,213,1,0,0,0,212,210,1,0,0,0,213,214,5,
        34,0,0,214,74,1,0,0,0,215,217,7,3,0,0,216,215,1,0,0,0,217,218,1,
        0,0,0,218,216,1,0,0,0,218,219,1,0,0,0,219,226,1,0,0,0,220,222,5,
        46,0,0,221,223,7,3,0,0,222,221,1,0,0,0,223,224,1,0,0,0,224,222,1,
        0,0,0,224,225,1,0,0,0,225,227,1,0,0,0,226,220,1,0,0,0,226,227,1,
        0,0,0,227,76,1,0,0,0,228,229,5,47,0,0,229,230,5,47,0,0,230,234,1,
        0,0,0,231,233,8,4,0,0,232,231,1,0,0,0,233,236,1,0,0,0,234,232,1,
        0,0,0,234,235,1,0,0,0,235,237,1,0,0,0,236,234,1,0,0,0,237,238,6,
        38,0,0,238,78,1,0,0,0,239,241,7,5,0,0,240,239,1,0,0,0,241,242,1,
        0,0,0,242,240,1,0,0,0,242,243,1,0,0,0,243,244,1,0,0,0,244,245,6,
        39,0,0,245,80,1,0,0,0,8,0,203,210,218,224,226,234,242,1,6,0,0
    ]

class Lexico(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    VAR = 1
    FUN = 2
    FOR = 3
    IF = 4
    ELSE = 5
    WHILE = 6
    PRINT = 7
    RETURN = 8
    OR = 9
    AND = 10
    NOT = 11
    TRUE = 12
    FALSE = 13
    NIL = 14
    THIS = 15
    SUPER = 16
    OPEN_PAREN = 17
    CLOSE_PAREN = 18
    OPEN_BRACE = 19
    CLOSE_BRACE = 20
    COMMA = 21
    DOT = 22
    MINUS = 23
    PLUS = 24
    SEMICOLON = 25
    SLASH = 26
    MULTIPLY = 27
    MODULO = 28
    LESS_THAN = 29
    GREATER_THAN = 30
    EQUAL = 31
    NOT_EQUAL = 32
    LESS_EQUAL = 33
    GREATER_EQUAL = 34
    ASSIGN = 35
    IDENTIFIER = 36
    STRING = 37
    NUMBER = 38
    COMMENT = 39
    WHITESPACE = 40

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'var'", "'fun'", "'for'", "'if'", "'else'", "'while'", "'print'", 
            "'return'", "'or'", "'and'", "'not'", "'true'", "'false'", "'nil'", 
            "'this'", "'super'", "'('", "')'", "'{'", "'}'", "','", "'.'", 
            "'-'", "'+'", "';'", "'/'", "'*'", "'%'", "'<'", "'>'", "'=='", 
            "'!='", "'<='", "'>='", "'='" ]

    symbolicNames = [ "<INVALID>",
            "VAR", "FUN", "FOR", "IF", "ELSE", "WHILE", "PRINT", "RETURN", 
            "OR", "AND", "NOT", "TRUE", "FALSE", "NIL", "THIS", "SUPER", 
            "OPEN_PAREN", "CLOSE_PAREN", "OPEN_BRACE", "CLOSE_BRACE", "COMMA", 
            "DOT", "MINUS", "PLUS", "SEMICOLON", "SLASH", "MULTIPLY", "MODULO", 
            "LESS_THAN", "GREATER_THAN", "EQUAL", "NOT_EQUAL", "LESS_EQUAL", 
            "GREATER_EQUAL", "ASSIGN", "IDENTIFIER", "STRING", "NUMBER", 
            "COMMENT", "WHITESPACE" ]

    ruleNames = [ "VAR", "FUN", "FOR", "IF", "ELSE", "WHILE", "PRINT", "RETURN", 
                  "OR", "AND", "NOT", "TRUE", "FALSE", "NIL", "THIS", "SUPER", 
                  "OPEN_PAREN", "CLOSE_PAREN", "OPEN_BRACE", "CLOSE_BRACE", 
                  "COMMA", "DOT", "MINUS", "PLUS", "SEMICOLON", "SLASH", 
                  "MULTIPLY", "MODULO", "LESS_THAN", "GREATER_THAN", "EQUAL", 
                  "NOT_EQUAL", "LESS_EQUAL", "GREATER_EQUAL", "ASSIGN", 
                  "IDENTIFIER", "STRING", "NUMBER", "COMMENT", "WHITESPACE" ]

    grammarFileName = "Lexico.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


