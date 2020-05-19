from case_changer import case_changer

class TestLower:

    def test_empty(self):
        input_str = ""
        output_str = case_changer.CaseChanger(input_str).to_lower()
        assert output_str == "", "should return empty string if input is empty"

    def test_all_lower(self):
        input_str = "abcdefghijk"
        output_str = case_changer.CaseChanger(input_str).to_lower()
        assert input_str == output_str, "should return same string if input has no upper case letters"

    def test_mixed_upper(self):
        input_str = "aBcDeFgHiJK"
        output_str = case_changer.CaseChanger(input_str).to_lower()
        assert output_str == "abcdefghijk", "should return same string with all lower case letters"

    def test_all_upper(self):
        input_str = "ABCDEFGHIJLK"
        output_str = case_changer.CaseChanger(input_str).to_lower()
        assert output_str == "abcdefghijlk", "should return same string with all lower case letters"

    def test_type_cast(self):
        input_val = 123
        output_str = case_changer.CaseChanger(input_val).to_lower()
        assert output_str == "123", "should cast to string"


    def test_alphanumeric(self):
        input_val = "a1b2c3d4e5f6g7h8i9j10l"
        output_str = case_changer.CaseChanger(input_val).to_lower()
        assert output_str == "a1b2c3d4e5f6g7h8i9j10l", "should cast to string and change all to lower case"
    
    def test_alphanumeric_sentences(self):
        input_val = "The quick brown fox jumps over the 3 lazy dogs."
        output_str = case_changer.CaseChanger(input_val).to_lower()
        assert output_str == "the quick brown fox jumps over the 3 lazy dogs.", "should cast to string and change all to upper case"