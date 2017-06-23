from .msg import Msg
from .protobuf import normalized_bibrecord_pb2

class NormalizedBibRecord(Msg):

    def __init__(self, *args, **kwargs):
        super(NormalizedBibRecord, self).__init__(normalized_bibrecord_pb2.NormalizedBibRecord(), args, kwargs)

