from case_changer import case_changer

class TestUpperCamel:

    def test_empty(self):
        input_str = ""
        output_str = case_changer.CaseChanger(input_str).to_upper_camel()
        assert output_str == "", "should return empty string if input is empty"

    def test_all_lower(self):
        input_str = "abcdefghijk"
        output_str = case_changer.CaseChanger(input_str).to_upper_camel()
        assert output_str == "Abcdefghijk", "should return same string with first character in upper case"

    def test_mixed_upper(self):
        input_str = "aBcDeFgHiJK"
        output_str = case_changer.CaseChanger(input_str).to_upper_camel()
        assert output_str == "Abcdefghijk", "should return same string with only first character in upper case"

    def test_single_character(self):
        input_str = "a"
        output_str = case_changer.CaseChanger(input_str).to_upper_camel()
        assert output_str == "A", "should return same character in upper case"

    def test_all_upper(self):
        input_str = "ABCDEFGHIJLK"
        output_str = case_changer.CaseChanger(input_str).to_upper_camel()
        assert output_str == "Abcdefghijlk", "should return same string with only first character in upper case"

    def test_type_cast(self):
        input_val = 123
        output_str = case_changer.CaseChanger(input_val).to_upper_camel()
        assert output_str == "123", "should cast to string"

    def test_alphanumeric(self):
        input_val = "a1b2c3d4e5f6g7h8i9j10l"
        output_str = case_changer.CaseChanger(input_val).to_upper_camel()
        assert output_str == "A1b2c3d4e5f6g7h8i9j10l", "should return same string with only first character in upper case"
    
    def test_alphanumeric_sentences(self):
        input_val = "The quick brown fox jumps over the 3 lazy dogs."
        output_str = case_changer.CaseChanger(input_val).to_upper_camel()
        assert output_str == "TheQuickBrownFoxJumpsOverThe3LazyDogs.", "should cast to string and change to UpperCamelCase"

    def test_alphanumeric_sentences_with_symbols(self):
        input_val = "they're bill's friends from the UK"
        output_str = case_changer.CaseChanger(input_val).to_upper_camel()
        assert output_str == "They'reBill'sFriendsFromTheUk", "should cast to string and change to UpperCamelCase"

    def test_multiple_spaces(self):
        input_str = "this    is a  variable  with     multiple     spaces"
        output_str = case_changer.CaseChanger(input_str).to_upper_camel()
        assert output_str == "ThisIsAVariableWithMultipleSpaces", "should return same string in UpperCamelCase"

    def test_underscores(self):
        input_str = "this_is_a_variable"
        output_str = case_changer.CaseChanger(input_str).to_upper_camel()
        assert output_str == "ThisIsAVariable", "should return same string in UpperCamelCase"

    def test_hyphens(self):
        input_str = "this-is-a-variable"
        output_str = case_changer.CaseChanger(input_str).to_upper_camel()
        assert output_str == "ThisIsAVariable", "should return same string in UpperCamelCase"