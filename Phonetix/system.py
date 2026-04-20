
KEYS = (
'+-', 'S-', 'T-', 'K-', 'P-', 'W-', 'H-', 'R-',
'A-', 'O-',
'*',
'-U', '-I',
'-F', '-R', '-P', '-B', '-L', '-G', '-T', '-S', '-D', '-Z'
)

IMPLICIT_HYPHEN_KEYS = ('*', 'A-', 'O-', '-U', '-I')

SUFFIX_KEYS = ()

NUMBER_KEY = None

NUMBERS = {}

UNDO_STROKE_STENO = ('*')

ORTHOGRAPHY_RULES = [
    # dropping silent e before endings
    (r'^(.+[bcdfghjklmnpqrstuvz])e \^ (able|age|ed|est|ing|ings|ion|ory|ous)$', r'\1\2'),

    # dropping e after double vowels
    (r'^(.+[ie])e \^ (e.+)$', r'\1\2'),

    # consonant + y pluralization
    (r'^(.+[bcdfghjklmnpqrstvwxz])y \^ s$', r'\1ies'),

    # consonant doubling
    (r'^(.*(?:[bcdfghjklmnprstvwxyz]|qu)[aeiou])([bcdfgklmnprtvz]) \^ ((ee|[eo]i)(?:[bcdfghjklmnpqrstvwxyz].?)?)$', r'\1\2\2\3'),
    (r'^(.*(?:[bcdfghjklmnprstvwxyz]|qu)[aeiou])([bcdfgklmnprtvz]) \^ (([aeiouy]|[ai]e)(?:[bcdfghjklmnpqrstvwxyz].?))$', r'\1\2\2\3'),
    (r'^(.*(?:[bcdfghjklmnprstvwxyz]|qu)[aeiou])([bcdfgklmnprtvz]) \^ ([ei]?ous)$', r'\1\2\2\3'),
    (r'^(.*(?:[bcdfghjklmnprstvwxyz]|qu)[aeiou])([bcdfgklmnprtvz]) \^ ([ai]ble)$', r'\1\2\2\3'),
    (r'^(.*(?:[bcdfghjklmnprstvwxyz]|qu)[aeiou])([bcdfgklmnprtvz]) \^ ([ae]nce)$', r'\1\2\2\3'),
    (r'^(.*(?:[bcdfghjklmnprstvwxyz]|qu)[aeiou])([bcdfgklmnprtvz]) \^ (e[rn]ing)$', r'\1\2\2\3'),
    (r'^(.*(?:[bcdfghjklmnprstvwxyz]|qu)[aeiou])([bcdfgklmnprtvz]) \^ (ation)$', r'\1\2\2\3'),
    (r'^(.*(?:[bcdfghjklmnprstvwxyz]|qu)[aeiou])([bcdfgklmnprtvz]) \^ (iness)$', r'\1\2\2\3'),
    (r'^(.*(?:[bcdfghjklmnprstvwxyz]|qu)[aeiou])([bcdfgklmnprtvz]) \^ (ably)$', r'\1\2\2\3'),
    (r'^(.*(?:[bcdfghjklmnprstvwxyz]|qu)[aeiou])([bcdfgklmnprtvz]) \^ (ened)$', r'\1\2\2\3'),
    (r'^(.*(?:[bcdfghjklmnprstvwxyz]|qu)[aeiou])([bcdfgklmnprtvz]) \^ (ings)$', r'\1\2\2\3'),
]

ORTHOGRAPHY_RULES_ALIASES = {
    'able': 'ible',
    'ability': 'ibility',
}

ORTHOGRAPHY_WORDLIST = 'american_english_words.txt'

KEYMAPS = {
        'Gemini PR': {
        '+-' : ('#1','#2'),
        'S-' : ('S1-','S2-'),
        'T-' : 'T-',
        'K-' : 'K-',
        'P-' : 'P-',
        'W-' : 'W-',
        'H-' : 'H-',
        'R-' : 'R-',
        'A-' : 'A-',
        'O-' : 'O-',
        '*'  : ('*1','*2','*3','*4','#3','#4'),
        '-U' : '-E',
        '-I' : '-U',
        '-F' : '-F',
        '-R' : '-R',
        '-P' : '-P',
        '-B' : '-B',
        '-L' : '-L',
        '-G' : '-G',
        '-T' : '-T',
        '-S' : '-S',
        '-D' : '-D',
        '-Z' : '-Z',
        },
        'Plover HID': {
        '+-' : ('#1','#2'),
        'S-' : ('S1-','S2-'),
        'T-' : 'T-',
        'K-' : 'K-',
        'P-' : 'P-',
        'W-' : 'W-',
        'H-' : 'H-',
        'R-' : 'R-',
        'A-' : 'A-',
        'O-' : 'O-',
        '*'  : ('*1','*2','*3','*4','#3','#4'),
        '-U' : '-E',
        '-I' : '-U',
        '-F' : '-F',
        '-R' : '-R',
        '-P' : '-P',
        '-B' : '-B',
        '-L' : '-L',
        '-G' : '-G',
        '-T' : '-T',
        '-S' : '-S',
        '-D' : '-D',
        '-Z' : '-Z',
        },
        'Keyboard': {
        '+-' : 'q',
        'S-' : 'a',
        'T-' : 'w',
        'K-' : 's',
        'P-' : 'e',
        'W-' : 'd',
        'H-' : 'r',
        'R-' : 'f',
        'A-' : 'c',
        'O-' : 'v',
        '*'  : ('space','t','g','y','h'),
        '-U' : 'n',
        '-I' : 'm',
        '-F' : 'u',
        '-R' : 'j',
        '-P' : 'i',
        '-B' : 'k',
        '-L' : 'o',
        '-G' : 'l',
        '-T' : 'p',
        '-S' : ';',
        '-D' : '[',
        '-Z' : '\'',
        'arpeggiate' : 'return',
        }
}
DICTIONARIES_ROOT = 'asset:Phonetix:dictionaries'
DEFAULT_DICTIONARIES = ('phonetix-user.json','phonetix-commands.json','phonetix-brief.json','phonetix-preffix.json','phonetix-suffix.json','phonetix-base.json','jeff-phrasing.py')



