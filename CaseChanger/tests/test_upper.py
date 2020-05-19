from case_changer import case_changer

class TestUpper:

    def test_empty(self):
        input_str = ""
        output_str = case_changer.CaseChanger(input_str).to_upper()
        assert output_str == "", "should return empty string if input is empty"

    def test_all_upper(self):
        input_str = "ABCDEFGHIJLK"
        output_str = case_changer.CaseChanger(input_str).to_upper()
        assert input_str == output_str, "should return same string if input has no lower case"

    def test_mixed_upper(self):
        input_str = "aBcDeFgHiJlK"
        output_str = case_changer.CaseChanger(input_str).to_upper()
        assert output_str == "ABCDEFGHIJLK", "should return same string with all upper case"

    def test_all_lower(self):
        input_str = "abcdefghijlk"
        output_str = case_changer.CaseChanger(input_str).to_upper()
        assert output_str == "ABCDEFGHIJLK", "should return same string with all upper case"

    def test_type(self):
        input_val = 123
        output_str = case_changer.CaseChanger(input_val).to_upper()
        assert output_str == "123", "should cast to string"

    def test_alphanumeric(self):
        input_val = "a1b2c3d4e5f6g7h8i9j10l"
        output_str = case_changer.CaseChanger(input_val).to_upper()
        assert output_str == "A1B2C3D4E5F6G7H8I9J10L", "should cast to string and change all to upper case"
    
    def test_alphanumeric_sentences(self):
        input_val = "The quick brown fox jumps over the 3 lazy dogs."
        output_str = case_changer.CaseChanger(input_val).to_upper()
        assert output_str == "THE QUICK BROWN FOX JUMPS OVER THE 3 LAZY DOGS.", "should cast to string and change all to upper case"