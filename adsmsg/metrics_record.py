from .msg import Msg
from .protobuf import metrics_pb2

class MetricsRecord(Msg):

    def __init__(self, *args, **kwargs):
        super(MetricsRecord, self).__init__(metrics_pb2.MetricsRecord(), args, kwargs)


class MetricsRecordList(Msg):
    
    def __init__(self, *args, **kwargs):
        if 'metrics_array' in kwargs:
            kwargs['metrics_records'] = [MetricsRecord(**x) for x in kwargs.pop('metrics_array')]       
        super(MetricsRecordList, self).__init__(metrics_pb2.MetricsRecordList(), args, kwargs)
