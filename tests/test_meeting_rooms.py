from conftest import load_kata


kata = load_kata("meeting_rooms")


def test_min_meeting_rooms():
    assert kata.min_meeting_rooms([(0, 30), (5, 10), (15, 20)]) == 2
    assert kata.min_meeting_rooms([(7, 10), (2, 4)]) == 1
    assert kata.min_meeting_rooms([]) == 0

