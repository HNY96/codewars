def race(v1, v2, g):
    if v1 > v2:
        return None
    else:
        dis = v2 - v1
        hour = float(g) / dis
        res_h = int(hour)
        minute = (hour - res_h) * 60
        res_m = int(minute)
        sec = (minute - res_m) * 60
        res_s = int(sec)
        return [res_h, res_m, res_s]

if __name__ == '__main__':
    print(race(80, 91, 37))
