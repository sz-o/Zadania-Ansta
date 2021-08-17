from decimal import Decimal


def generuj_liste():
    return [Decimal(i / 2) for i in range(4, 12)]


# Poniżej testy

def czy_dziesietny(liczba):
    return isinstance(liczba, Decimal)


def test_zwykle_2_nie_jest_typu_decimal():
    assert czy_dziesietny(2) != type(Decimal)


def test_dziesietne_2_jest_typu_decimal():
    assert czy_dziesietny(Decimal(2))


def test_lista_od_4_do_11():
    assert list(range(4, 12)) == [4, 5, 6, 7, 8, 9, 10, 11]


def test_lista_od_dwa_do_piec_i_pol():
    assert [i / 2 for i in range(4, 12)] == [2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5]


def test_lista_dziesietnych_od_dwa_do_piec_i_pol():
    assert generuj_liste() == [Decimal(2),
                               Decimal(2.5),
                               Decimal(3),
                               Decimal(3.5),
                               Decimal(4),
                               Decimal(4.5),
                               Decimal(5),
                               Decimal(5.5)
                               ]
