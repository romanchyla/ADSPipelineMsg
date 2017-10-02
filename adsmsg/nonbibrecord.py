from .msg import Msg
from .protobuf import nonbibrecord_pb2

class NonBibRecord(Msg):

    def __init__(self, *args, **kwargs):
        instance = nonbibrecord_pb2.NonBibRecord()
        links_data = kwargs.pop('links_data', None) # remove for special handling
        data_links_rows = kwargs.pop('data_links_rows', None) 
        super(NonBibRecord, self).__init__(instance, args, kwargs)
        if links_data:
            # convert links_data dict <key, string array> to inner record
            # eventually vestigial
            for k in links_data:
                instance.links_data.get_or_create(k) 
                instance.links_data[k].value.extend(links_data[k])
        if data_links_rows:
            # populate rows from database field
            for current in data_links_rows:
                row = instance.data_links_rows.add()
                row.link_type = current['link_type']
                row.link_sub_type = current['link_sub_type']
                row.item_count = current['item_count']
                row.url.extend(current['url'])
                row.title.extend(current['title'])
                

class NonBibRecordList(Msg):

    def __init__(self, *args, **kwargs):
        super(NonBibRecordList, self).__init__(nonbibrecord_pb2.NonBibRecordList(), args, kwargs)

