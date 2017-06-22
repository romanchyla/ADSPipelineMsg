from .msg import Msg
from .protobuf import fulltext_request_pb2

class FulltextRequests(Msg):

    def __init__(self, *args, **kwargs):
        if 'fulltext_array' in kwargs:
          kwargs['requests'] = [fulltext_request_pb2.FulltextRequest(**x) for x in kwargs.pop('fulltext_array')]
        super(FulltextRequests, self).__init__(fulltext_request_pb2.FulltextRequests(), args, kwargs)

