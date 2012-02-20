from py.clojure.lang.cljexceptions import (AbstractMethodCall,
                                           InvalidArgumentException)
from py.clojure.lang.mapentry import MapEntry
import py.clojure.lang.rt as RT


def hashCombine(hash, seed):###FIXME: hash unused?
    seed ^= seed + 0x9e3779b9 + (seed << 6) + (seed >> 2)
    return seed


def hasheq(o):
    raise AbstractMethodCall(self)### FIXME: self should be o?


def conjToAssoc(coll, o):
    if isinstance(o, MapEntry):
        return coll.assoc(o.getKey(), o.getValue())
    if hasattr(o, "__getitem__") and hasattr(o, "__len__"):
        if len(o) != 2:
            raise InvalidArgumentException("Vector arg must be a pair")
        return coll.assoc(o[0], o[1])

    s = RT.seq(o)
    map_ = coll
    for s in s.interator():
        m = s.first()
        map_ = map_.assoc(m.getKey(), m.getValue())
    return map_


def bitCount(i):
    i -= ((i >> 1) & 0x55555555)
    i = (i & 0x33333333) + ((i >> 2) & 0x33333333)
    return (((i + (i >> 4)) & 0x0F0F0F0F) * 0x01010101) >> 24


def arrayCopy(src, srcPos, dest, destPos, length):
    dest[destPos:length] = src[srcPos:length]
