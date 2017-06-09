from msg import Msg

try:
    from google.protobuf import bibrecord_pb2
except ImportError:
    from protobuf import bibrecord_pb2

class BibRecord(Msg):

    def __init__(self):
        super(BibRecord, self).__init__()
        self._data = bibrecord_pb2.BibRecord()

