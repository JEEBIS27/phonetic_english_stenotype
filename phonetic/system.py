KEYS = (
'#-', 'S-', 'T-', 'K-', 'P-', 'W-', 'H-', 'R-',
'A-', 'O-',
'*',
'-U', '-I',
'-F', '-R', '-P', '-B', '-L', '-G', '-T', '-S', '-D', '-Z'
)

IMPLICIT_HYPHEN_KEYS = ('*')

SUFFIX_KEYS = ()

NUMBER_KEY = None

NUMBERS = {}

UNDO_STROKE_STENO = ('*')

ORTHOGRAPHY_RULES = []

ORTHOGRAPHY_RULES_ALIASES = {}

ORTHOGRAPHY_WORDLIST = None

KEYMAPS = {
        'Gemini PR': {
        '#-'  : ('#1','#2'),
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
        '#-'  : ('#1','#2'),
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
        '#-' : 'q',
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
DICTIONARIES_ROOT = 'asset:phonetic:dictionaries/default'
DEFAULT_DICTIONARIES = ('phonetic-user.json','phonetic-commands.json','phonetic-brief.json','phonetic-base.json','jeff-phrasing.py')



