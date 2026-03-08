from logic_utils import get_range_for_difficulty, parse_guess, check_guess, update_score


# ─── get_range_for_difficulty ───────────────────────────────────────────────

class TestGetRangeForDifficulty:
    def test_easy(self):
        assert get_range_for_difficulty("Easy") == (1, 50)

    def test_normal(self):
        assert get_range_for_difficulty("Normal") == (1, 100)

    def test_hard(self):
        assert get_range_for_difficulty("Hard") == (1, 200)

    def test_unknown_defaults_to_normal(self):
        assert get_range_for_difficulty("Extreme") == (1, 100)

    def test_empty_string(self):
        assert get_range_for_difficulty("") == (1, 100)


# ─── parse_guess ────────────────────────────────────────────────────────────

class TestParseGuess:
    def test_valid_integer(self):
        ok, value, err = parse_guess("42")
        assert ok is True
        assert value == 42
        assert err is None

    def test_float_truncated(self):
        ok, value, err = parse_guess("3.7")
        assert ok is True
        assert value == 3
        assert err is None

    def test_none_input(self):
        ok, value, err = parse_guess(None)
        assert ok is False
        assert value is None
        assert err == "Enter a guess."

    def test_empty_string(self):
        ok, value, err = parse_guess("")
        assert ok is False
        assert value is None
        assert err == "Enter a guess."

    def test_non_numeric(self):
        ok, value, err = parse_guess("abc")
        assert ok is False
        assert value is None
        assert err == "That is not a number."

    def test_negative_number(self):
        ok, value, err = parse_guess("-5")
        assert ok is True
        assert value == -5
        assert err is None

    def test_zero(self):
        ok, value, err = parse_guess("0")
        assert ok is True
        assert value == 0
        assert err is None

    def test_large_number(self):
        ok, value, err = parse_guess("9999")
        assert ok is True
        assert value == 9999
        assert err is None

    def test_whitespace_only(self):
        ok, value, err = parse_guess("   ")
        assert ok is False
        assert value is None
        assert err == "That is not a number."


# ─── check_guess ────────────────────────────────────────────────────────────

class TestCheckGuess:
    def test_correct_guess(self):
        outcome, message = check_guess(50, 50)
        assert outcome == "Win"
        assert "Correct" in message

    def test_too_high(self):
        outcome, message = check_guess(60, 50)
        assert outcome == "Too High"
        assert "LOWER" in message

    def test_too_low(self):
        outcome, message = check_guess(40, 50)
        assert outcome == "Too Low"
        assert "HIGHER" in message

    def test_guess_one_above(self):
        outcome, _ = check_guess(51, 50)
        assert outcome == "Too High"

    def test_guess_one_below(self):
        outcome, _ = check_guess(49, 50)
        assert outcome == "Too Low"

    def test_hint_direction_high(self):
        _, message = check_guess(75, 50)
        assert "LOWER" in message
        assert "HIGHER" not in message

    def test_hint_direction_low(self):
        _, message = check_guess(25, 50)
        assert "HIGHER" in message
        assert "LOWER" not in message


# ─── update_score ───────────────────────────────────────────────────────────

class TestUpdateScore:
    def test_win_first_attempt(self):
        score = update_score(0, "Win", 1)
        assert score == 90

    def test_win_second_attempt(self):
        score = update_score(0, "Win", 2)
        assert score == 80

    def test_win_fifth_attempt(self):
        score = update_score(0, "Win", 5)
        assert score == 50

    def test_win_floor_at_10(self):
        score = update_score(0, "Win", 10)
        assert score == 10

    def test_win_floor_at_10_large_attempt(self):
        score = update_score(0, "Win", 20)
        assert score == 10

    def test_too_high_penalty(self):
        score = update_score(50, "Too High", 1)
        assert score == 45

    def test_too_low_penalty(self):
        score = update_score(50, "Too Low", 1)
        assert score == 45

    def test_symmetric_penalties(self):
        high_score = update_score(100, "Too High", 3)
        low_score = update_score(100, "Too Low", 3)
        assert high_score == low_score == 95

    def test_unknown_outcome(self):
        score = update_score(50, "Unknown", 1)
        assert score == 50

    def test_win_adds_to_existing_score(self):
        score = update_score(20, "Win", 3)
        assert score == 90  # 20 + 70

    def test_penalty_floors_at_zero(self):
        score = update_score(2, "Too High", 1)
        assert score == 0

    def test_penalty_stays_at_zero(self):
        score = update_score(0, "Too Low", 1)
        assert score == 0
