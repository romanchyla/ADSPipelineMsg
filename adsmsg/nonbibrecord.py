from .msg import Msg
from .protobuf import nonbibrecord_pb2

class NonBibRecord(Msg):

    def __init__(self, *args, **kwargs):
        super(NonBibRecord, self).__init__(nonbibrecord_pb2.NonBibRecord(), args, kwargs)


class NonBibRecordList(Msg):

    def __init__(self, *args, **kwargs):
        super(NonBibRecordList, self).__init__(nonbibrecord_pb2.NonBibRecordList(), args, kwargs)

