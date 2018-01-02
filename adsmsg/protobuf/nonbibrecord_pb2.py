# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nonbibrecord.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import status_pb2 as status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='nonbibrecord.proto',
  package='adsmsg',
  syntax='proto3',
  serialized_pb=_b('\n\x12nonbibrecord.proto\x12\x06\x61\x64smsg\x1a\x0cstatus.proto\"\xea\x02\n\x0cNonBibRecord\x12\x0f\n\x07\x62ibcode\x18\x01 \x01(\t\x12\x16\n\x0esimbad_objects\x18\x03 \x03(\t\x12\x0e\n\x06grants\x18\x04 \x03(\t\x12\r\n\x05\x62oost\x18\x06 \x01(\x02\x12\x16\n\x0e\x63itation_count\x18\x07 \x01(\x05\x12\x12\n\nread_count\x18\x08 \x01(\x05\x12\x0f\n\x07readers\x18\t \x03(\t\x12\x11\n\treference\x18\x0c \x03(\t\x12\x13\n\x0bned_objects\x18\r \x03(\t\x12\x0c\n\x04\x64\x61ta\x18\x0e \x03(\t\x12\x19\n\x11total_link_counts\x18\x0f \x01(\x05\x12\x0f\n\x07\x65source\x18\x11 \x03(\t\x12\x10\n\x08property\x18\x12 \x03(\t\x12-\n\x0f\x64\x61ta_links_rows\x18\x13 \x03(\x0b\x32\x14.adsmsg.DataLinksRow\x12\x1e\n\x06status\x18\x14 \x01(\x0e\x32\x0e.adsmsg.Status\x12\x12\n\nnorm_cites\x18\x15 \x01(\x05\"h\n\x0c\x44\x61taLinksRow\x12\x11\n\tlink_type\x18\x01 \x01(\t\x12\x15\n\rlink_sub_type\x18\x02 \x01(\t\x12\x0b\n\x03url\x18\x03 \x03(\t\x12\r\n\x05title\x18\x04 \x03(\t\x12\x12\n\nitem_count\x18\x05 \x01(\x05\"`\n\x10NonBibRecordList\x12,\n\x0enonbib_records\x18\x01 \x03(\x0b\x32\x14.adsmsg.NonBibRecord\x12\x1e\n\x06status\x18\x02 \x01(\x0e\x32\x0e.adsmsg.Status\"Q\n\x0f\x44\x61taLinksRecord\x12\x0f\n\x07\x62ibcode\x18\x01 \x01(\t\x12-\n\x0f\x64\x61ta_links_rows\x18\x02 \x03(\x0b\x32\x14.adsmsg.DataLinksRow\"i\n\x13\x44\x61taLinksRecordList\x12\x32\n\x11\x64\x61talinks_records\x18\x01 \x03(\x0b\x32\x17.adsmsg.DataLinksRecord\x12\x1e\n\x06status\x18\x02 \x01(\x0e\x32\x0e.adsmsg.Statusb\x06proto3')
  ,
  dependencies=[status__pb2.DESCRIPTOR,])




_NONBIBRECORD = _descriptor.Descriptor(
  name='NonBibRecord',
  full_name='adsmsg.NonBibRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bibcode', full_name='adsmsg.NonBibRecord.bibcode', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='simbad_objects', full_name='adsmsg.NonBibRecord.simbad_objects', index=1,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='grants', full_name='adsmsg.NonBibRecord.grants', index=2,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='boost', full_name='adsmsg.NonBibRecord.boost', index=3,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='citation_count', full_name='adsmsg.NonBibRecord.citation_count', index=4,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='read_count', full_name='adsmsg.NonBibRecord.read_count', index=5,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='readers', full_name='adsmsg.NonBibRecord.readers', index=6,
      number=9, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reference', full_name='adsmsg.NonBibRecord.reference', index=7,
      number=12, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ned_objects', full_name='adsmsg.NonBibRecord.ned_objects', index=8,
      number=13, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='adsmsg.NonBibRecord.data', index=9,
      number=14, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total_link_counts', full_name='adsmsg.NonBibRecord.total_link_counts', index=10,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='esource', full_name='adsmsg.NonBibRecord.esource', index=11,
      number=17, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='property', full_name='adsmsg.NonBibRecord.property', index=12,
      number=18, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data_links_rows', full_name='adsmsg.NonBibRecord.data_links_rows', index=13,
      number=19, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='adsmsg.NonBibRecord.status', index=14,
      number=20, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='norm_cites', full_name='adsmsg.NonBibRecord.norm_cites', index=15,
      number=21, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=45,
  serialized_end=407,
)


_DATALINKSROW = _descriptor.Descriptor(
  name='DataLinksRow',
  full_name='adsmsg.DataLinksRow',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='link_type', full_name='adsmsg.DataLinksRow.link_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='link_sub_type', full_name='adsmsg.DataLinksRow.link_sub_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='url', full_name='adsmsg.DataLinksRow.url', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='title', full_name='adsmsg.DataLinksRow.title', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_count', full_name='adsmsg.DataLinksRow.item_count', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=409,
  serialized_end=513,
)


_NONBIBRECORDLIST = _descriptor.Descriptor(
  name='NonBibRecordList',
  full_name='adsmsg.NonBibRecordList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nonbib_records', full_name='adsmsg.NonBibRecordList.nonbib_records', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='adsmsg.NonBibRecordList.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=515,
  serialized_end=611,
)


_DATALINKSRECORD = _descriptor.Descriptor(
  name='DataLinksRecord',
  full_name='adsmsg.DataLinksRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bibcode', full_name='adsmsg.DataLinksRecord.bibcode', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data_links_rows', full_name='adsmsg.DataLinksRecord.data_links_rows', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=613,
  serialized_end=694,
)


_DATALINKSRECORDLIST = _descriptor.Descriptor(
  name='DataLinksRecordList',
  full_name='adsmsg.DataLinksRecordList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='datalinks_records', full_name='adsmsg.DataLinksRecordList.datalinks_records', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='adsmsg.DataLinksRecordList.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=696,
  serialized_end=801,
)

_NONBIBRECORD.fields_by_name['data_links_rows'].message_type = _DATALINKSROW
_NONBIBRECORD.fields_by_name['status'].enum_type = status__pb2._STATUS
_NONBIBRECORDLIST.fields_by_name['nonbib_records'].message_type = _NONBIBRECORD
_NONBIBRECORDLIST.fields_by_name['status'].enum_type = status__pb2._STATUS
_DATALINKSRECORD.fields_by_name['data_links_rows'].message_type = _DATALINKSROW
_DATALINKSRECORDLIST.fields_by_name['datalinks_records'].message_type = _DATALINKSRECORD
_DATALINKSRECORDLIST.fields_by_name['status'].enum_type = status__pb2._STATUS
DESCRIPTOR.message_types_by_name['NonBibRecord'] = _NONBIBRECORD
DESCRIPTOR.message_types_by_name['DataLinksRow'] = _DATALINKSROW
DESCRIPTOR.message_types_by_name['NonBibRecordList'] = _NONBIBRECORDLIST
DESCRIPTOR.message_types_by_name['DataLinksRecord'] = _DATALINKSRECORD
DESCRIPTOR.message_types_by_name['DataLinksRecordList'] = _DATALINKSRECORDLIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NonBibRecord = _reflection.GeneratedProtocolMessageType('NonBibRecord', (_message.Message,), dict(
  DESCRIPTOR = _NONBIBRECORD,
  __module__ = 'nonbibrecord_pb2'
  # @@protoc_insertion_point(class_scope:adsmsg.NonBibRecord)
  ))
_sym_db.RegisterMessage(NonBibRecord)

DataLinksRow = _reflection.GeneratedProtocolMessageType('DataLinksRow', (_message.Message,), dict(
  DESCRIPTOR = _DATALINKSROW,
  __module__ = 'nonbibrecord_pb2'
  # @@protoc_insertion_point(class_scope:adsmsg.DataLinksRow)
  ))
_sym_db.RegisterMessage(DataLinksRow)

NonBibRecordList = _reflection.GeneratedProtocolMessageType('NonBibRecordList', (_message.Message,), dict(
  DESCRIPTOR = _NONBIBRECORDLIST,
  __module__ = 'nonbibrecord_pb2'
  # @@protoc_insertion_point(class_scope:adsmsg.NonBibRecordList)
  ))
_sym_db.RegisterMessage(NonBibRecordList)

DataLinksRecord = _reflection.GeneratedProtocolMessageType('DataLinksRecord', (_message.Message,), dict(
  DESCRIPTOR = _DATALINKSRECORD,
  __module__ = 'nonbibrecord_pb2'
  # @@protoc_insertion_point(class_scope:adsmsg.DataLinksRecord)
  ))
_sym_db.RegisterMessage(DataLinksRecord)

DataLinksRecordList = _reflection.GeneratedProtocolMessageType('DataLinksRecordList', (_message.Message,), dict(
  DESCRIPTOR = _DATALINKSRECORDLIST,
  __module__ = 'nonbibrecord_pb2'
  # @@protoc_insertion_point(class_scope:adsmsg.DataLinksRecordList)
  ))
_sym_db.RegisterMessage(DataLinksRecordList)


# @@protoc_insertion_point(module_scope)
