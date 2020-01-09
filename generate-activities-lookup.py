#!/bin/python


results = 'Resultado Forms'
weights = 'Atividades Pesos'


def get_next_column(column):
    if len(column) == 2:
        # hack to prevent crash
        return "AB"

    column = ord(column) + 1

    if column <= ord("Z"):
        return chr(column)
    else:
        return "AA"


activities = [
        "Artística",
        "Aquática",
        "Esportes",
        "Natureza",
        "Código",
        ]

def query_get(index):
    """
    ='Resultado Forms'!$C2*'Atividades Pesos'!$C$2+'Resultado Forms'!$D2*'Atividades Pesos'!$D$2
    """
    strings = ["="]
    column = "C"
    weight_row = index + 2 # it starts on 2

    for i in range(25):
        # 'Resultado Forms'!$C2*'Atividades Pesos'!$C$2 +
        strings.append("'{results}'!${column}2 * '{weights}'!${column}${weight_row} + ".format(
            column=column,
            results=results,
            weights=weights,
            weight_row=weight_row))
        column = get_next_column(column)

    return " ".join(strings)[:-3]


def main():
    for i, activity in enumerate(activities):
        print("{activity} {query}".format(activity=activity, query=query_get(i)))


if __name__ == "__main__":
    main()
