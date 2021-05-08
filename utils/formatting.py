import unicodedata
import re


def num(s):
    s = re.sub('[(,)]', '', s)
    try:
        res = int(s)
    except:
        res = float(s)
    return res


def normalize(s):
    return unicodedata.normalize('NFKC', s).replace(' ', '')
