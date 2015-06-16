# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: preloads.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2 as common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='preloads.proto',
  package='Preloads',
  syntax='proto2',
  serialized_pb=_b('\n\x0epreloads.proto\x12\x08Preloads\x1a\x0c\x63ommon.proto\"\xa6\x01\n\x07Preload\x12\x1c\n\x05\x64ocid\x18\x01 \x01(\x0b\x32\r.Common.Docid\x12\x13\n\x0bversionCode\x18\x02 \x01(\x05\x12\r\n\x05title\x18\x03 \x01(\t\x12\x1b\n\x04icon\x18\x04 \x01(\x0b\x32\r.Common.Image\x12\x15\n\rdeliveryToken\x18\x05 \x01(\t\x12\x17\n\x0finstallLocation\x18\x06 \x01(\x05\x12\x0c\n\x04size\x18\x07 \x01(\x03\"c\n\x10PreloadsResponse\x12(\n\rconfigPreload\x18\x01 \x01(\x0b\x32\x11.Preloads.Preload\x12%\n\nappPreload\x18\x02 \x03(\x0b\x32\x11.Preloads.PreloadB,\n com.google.android.finsky.protosB\x08Preloads')
  ,
  dependencies=[common__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PRELOAD = _descriptor.Descriptor(
  name='Preload',
  full_name='Preloads.Preload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='docid', full_name='Preloads.Preload.docid', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='versionCode', full_name='Preloads.Preload.versionCode', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='title', full_name='Preloads.Preload.title', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='icon', full_name='Preloads.Preload.icon', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deliveryToken', full_name='Preloads.Preload.deliveryToken', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='installLocation', full_name='Preloads.Preload.installLocation', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='size', full_name='Preloads.Preload.size', index=6,
      number=7, type=3, cpp_type=2, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=43,
  serialized_end=209,
)


_PRELOADSRESPONSE = _descriptor.Descriptor(
  name='PreloadsResponse',
  full_name='Preloads.PreloadsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='configPreload', full_name='Preloads.PreloadsResponse.configPreload', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='appPreload', full_name='Preloads.PreloadsResponse.appPreload', index=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=211,
  serialized_end=310,
)

_PRELOAD.fields_by_name['docid'].message_type = common__pb2._DOCID
_PRELOAD.fields_by_name['icon'].message_type = common__pb2._IMAGE
_PRELOADSRESPONSE.fields_by_name['configPreload'].message_type = _PRELOAD
_PRELOADSRESPONSE.fields_by_name['appPreload'].message_type = _PRELOAD
DESCRIPTOR.message_types_by_name['Preload'] = _PRELOAD
DESCRIPTOR.message_types_by_name['PreloadsResponse'] = _PRELOADSRESPONSE

Preload = _reflection.GeneratedProtocolMessageType('Preload', (_message.Message,), dict(
  DESCRIPTOR = _PRELOAD,
  __module__ = 'preloads_pb2'
  # @@protoc_insertion_point(class_scope:Preloads.Preload)
  ))
_sym_db.RegisterMessage(Preload)

PreloadsResponse = _reflection.GeneratedProtocolMessageType('PreloadsResponse', (_message.Message,), dict(
  DESCRIPTOR = _PRELOADSRESPONSE,
  __module__ = 'preloads_pb2'
  # @@protoc_insertion_point(class_scope:Preloads.PreloadsResponse)
  ))
_sym_db.RegisterMessage(PreloadsResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n com.google.android.finsky.protosB\010Preloads'))
# @@protoc_insertion_point(module_scope)
