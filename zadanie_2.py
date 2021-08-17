def brakujace_elementy(istniejace, n):
    return [x for x in list(range(1, n + 1)) if x not in istniejace]


# Poniżej testy

def test_gdy_dodaje_pusta_liste_i_3_to_zwracana_jest_pelna_lista_od_1_do_3():
    assert brakujace_elementy([], 3) == [1, 2, 3]


def test_gdy_dodaje_pusta_liste_i_4_to_zwracana_jest_pelna_lista_od_1_do_4():
    assert brakujace_elementy([], 4) == [1, 2, 3, 4]


def test_gdy_lista_zawiera_elementy_to_nie_sa_one_zwracane_w_liscie_docelowej():
    assert brakujace_elementy([2, 4], 5) == [1, 3, 5]
