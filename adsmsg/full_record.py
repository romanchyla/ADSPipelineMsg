from msg import Msg
from protobuf import full_record_pb2

class FullRecord(Msg):

    def __init__(self):
        super(FullRecord, self).__init__()
        self._data = full_record_pb2.FullRecord()

    @property
    def record(self):
        return self._data
