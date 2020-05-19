import re

class CaseChanger:
    def __init__(self, original_str):
        self.current_str = str(original_str)

    def to_upper(self):
        if type(self.current_str) is not str:
            raise TypeError
        return self.current_str.upper()

    def to_lower(self):
        if type(self.current_str) is not str:
            raise TypeError
        return self.current_str.lower()

    def to_title(self, sep = r"[\s+_-]"):
        original_str = self.current_str
        split_tokens = re.split(sep, original_str)
        capitalised_tokens = map(lambda token: token[0].upper() + token[1:].lower() if len(token) > 0 else token, split_tokens);
        return " ".join(capitalised_tokens)
    
    def to_upper_camel(self):
        title_str = self.to_title()
        return title_str.replace(" ", "")

    def to_lower_camel(self):
        title_str = self.to_title()
        upper_camel_str = title_str.replace(" ", "")
        return upper_camel_str[0].lower() + upper_camel_str[1:] if len(upper_camel_str) > 0 else upper_camel_str