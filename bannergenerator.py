r"""Simple Banner Generator

||================================================================================================||
||          ____             __    _ __    _  _____  _____                                        ||
||         ||   \\     /\    |\\   | |\\   | ||    ` ||   \\                                      ||
||         ||___//    / \\   | \\  | | \\  | ||___   ||___//                                      ||
||         ||    \\  /___\\  |  \\ | |  \\ | ||      || \\                                        ||
||         ||____// /     \\ |   \\| |   \\| ||____, ||  \\,                                      ||
||           ____    _____  __    _  _____  _____             ________    ____   _____            ||
||          //   `  ||    ` |\\   | ||    ` ||   \\    /\    '   ||   '  //  \\  ||   \\ |        ||
||         ||   ___ ||___   | \\  | ||___   ||___//   / \\       ||     ||    || ||___// |        ||
||         ||    || ||      |  \\ | ||      || \\    /___\\      ||     ||    || || \\   |        ||
||          \\___/| ||____, |   \\| ||____, ||  \\, /     \\    _||_     \\__//  ||  \\, '        ||
||                                                                                       o        ||
||================================================================================================||
||======================================= BANNER GENERATOR! ======================================||
||================================================================================================||
"""

import argparse

# :------------------------------------------------------------------------------------------------:
# :                                         __  __  ,  , ___                                       :
# :                                        |_  /  \ |\ |  |                                        :
# :                                        |   \__/ | \|  |                                        :
# :                                                                                                :
# :------------------------------------------------------------------------------------------------:
# :--------------------------------------------- Font ---------------------------------------------:
# :------------------------------------------------------------------------------------------------:


big_font = { # height == 2 (caps) 4 total
'ABCDEFGHIJKLMNOPQRSTUVWXYZ':r"""
  _    __   __   _    __  __  __  _  _ ___   _         ,   , ,  ,  __   __   __   __   __  ___ .  . _  _               ___
 /_\  |__) /  ` |  \ |_  |_  /  _ |__|  |    | |_/ |   |\_/| |\ | /  \ |__) /  \ |__) (__`  |  |  | \  / | . | \_/ \_/  _/
/   \ |__) \__, |__/ |__ |   \__) |  | _|_ \_/ | \ |__ |   | | \| \__/ |    \__\ | \_ .__)  |  |__|  \/  |/ \| / \  |  /__,
""",  # noqa: E501

'abcdefghijklmnopqrstuvwxyz':r"""
                      _                 ╮
 __╮ |_   _   _|  _  /_  _, |_  °  ° ╮, | ,  ,  _   _  ,_   _,  ,_  _ _|_             ╮,    _
(_/| |_) (_, (_| (/, |  (_| | | |  | |\ | |\/| | | (_) |_) (_|  |  _\  |  (_| \/ |/\| /\ |/ /_
                        ._/       /                    j     |,                          /
""",
',.!"_-':r"""
    . ||
    |         ___
    !    ____
/ ° °
""",
}

huge_font = { # height == 4 (caps) 6 total
'ABCDEFGHIJKLMNOP':r"""
          ____      ____   ____     _____   _____    ____   __    __ ____   ____ __  __  __     __      __  __    _   ____   _____
   /\    ||   \\   //   ` ||   \\  ||    ` ||    `  //   `  ||    ||  ||     ||  ||  /   ||     |\\    /||  |\\   |  //  \\  ||   \\
  / \\   ||___//  ||      ||    || ||___   ||___   ||   ___ ||____||  ||     ||  || /    ||     | \\  / ||  | \\  | ||    || ||___//
 /___\\  ||    \\ ||      ||    || ||      ||      ||    || ||    ||  ||     ||  ||/\\   ||     |  \\/  ||  |  \\ | ||    || ||
/     \\ ||____//  \\___/ ||___//  ||____, ||       \\___/| ||    || _||_ \__//  ||  \\, ||___, |       ||  |   \\|  \\__//  ||
""",  # noqa: E501

'QRSTUVWXYZ':r"""
  ____    _____     _____   ________  __     _  __     _ __   __     _ ___  __ __    __  _____
 //  \\   ||   \\  //    ` '   ||   ' ||     |  \\     / \\   \\     /  \\  /   \\   /  '   //
||    ||  ||___//  \\___       ||     ||     |   \\   /   \\   \\   /    \\/     \\ /      //
||    ||  || \\         \\     ||     ||     |    \\ /     \\ / \\ /     /\\      ||      //
 \\__//   ||  \\,  \____//    _||_     \\___/      \/       \/   \/    _/  \\_   _||_    //___,
  '  \\_,
""",

'1234567890':r"""
 __   _____    ___             _____,    ___    _______   ___      ____     _____
/||  /    \\ //   \\    /||   ||       //   `  |-----//  //  \\   //  \\   //   \\
 ||       //      //   / ||   ||___   ||____        //  ||    || ||    || ||   / ||
 ||     //      -<(   /  ||   |/   \\ ||   \\      //    ))><((   \\__/|| ||  /  ||
 ||   //          \\ /___||_,      || ||    ||    //    ||    ||       |/ || /   ||
_||_ ||____, \\___//    _||_  \\___//  \\__//     ||     \\__//   .____/   \\___//
""",

'abcdefghijklmnopqrstuvwxyz':r"""

 __    ╮            ╮        __       ╮     °     ° ╮    ╮                                              ╮
 __\   |__   __   __|   __  /__`  __, |__   ╮     ╮ | /  |    _  _      __    __   ╮__   __,  ╮_   __  _|_                               ___
/   |  |  \ /  ` /  |  /__) |    /  | |  \  |     | |/   |  ╮/ |/ |   ╮/  |  /  \  |  \ /  |  | ` (__`  |  ╮  ╮  \  / \ \  / \_/   \  /  __/
\__/|, |__/ \__, \__|, \__, |    \__| |  |, |,    | | \, |, |     |,  |   |, \__/  |__/ \__|  |   .__)  |, \__|,  \/   \/\/  / \,   \/  /__,
                            /    .__/           ._/      `                        .|       |,                                     ._/
""", # noqa: E501

',.!"_-':r"""

    | ||
    |
    |          ___
    '    _____
/ ° o
""",
"'?()|[]{}":r"""
    ___    // \\  || ,== ==.  ,/= =\.
|  /   \  //   \\ || ||   ||  ||   ||
       /  ||   || || ||   || //     \\
     /    ||   || || ||   || \\     //
     '    \\   // || ||   ||  ||   ||
     o     \\ //  || `== =='  `\= =/'
""",
}


# :------------------------------------------------------------------------------------------------:
# :                                __  ___  __   __  _  _   _    __                                :
# :                               |__)  |  /  _ /  ` |__|  /_\  |__)                               :
# :                               |__) _|_ \__) \__, |  | /   \ | \_                               :
# :                                                                                                :
# :------------------------------------------------------------------------------------------------:
# :-------------------------------------------- BigChar -------------------------------------------:
# :------------------------------------------------------------------------------------------------:

class BigChar:
    """BigChar stores multi-line char as a list of strings."""

    def __init__(self, lines:list):
        """Create a BigChar.

        `lines` should be a list of strings,
        representing a single multi-line character.
        """
        self.width = len(max(lines, key=len))
        # pad line endings
        for idx, line in enumerate(lines):
            if len(line) < self.width:
                lines[idx] = line + (' ' * (self.width - len(line)))
        self.lines = lines
        self.height = len(lines)

    def __repr__(self):
        string = '\n'.join(self.lines)
        return f'BigChar<\n{string}\n>'



# :------------------------------------------------------------------------------------------------:
# :                                  __  ___  __   __  __  ,  , ___                                :
# :                                 |__)  |  /  _ |_  /  \ |\ |  |                                 :
# :                                 |__) _|_ \__) |   \__/ | \|  |                                 :
# :                                                                                                :
# :------------------------------------------------------------------------------------------------:
# :-------------------------------------------- BigFont -------------------------------------------:
# :------------------------------------------------------------------------------------------------:

class BigFont:
    """A container for BigChars, which can convert a string to a big string."""

    def __init__(self):
        """Create a BigFont with only a single space character."""
        self.chars = {}
        # add space as a default char
        self.add_char(' ', [' '])
        self.height = 1


    def __getitem__(self, key:str) -> BigChar:
        # somewhat fuzzy matching so displaying varied text is easier:
        if key in self.chars:
            return self.chars[key]
        if key.lower() in self.chars:
            return self.chars[key.lower()]
        if key.upper() in self.chars:
            return self.chars[key.upper()]
        return self.chars[' ']


    def __setitem__(self, key:str, val:BigChar):
        self.chars[key] = val


    def render_text(
            self,
            text: str,
            *,
            char_sep: str = ' ',
            wide_space: int = 2,
            clean_empty: bool = False,
            add_underline: bool = False,
            ) -> str:
        """Convert a given string into a multiline "BigChar" string.

        Args:
        - text:
            A string to make into a big string.

        Kwargs:
        - char_sep:
            A character to add between all characters. Defaults to " " to space out letters more.
        - wide_space:
            The number of times to repeat spaces in the output text.
        - clean_empty:
            Whether or not to remove empty first/last lines before returning.
        - add_underline:
            Whether or not to add an additional underline to the text.
        """
        if wide_space > 1:
            text = text.replace(' ', ' ' * wide_space)
        if char_sep:
            # separate characters by the given separator
            text = char_sep.join(list(text))

        big_line = [''] * self.height
        for char in text:
            big_char = self[char]
            char_lines = big_char.lines
            for idx, _line in enumerate(big_line):
                if idx < len(char_lines):
                    big_line[idx] += char_lines[idx]
                else:
                    # pad line with spaces
                    big_line[idx] += ' ' * big_char.width
        if clean_empty:
            if big_line[0].isspace():
                big_line.pop(0)
            if big_line[-1].isspace():
                big_line.pop(-1)
        if add_underline:
            total_len = len(max(big_line, key=len))
            big_line.append('~' * total_len)
        return big_line


    def _set_height(self):
        self.height = max(char.height for char in self.chars.values())


    def add_char(self, char:str, lines:list[str]):
        """Add one char to font, where lines is a list of string representing a multiline character."""
        self.chars[char] = BigChar(lines)


    @staticmethod
    def _ensure_equal_lenth(lines:list[str]) -> list[str]:
        """Make all input lines the same length"""
        # find the largest len
        full_len = len(max(lines, key=len))
        for idx, line in enumerate(lines):
            lines[idx] += ' ' * (full_len - len(line))
        return lines


    def bulk_add_chars(self, chars:str, lines:list[str]):
        """Add multiple chars at once.

        Args:
        - chars:
            A string containing one or more chars
        - lines:
            A list of strings containing matching multiline characters, separated by spaces.
        """
        # add a space to each line, to make finding the final char easier
        lines = [line + ' ' for line in lines]
        lines = self._ensure_equal_lenth(lines)
        # iterate over each char
        for char in chars:
            idx = 0
            # while idx is less than multiline length
            while idx < len(lines[0]):
                # if entire multiline is a space
                if all(line[idx].isspace() for line in lines):
                    # split char lines off of source lines
                    char_lines = [line[:idx] for line in lines]
                    lines = [line[idx:] for line in lines]

                    self[char] = BigChar(char_lines)

                    # clean starting spaces in multiline for next char
                    while all(line and line[0].isspace() for line in lines):
                        lines = [line[1:] for line in lines]
                    break
                idx += 1
        self._set_height()





# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
# |                                   __      __                                                   |
# |                                   |\\    /||  __    °                                          |
# |                                   | \\  / ||  __\   ╮    __                                    |
# |                                   |  \\/  || /   |  |  ╮/  |                                   |
# |                                   |       || \__/|, |, |   |,                                  |
# |                                                                                                |
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Main ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|



# :------------------------------------------------------------------------------------------------:
# :                           __   __ ___ .  .  __       __  __  ,  , ___                          :
# :                          (__` |_   |  |  | |__)     |_  /  \ |\ |  |                           :
# :                          .__) |__  |  |__| |        |   \__/ | \|  |                           :
# :                                                                                                :
# :------------------------------------------------------------------------------------------------:
# :------------------------------------------ Setup Font ------------------------------------------:
# :------------------------------------------------------------------------------------------------:
def setup_font(chosen_font:dict) -> BigFont:
    """Create and return the chosen font"""
    # process font chars
    font = BigFont()
    for key, val in chosen_font.items():
        lines = val.splitlines()[1:] # first line is an empty newline, and doesn't count
        font.bulk_add_chars(key, lines)
    return font



# :------------------------------------------------------------------------------------------------:
# :                          __   __ ___ .  .  __        _    __   __   __                         :
# :                         (__` |_   |  |  | |__)      /_\  |__) /  _ (__`                        :
# :                         .__) |__  |  |__| |        /   \ | \_ \__) .__)                        :
# :                                                                                                :
# :------------------------------------------------------------------------------------------------:
# :------------------------------------------ Setup Args ------------------------------------------:
# :------------------------------------------------------------------------------------------------:

def setup_generator_args() -> dict:
    """Get banner settings from input args"""

    #                       _                                  __           _  _
    #                      /_\  ,_  _, ,_   __╮ ,_  _  _      (__` _|_     /_ /_
    #                     /   \ |  (_| |_) (_/| |  _\ (/,     .__)  |  (_| |  |
    #                              ._/ j
    parser = argparse.ArgumentParser()
    parser.add_argument('text', help='The text to use in the banner', nargs='+')
    parser.add_argument(
        '--style',
        help='Choose a baseline style for the banner ("xxl", "xl", "l", "m")',
        default='l',
        )
    parser.add_argument('-w', '--width', help='The total width of the banner', type=int, default=100)
    parser.add_argument('--title_case', help='enable title case in the big text', action='store_true')
    parser.add_argument('--plain_case', help='Dont modify the case from the input.', action='store_true')
    parser.add_argument('--caps_case', help='Convert big text to all caps.', action='store_true')
    parser.add_argument('--no_space_subtitle', help='Remove spaces from the subtitle text.', action='store_true')
    parser.add_argument('--trim_blank', help='Delete any empty lines before finishing', action='store_true')
    parser.add_argument('--h_char', help='Char to use for the horizontal bars')
    parser.add_argument('--v_char', help='Char to use for the vertical bars')
    parser.add_argument('--no_comment', help='disable "#" at the start of the lines', action='store_true')
    args = parser.parse_args()

    use_comment = not args.no_comment
    trim_blank = args.trim_blank
    text = ' '.join(args.text)

    #                        __           _                       __         ╮
    #                       /  `  _   _  /_ °  _,     ,_  _      (__` _|_    |  _
    #                       \__, (_) | | |  | (_| (_| |  (/,     .__)  |  |/ | (/,
    #                                         ._/                         /
    add_underline = False
    style = args.style
    match style.lower():
        case 'xxl':
            font = huge_font
            big_text = text.upper()
            sub_text = text
            h_char = '='
            v_char = '||'
        case 'xl':
            font = huge_font
            big_text = text.title()
            sub_text = text
            h_char = '~'
            v_char = '|'
        case 'l':
            font = big_font
            big_text = text.upper()
            sub_text = text
            h_char = '-'
            v_char = ':'
        case 'm':
            font = big_font
            big_text = text.title()
            sub_text = ''
            h_char = ' '
            v_char = ' '
            trim_blank = True
            add_underline = True
        case _:
            all_styles = ('xxl', 'xl', 'l', 'm')
            msg = f'Style should be one of {all_styles} (got {style})'
            raise ValueError(msg)

    # override style defaults with specific options
    # override banner chars
    if args.h_char:
        h_char = args.h_char
    if args.v_char:
        v_char = args.v_char
    # override text style
    if args.title_case:
        big_text = big_text.title()
    elif args.caps_case:
        big_text = big_text.upper()
    elif args.plain_case:
        big_text = text

    # make room for added comment and left/right bars
    total_width = width = args.width
    if use_comment:
        width -= 2
    width -= len(v_char) * 2

    return {
        'font':font,
        'big_text':big_text,
        'sub_text':sub_text,
        'h_char':h_char,
        'v_char':v_char,
        'total_width':total_width,
        'width':width,
        'use_comment':use_comment,
        'trim_blank':trim_blank,
        'add_underline':add_underline,
    }



# :------------------------------------------------------------------------------------------------:
# :                      ,   ,   _        __      __    _   ,  , ,  ,  __  __                      :
# :                      |\_/|  /_\  |_/ |_      |__)  /_\  |\ | |\ | |_  |__)                     :
# :                      |   | /   \ | \ |__     |__) /   \ | \| | \| |__ | \_                     :
# :                                                                                                :
# :------------------------------------------------------------------------------------------------:
# :------------------------------------------ Make Banner -----------------------------------------:
# :------------------------------------------------------------------------------------------------:

def make_banner():
    """Make a giant banner from given args"""
    args = setup_generator_args()
    font = setup_font(args['font'])
    big_text = args['big_text']
    sub_text = args['sub_text']
    width = args['width']
    h_char = args['h_char']
    v_char = args['v_char']
    width = args['width']
    trim_blank = args['trim_blank']
    use_comment = args['use_comment']
    add_underline = args['add_underline']

    #                           _
    #                          /_\   _|  °      _ _|_     | . | °  _| _|_ |_
    #                         /   \ (_|  | (_| _\  |      |/ \| | (_|  |  | |
    #                                   /
    big_line = font.render_text(big_text, add_underline=add_underline)
    # account for lines too long
    if len(big_line[0]) > width:
        big_line = font.render_text(big_text, char_sep='', add_underline=add_underline)
    if len(big_line[0]) > width:
        big_line = font.render_text(big_text, char_sep='', wide_space=1, add_underline=add_underline)
    if len(big_line[0]) > width:
        # try splitting the lines
        split_text = big_text.split()

        def multi_big_line(words, char_sep) -> list[str]:
            """Make a multi-line big_line"""
            big_line = []
            for word in words:
                big_line += font.render_text(
                    word,
                    char_sep=char_sep,
                    wide_space=1,
                    clean_empty=True,
                    add_underline=add_underline,
                    )
            return big_line

        big_line = multi_big_line(split_text, ' ')
        full_len = len(max(big_line, key=len))

        # final effort for making it fit
        if full_len > width:
            big_line = multi_big_line(split_text, '')
            full_len = len(max(big_line, key=len))

        # ensure same len:
        for idx, line in enumerate(big_line):
            big_line[idx] += ' ' * (full_len - len(line))

    #                      __                           __
    #                     /  ` ,_  _   __╮ _|_  _      |__)  _  ,_  _|  _  ,_  _
    #                     \__, |  (/, (_/|  |  (/,     |__) (_) |  (_| (/, |  _\.
    # pad big line on left/right
    line_len = len(big_line[0])
    additional_width = width - line_len
    additional_right = additional_width // 2
    additional_left = additional_width - additional_right
    big_line = [(' ' * additional_left) + line + (' ' * additional_right) for line in big_line]


    # add horizontal lines to top and bottom
    hline = (h_char * width)

    # add searchable annotation below
    sub_text = ' ' + sub_text + ' '
    additional_width = width - len(sub_text)
    additional_right = additional_width // 2
    additional_left = additional_width - additional_right
    sub_text = h_char * additional_left + sub_text + h_char * additional_right

    big_line = [hline, *big_line, hline, sub_text, hline]


    # add left/right bars
    big_line = [v_char + line + v_char for line in big_line]


    #                                 __  ╮                  .  .
    #                                /  ` |  _   __╮  _      |  | ,_
    #                                \__, | (/, (_/| | |     |__| |_)
    #                                                             j
    # remove any completely blank lines
    if trim_blank:
        big_line = [line for line in big_line if not line.isspace()]

    if use_comment:
        big_line = ['# ' + line for line in big_line]

    # removing trailing whitespace
    big_line = [line.rstrip() for line in big_line]

    print('\n'.join(big_line))


if __name__ == '__main__':
    make_banner()
