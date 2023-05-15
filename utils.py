from enum import Enum, auto
import re


class SymbolTableHeader(Enum):
    """Represents the symbol table header as enum in order
    to map the corresponding index state given the char type."""
    DIGIT = 0
    LETTER = auto()
    DOT = auto()
    EULER = auto()
    SLASH = auto()
    ASTERISK = auto()
    SINGLE_QUOTE = auto()
    HYPHEN = auto()
    PLUS = auto()
    COMMA = auto()
    SEMICOLON = auto()
    COLON = auto()
    EQUALS = auto()
    EXCLAMATION = auto()
    AMPERSAND = auto()
    PIPE = auto()
    GREATER_THAN = auto()
    SPACE = auto()
    LESS_THAN = auto()
    PARENTHESIS_O = auto()
    PARENTHESIS_C = auto()
    BRACKET_O = auto()
    BRACKET_C = auto()
    SQUARE_BRACKET_O = auto()
    SQUARE_BRACKET_C = auto()


class Utils:
    @staticmethod
    def get_char_state(ch: str) -> int:
        """Gets the corresponing state of the 'ch' param (char)."""
        if Utils.is_digit(ch):
            return SymbolTableHeader.DIGIT.value
        elif Utils.is_letter(ch):
            return SymbolTableHeader.LETTER.value
        elif Utils.is_dot(ch):
            return SymbolTableHeader.DOT.value
        elif Utils.is_euler(ch):
            return SymbolTableHeader.EULER.value
        elif Utils.is_slash(ch):
            return SymbolTableHeader.SLASH.value
        elif Utils.is_asterisk(ch):
            return SymbolTableHeader.ASTERISK.value
        elif Utils.is_single_quote(ch):
            return SymbolTableHeader.SINGLE_QUOTE.value
        elif Utils.is_hyphen(ch):
            return SymbolTableHeader.HYPHEN.value
        elif Utils.is_plus(ch):
            return SymbolTableHeader.PLUS.value
        elif Utils.is_comma(ch):
            return SymbolTableHeader.COMMA.value
        elif Utils.is_semicolon(ch):
            return SymbolTableHeader.SEMICOLON.value
        elif Utils.is_colon(ch):
            return SymbolTableHeader.COLON.value
        elif Utils.is_equals(ch):
            return SymbolTableHeader.EQUALS.value
        elif Utils.is_exclamation(ch):
            return SymbolTableHeader.EXCLAMATION.value
        elif Utils.is_ampersand(ch):
            return SymbolTableHeader.AMPERSAND.value
        elif Utils.is_pipe(ch):
            return SymbolTableHeader.PIPE.value
        elif Utils.is_greater_than(ch):
            return SymbolTableHeader.GREATER_THAN.value
        elif Utils.is_space(ch):
            return SymbolTableHeader.SPACE.value
        elif Utils.is_less_than(ch):
            return SymbolTableHeader.LESS_THAN.value
        elif Utils.is_parenthesis_o(ch):
            return SymbolTableHeader.PARENTHESIS_O.value
        elif Utils.is_parenthesis_c(ch):
            return SymbolTableHeader.PARENTHESIS_C.value
        elif Utils.is_bracket_o(ch):
            return SymbolTableHeader.BRACKET_O.value
        elif Utils.is_bracket_c(ch):
            return SymbolTableHeader.BRACKET_C.value
        elif Utils.is_square_bracket_o(ch):
            return SymbolTableHeader.SQUARE_BRACKET_O.value
        elif Utils.is_square_bracket_c(ch):
            return SymbolTableHeader.SQUARE_BRACKET_C.value

    @staticmethod
    def is_digit(ch: str) -> bool:
        return Utils.match_regex('\d', ch)

    @staticmethod
    def is_letter(ch: str) -> bool:
        return Utils.match_regex('[A-Za-z]', ch)

    @staticmethod
    def is_dot(ch: str) -> bool:
        return Utils.match_regex('\.', ch)

    @staticmethod
    def is_euler(ch: str) -> bool:
        return Utils.match_regex('e', ch)

    @staticmethod
    def is_slash(ch: str) -> bool:
        return Utils.match_regex('\/', ch)

    @staticmethod
    def is_asterisk(ch: str) -> bool:
        return Utils.match_regex('\*', ch)

    @staticmethod
    def is_single_quote(ch: str) -> bool:
        return Utils.match_regex("\'", ch)

    @staticmethod
    def is_hyphen(ch: str) -> bool:
        return Utils.match_regex('\-', ch)

    @staticmethod
    def is_plus(ch: str) -> bool:
        return Utils.match_regex('\+', ch)

    @staticmethod
    def is_comma(ch: str) -> bool:
        return Utils.match_regex('\,', ch)

    @staticmethod
    def is_semicolon(ch: str) -> bool:
        return Utils.match_regex('\;', ch)

    @staticmethod
    def is_colon(ch: str) -> bool:
        return Utils.match_regex('\:', ch)

    @staticmethod
    def is_equals(ch: str) -> bool:
        return Utils.match_regex('\=', ch)

    @staticmethod
    def is_exclamation(ch: str) -> bool:
        return Utils.match_regex('\!', ch)

    @staticmethod
    def is_ampersand(ch: str) -> bool:
        return Utils.match_regex('\&', ch)

    @staticmethod
    def is_pipe(ch: str) -> bool:
        return Utils.match_regex('\|', ch)

    @staticmethod
    def is_greater_than(ch: str) -> bool:
        return Utils.match_regex('\>', ch)

    @staticmethod
    def is_less_than(ch: str) -> bool:
        return Utils.match_regex('\<', ch)

    @staticmethod
    def is_parenthesis_o(ch: str) -> bool:
        return Utils.match_regex('\(', ch)

    @staticmethod
    def is_parenthesis_c(ch: str) -> bool:
        return Utils.match_regex('\)', ch)

    @staticmethod
    def is_bracket_o(ch: str) -> bool:
        return Utils.match_regex('\{', ch)

    @staticmethod
    def is_bracket_c(ch: str) -> bool:
        return Utils.match_regex('\}', ch)

    @staticmethod
    def is_square_bracket_o(ch: str) -> bool:
        return Utils.match_regex('\[', ch)

    @staticmethod
    def is_square_bracket_c(ch: str) -> bool:
        return Utils.match_regex('\]', ch)

    @staticmethod
    def is_space(ch: str) -> bool:
        return Utils.match_regex('\s', ch)

    @staticmethod
    def match_regex(regex: str, string: str) -> bool:
        return re.match(regex, string) is not None
