from case_changer import case_changer

class Test_Title:

    def test_empty(self):
        input_str = ""
        output_str = case_changer.CaseChanger(input_str).to_title()
        assert output_str == "", "should return empty string if input is empty"

    def test_all_lower(self):
        input_str = "abcdefghijk"
        output_str = case_changer.CaseChanger(input_str).to_title()
        assert output_str == "Abcdefghijk", "should return same string with first character in upper case"

    def test_mixed_upper(self):
        input_str = "aBcDeFgHiJK"
        output_str = case_changer.CaseChanger(input_str).to_title()
        assert output_str == "Abcdefghijk", "should return same string with only first character in upper case"

    def test_single_character(self):
        input_str = "a"
        output_str = case_changer.CaseChanger(input_str).to_title()
        assert output_str == "A", "should return same character in upper case"

    def test_all_upper(self):
        input_str = "ABCDEFGHIJLK"
        output_str = case_changer.CaseChanger(input_str).to_title()
        assert output_str == "Abcdefghijlk", "should return same string with only first character in upper case"

    def test_type_cast(self):
        input_val = 123
        output_str = case_changer.CaseChanger(input_val).to_title()
        assert output_str == "123", "should cast to string"

    def test_alphanumeric(self):
        input_val = "a1b2c3d4e5f6g7h8i9j10l"
        output_str = case_changer.CaseChanger(input_val).to_title()
        assert output_str == "A1b2c3d4e5f6g7h8i9j10l", "should return same string with only first character in upper case"
    
    def test_alphanumeric_sentences(self):
        input_val = "The quick brown fox jumps over the 3 lazy dogs."
        output_str = case_changer.CaseChanger(input_val).to_title()
        assert output_str == "The Quick Brown Fox Jumps Over The 3 Lazy Dogs.", "should cast to string and change all to upper case"

    def test_alphanumeric_sentences_with_symbols(self):
        input_val = "they're bill's friends from the UK"
        output_str = case_changer.CaseChanger(input_val).to_title()
        assert output_str == "They're Bill's Friends From The Uk", "should cast to string and change all to upper case"