r"""Simple Banner Generator

|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|           __    _   ,  , ,  ,  __  __       __   __ ,  ,  __  __    _   ___  __   __  .          |
|          |__)  /_\  |\ | |\ | |_  |__)     /  _ |_  |\ | |_  |__)  /_\   |  /  \ |__) |          |
|          |__) /   \ | \| | \| |__ | \_     \__) |__ | \| |__ | \_ /   \  |  \__/ | \_ !          |
|                                                                                       °          |
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Banner Generator! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
"""

import argparse

# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
# |                                         __  __  ,  , ___                                       |
# |                                        |_  /  \ |\ |  |                                        |
# |                                        |   \__/ | \|  |                                        |
# |                                                                                                |
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Font ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|

height = 3
raw_font = {
"ABCDEFGHIJKLMNOPQRSTUVWXYZ":r"""
  _    __   __   _    __  __  __  _  _ ___   _         ,   , ,  ,  __   __   __   __   __  ___ .  . _  _               ___ 
 /_\  |__) /  ` |  \ |_  |_  /  _ |__|  |    | |_/ |   |\_/| |\ | /  \ |__) /  \ |__) (__`  |  |  | \  / | . | \_/ \_/  _/ 
/   \ |__) \__, |__/ |__ |   \__) |  | _|_ \_/ | \ |__ |   | | \| \__/ |    \__\ | \_ .__)  |  |__|  \/  |/ \| / \  |  /__,
""",
"abcdefghijklmnopqrstuvwxyz":r"""
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



# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
# |                                __  ___  __   __  _  _   _    __                                |
# |                               |__)  |  /  _ /  ` |__|  /_\  |__)                               |
# |                               |__) _|_ \__) \__, |  | /   \ | \_                               |
# |                                                                                                |
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ BigChar ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|

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
                lines[idx] = line + (" " * (self.width - len(line)))
        self.lines = lines
        self.height = len(lines)

    def __repr__(self):
        string = "\n".join(self.lines)
        return f"BigChar<\n{string}\n>"



# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
# |                                  __  ___  __   __  __  ,  , ___                                |
# |                                 |__)  |  /  _ |_  /  \ |\ |  |                                 |
# |                                 |__) _|_ \__) |   \__/ | \|  |                                 |
# |                                                                                                |
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ BigFont ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|

class BigFont:
    """A container for BigChars, which can convert a string to a big string."""

    def __init__(self):
        """Create a BigFont with only a single space character."""
        self.chars = {}
        # add space as a default char
        self.add_char(" ", [" "])
        self.height = 1


    def __getitem__(self, key:str) -> BigChar:
        # somewhat fuzzy matching so displaying varied text is easier:
        if key in self.chars:
            return self.chars[key]
        if key.lower() in self.chars:
            return self.chars[key.lower()]
        if key.upper() in self.chars:
            return self.chars[key.upper()]
        return self.chars[" "]


    def __setitem__(self, key:str, val:BigChar):
        self.chars[key] = val


    def render_text(self, text:str, *, char_sep:str=" ", wide_space:int=2, clean_empty:bool=False) -> str:
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
        """
        if wide_space > 1:
            text = text.replace(" ", " " * wide_space)
        if char_sep:
            # separate characters by the given separator
            text = char_sep.join(list(text))

        big_line = [""] * self.height
        for char in text:
            big_char = self[char]
            char_lines = big_char.lines
            for idx, _line in enumerate(big_line):
                if idx < len(char_lines):
                    big_line[idx] += char_lines[idx]
                else:
                    # pad line with spaces
                    big_line[idx] += " " * big_char.width
        if clean_empty:
            if big_line[0].isspace():
                big_line.pop(0)
            if big_line[-1].isspace():
                big_line.pop(-1)
        return "\n".join(big_line)


    def _set_height(self):
        self.height = max(char.height for char in self.chars.values())


    def add_char(self, char:str, lines:list[str]):
        """Add one char to font, where lines is a list of string representing a multiline character."""
        self.chars[char] = BigChar(lines)


    def bulk_add_chars(self, chars:str, lines:list[str]):
        """Add multiple chars at once.

        Args:
        - chars:
            A string containing one or more chars
        - lines:
            A list of strings containing matching multiline characters, separated by spaces.
        """
        # add a space to each line, to make finding the final char easier
        lines = [line + " " for line in lines]
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


# process font chars
font = BigFont()
for key, val in raw_font.items():
    lines = val.splitlines()[1:] # first line is an empty newline, and doesn't count
    font.bulk_add_chars(key, lines)



# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
# |                                      ,   ,   _   ___ ,  ,                                      |
# |                                      |\_/|  /_\   |  |\ |                                      |
# |                                      |   | /   \ _|_ | \|                                      |
# |                                                                                                |
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ MAIN ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("text", help="The text to use in the banner")
    parser.add_argument("-w", "--width", help="The width of the banner", type=int, default=100)
    parser.add_argument("--title_case", help="enable title case", action="store_true")
    parser.add_argument("--plain_case", help="Dont modify the case from the input.", action="store_true")
    parser.add_argument("-H", "--h_char", help="Char to use for the horizontal bars", default="~")
    parser.add_argument("-v", "--v_char", help="Char to use for the vertical bars", default="|")
    parser.add_argument("--no_comment", help='disable "#" at the start of the lines', action="store_true")

    args = parser.parse_args()

    width = args.width
    use_comment = not args.no_comment
    use_title = args.title_case
    plain_case = args.plain_case
    h_char = args.h_char
    v_char = args.v_char

    # make room for added comment and left/right bars
    width -= 4 if use_comment else 2

    text = args.text
    if use_title:
        text = text.title()
    elif not plain_case:
        text = text.upper()

    big_line = font.render_text(text)
    # account for lines too long
    if len(big_line[0]) > width:
        big_line = font.render_text(text, char_sep="")
    if len(big_line[0]) > width:
        big_line = font.render_text(text, char_sep="", wide_space=1)

    big_line = big_line.splitlines()
    # pad big line on left/right
    line_len = len(big_line[0])
    additional_width = width - line_len
    additional_right = additional_width // 2
    additional_left = additional_width - additional_right
    big_line = [(" " * additional_left) + line + (" " * additional_right) for line in big_line]


    # add horizontal lines to top and bottom
    hline = (h_char * width)

    # add searchable annotation below
    small_text = " " + args.text + " "
    additional_width = width - len(small_text)
    additional_right = additional_width // 2
    additional_left = additional_width - additional_right
    small_text = h_char * additional_left + small_text + h_char * additional_right

    big_line = [hline, *big_line, hline, small_text, hline]


    # add left/right bars
    big_line = [v_char + line + v_char for line in big_line]
    if use_comment:
        big_line = ["# " + line for line in big_line]

    print("\n".join(big_line))
