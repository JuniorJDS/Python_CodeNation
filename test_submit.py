import pytest
from main import classify_by_phone_number

records = [
    {'source': '48-996355555', 'destination': '48-666666666', 'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097', 'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097', 'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788', 'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788', 'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099', 'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697', 'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099', 'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697', 'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097', 'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564627800, 'start': 1564626000}
]

class TestChallenge1:

    expected = [
        {'source': '41-833333333', 'total': 4.77},
        {'source': '48-999999999', 'total': 4.68},
        {'source': '41-885633788', 'total': 3.96},
        {'source': '48-996355555', 'total': 2.61},
        {'source': '41-886383097', 'total': 1.53},
        {'source': '48-996383697', 'total': 1.35}
    ]

    def test_len(self):
        result = classify_by_phone_number(records)
        assert len(result) == 6

    def test_1(self):
        result = classify_by_phone_number(records)
        assert result[0] == self.expected[0]

    def test_2(self):
        result = classify_by_phone_number(records)
        assert result[1] == self.expected[1]

    def test_3(self):
        result = classify_by_phone_number(records)
        assert result[2] == self.expected[2]

    def test_4(self):
        result = classify_by_phone_number(records)
        assert result[3] == self.expected[3]

    def test_5(self):
        result = classify_by_phone_number(records)
        assert result[4] == self.expected[4]

    def test_6(self):
        result = classify_by_phone_number(records)
        assert result[5] == self.expected[5]

    def test_7(self):
        result = classify_by_phone_number(records)
        assert result == TestChallenge1.expected