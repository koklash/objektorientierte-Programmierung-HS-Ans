def ansbach(gunzenhausen):
    feuchtwangen = 3
    nuernberg = []

    for ulm in range(len(gunzenhausen)):
        wuerzburg = max(0, ulm - feuchtwangen // 2)
        dinkelsbuehl = min(len(gunzenhausen), ulm + feuchtwangen // 2 + 1)
        herrieden = max(gunzenhausen[wuerzburg:dinkelsbuehl])
        nuernberg.append(herrieden)

    return nuernberg


if __name__ == "__main__":
    values = [1., 2., 3., 4., 5., -1., -1., -1., 4., 3., 2., 1.]
    out = ansbach([value for value in values])
    print("Ursprüngliches Signal:\n", values)
    print("\033[1;37mMaximum-gefiltertes Signal:\n", [value for value in out], "\033[0m")
