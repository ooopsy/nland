

import re


def amt_number(price):
    total = 0;
    amt1 = re.findall(r"\d+\.?\d*억",price)

    if len(amt1):
        amt1 = re.findall(r"\d+\.?\d*", amt1[0])
        total += int(float(amt1[0]) * 10000 + 0.5)

    remain = re.sub('\d+\.?\d*?억', "", price).replace(",", "")

    if remain :
        total += round(float(re.sub('\d+억', "", remain).replace(",", "")))

    return str(total)


