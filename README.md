```
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
# |      __    _   ,  , ,  ,  __  __       __   __ ,  ,  __  __    _   ___  __   __      |
# |     |__)  /_\  |\ | |\ | |_  |__) ___ /  _ |_  |\ | |_  |__)  /_\   |  /  \ |__)     |
# |     |__) /   \ | \| | \| |__ | \_     \__) |__ | \| |__ | \_ /   \  |  \__/ | \_     |
# |                                                                                      |
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ banner-generator ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
# |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
```

Simple code comment banner generator for visually dividing long scripts.

```
usage: bannergenerator.py [-h] [-w WIDTH] [--title_case] [--plain_case] [-H H_CHAR] [-v V_CHAR] [--no_comment] text

positional arguments:
  text                  The text to use in the banner

options:
  -h, --help            show this help message and exit
  -w WIDTH, --width WIDTH
                        The width of the banner
  --title_case          enable title case
  --plain_case          Dont modify the case from the input.
  -H H_CHAR, --h_char H_CHAR
                        Char to use for the horizontal bars
  -v V_CHAR, --v_char V_CHAR
                        Char to use for the vertical bars
  --no_comment          disable "#" at the start of the lines
```
