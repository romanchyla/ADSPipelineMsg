from msg import Msg
from .protobuf import denormalized_record_pb2

class DenormalizedRecord(Msg):

    def __init__(self):
        super(DenormalizedRecord, self).__init__()
        self._data = denormalized_record_pb2.DenormalizedRecord()

