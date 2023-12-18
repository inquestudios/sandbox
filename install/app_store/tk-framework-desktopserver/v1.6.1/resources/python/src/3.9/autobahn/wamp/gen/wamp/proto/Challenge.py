# automatically generated by the FlatBuffers compiler, do not modify

# namespace: proto

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Challenge(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Challenge()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsChallenge(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Challenge
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Challenge
    def Session(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # Challenge
    def Method(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # Challenge
    def Extra(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from wamp.Map import Map
            obj = Map()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def ChallengeStart(builder): builder.StartObject(3)
def Start(builder):
    return ChallengeStart(builder)
def ChallengeAddSession(builder, session): builder.PrependUint64Slot(0, session, 0)
def AddSession(builder, session):
    return ChallengeAddSession(builder, session)
def ChallengeAddMethod(builder, method): builder.PrependUint8Slot(1, method, 0)
def AddMethod(builder, method):
    return ChallengeAddMethod(builder, method)
def ChallengeAddExtra(builder, extra): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(extra), 0)
def AddExtra(builder, extra):
    return ChallengeAddExtra(builder, extra)
def ChallengeEnd(builder): return builder.EndObject()
def End(builder):
    return ChallengeEnd(builder)