from case_changer import case_changer

class TestLowerCamel:

    def test_empty(self):
        input_str = ""
        output_str = case_changer.CaseChanger(input_str).to_lower_camel()
        assert output_str == "", "should return empty string if input is empty"

    def test_all_lower(self):
        input_str = "abcdefghijk"
        output_str = case_changer.CaseChanger(input_str).to_lower_camel()
        assert output_str == "abcdefghijk", "should return same string"

    def test_mixed_upper(self):
        input_str = "aBcDeFgHiJK"
        output_str = case_changer.CaseChanger(input_str).to_lower_camel()
        assert output_str == "abcdefghijk", "should return same string with only lowerCamelCase"

    def test_single_character(self):
        input_str = "a"
        output_str = case_changer.CaseChanger(input_str).to_lower_camel()
        assert output_str == "a", "should return same character in lowerCamelCase"

    def test_all_upper(self):
        input_str = "ABCDEFGHIJLK"
        output_str = case_changer.CaseChanger(input_str).to_lower_camel()
        assert output_str == "abcdefghijlk", "should return same string in lowerCamelCase"

    def test_type_cast(self):
        input_val = 123
        output_str = case_changer.CaseChanger(input_val).to_lower_camel()
        assert output_str == "123", "should cast to string"

    def test_alphanumeric(self):
        input_val = "a1b2c3d4e5f6g7h8i9j10l"
        output_str = case_changer.CaseChanger(input_val).to_lower_camel()
        assert output_str == "a1b2c3d4e5f6g7h8i9j10l", "should return same string in lowerCamelCase"
    
    def test_alphanumeric_sentences(self):
        input_val = "The quick brown fox jumps over the 3 lazy dogs."
        output_str = case_changer.CaseChanger(input_val).to_lower_camel()
        assert output_str == "theQuickBrownFoxJumpsOverThe3LazyDogs.", "should cast to string and change to lowerCamelCase"

    def test_alphanumeric_sentences_with_symbols(self):
        input_val = "they're bill's friends from the UK"
        output_str = case_changer.CaseChanger(input_val).to_lower_camel()
        assert output_str == "they'reBill'sFriendsFromTheUk", "should cast to string and change to lowerCamelCase"

    def test_multiple_spaces(self):
        input_str = "this    is a  variable  with     multiple     spaces"
        output_str = case_changer.CaseChanger(input_str).to_lower_camel()
        assert output_str == "thisIsAVariableWithMultipleSpaces", "should return same string in lowerCamelCase"

    def test_underscores(self):
        input_str = "this_is_a_variable"
        output_str = case_changer.CaseChanger(input_str).to_lower_camel()
        assert output_str == "thisIsAVariable", "should return same string in lowerCamelCase"

    def test_hyphens(self):
        input_str = "this-is-a-variable"
        output_str = case_changer.CaseChanger(input_str).to_lower_camel()
        assert output_str == "thisIsAVariable", "should return same string in lowerCamelCase"