from .msg import Msg
from .protobuf import nonbibrecord_pb2

class NonBibRecord(Msg):

    def __init__(self, *args, **kwargs):
        instance = nonbibrecord_pb2.NonBibRecord()
        data_links = kwargs.pop('data_links', None) # remove for special handling
        super(NonBibRecord, self).__init__(instance, args, kwargs)
        if data_links:
            # convert data_links dict <key, string array> to inner record
            # probably vestigial since data links does not come from nonbib
            for k in data_links:
                instance.data_links.get_or_create(k) 
                instance.data_links[k].value.extend(data_links[k])
                


class NonBibRecordList(Msg):

    def __init__(self, *args, **kwargs):
        super(NonBibRecordList, self).__init__(nonbibrecord_pb2.NonBibRecordList(), args, kwargs)

