from tarifia.kit.math import tarifia_round


def test_tarifia_round() -> None:
    assert tarifia_round(0) == 0
    assert tarifia_round(0.1) == 0.0
    assert tarifia_round(0.3) == 0.0
    assert tarifia_round(0.5) == 1.0
    assert tarifia_round(0.6) == 1.0
    assert tarifia_round(0.8) == 1.0
    assert tarifia_round(1.0) == 1.0
    assert tarifia_round(1.2) == 1.0
    assert tarifia_round(1.5) == 2.0
    assert tarifia_round(1.7) == 2.0
    assert tarifia_round(101.2) == 101.0
    assert tarifia_round(232.49) == 232.0
    assert tarifia_round(232.5) == 233.0
    assert tarifia_round(232.51) == 233.0
    assert tarifia_round(111111111.0) == 111111111.0

    assert tarifia_round(-0) == -0
    assert tarifia_round(-0.1) == 0.0
    assert tarifia_round(-0.3) == 0.0
    assert tarifia_round(-0.5) == -1.0
    assert tarifia_round(-0.6) == -1.0
    assert tarifia_round(-0.8) == -1.0
    assert tarifia_round(-1.0) == -1.0
    assert tarifia_round(-1.2) == -1.0
    assert tarifia_round(-1.5) == -2.0
    assert tarifia_round(-1.7) == -2.0
    assert tarifia_round(-111) == -111
    assert tarifia_round(-111.0) == -111.0
    assert tarifia_round(-232.2) == -232.0
    assert tarifia_round(-232.49) == -232.0
    assert tarifia_round(-232.5) == -233.0
    assert tarifia_round(-232.51) == -233.0
    assert tarifia_round(-111111111.0) == -111111111.0
