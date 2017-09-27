from .msg import Msg
from .protobuf import nonbibrecord_pb2

class NonBibSolrRecord(Msg):

    def __init__(self, *args, **kwargs):
        super(NonBibSolrRecord, self).__init__(nonbibrecord_pb2.NonBibSolrRecord(), args, kwargs)


class NonBibSolrRecordList(Msg):

    def __init__(self, *args, **kwargs):
        super(NonBibSolrRecordList, self).__init__(nonbibrecord_pb2.NonBibSolrRecordList(), args, kwargs)

