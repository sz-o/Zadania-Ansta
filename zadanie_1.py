def generuj(kod1, kod2):
    liczba1 = int(kod1.replace('-', ''))
    liczba2 = int(kod2.replace('-', ''))
    if liczba1 > liczba2:
        liczba2, liczba1 = liczba1, liczba2
    bez_minusa = [str(i).zfill(5) for i in range(liczba1, liczba2 + 1)]
    z_minusem = [f'{s[:2]}-{s[2:]}' for s in bez_minusa]
    return z_minusem


# Poniżej testy

def test_gdy_wprowadzam_string_11111_11111_to_generuje_sie_lista_jednoelementowa_11111():
    assert generuj("11-111", "11-111") == ["11-111"]


def test_gdy_wprowadzam_string_11111_11112_to_generuje_sie_lista_dwuelementowa_11111_11112():
    assert generuj("11-111", "11-112") == ["11-111", "11-112"]


def test_gdy_wprowadzam_string_z_luka_pomiedzy_elementami_to_generuje_sie_lista_3elementowa():
    assert generuj("01-234", "01-236") == ["01-234", "01-235", "01-236"]


def test_gdy_wprowadzam_string_z_odwrocona_kolejnoscia_to_generuje_sie_lista_dwuelementowa_rosnaco():
    assert generuj("11-112", "11-111") == ["11-111", "11-112"]
