# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: debug_info_proto.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='debug_info_proto.proto',
  package='DebugInfoProto',
  syntax='proto2',
  serialized_pb=_b('\n\x16\x64\x65\x62ug_info_proto.proto\x12\x0e\x44\x65\x62ugInfoProto\"x\n\tDebugInfo\x12\x0f\n\x07message\x18\x01 \x03(\t\x12\x30\n\x06timing\x18\x02 \x03(\x0b\x32 .DebugInfoProto.DebugInfo.Timing\x1a(\n\x06Timing\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x10\n\x08timeInMs\x18\x04 \x01(\x01\x42\x32\n com.google.android.finsky.protosB\x0e\x44\x65\x62ugInfoProto')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_DEBUGINFO_TIMING = _descriptor.Descriptor(
  name='Timing',
  full_name='DebugInfoProto.DebugInfo.Timing',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='DebugInfoProto.DebugInfo.Timing.name', index=0,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timeInMs', full_name='DebugInfoProto.DebugInfo.Timing.timeInMs', index=1,
      number=4, type=1, cpp_type=5, label=1,
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
  serialized_start=122,
  serialized_end=162,
)

_DEBUGINFO = _descriptor.Descriptor(
  name='DebugInfo',
  full_name='DebugInfoProto.DebugInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='DebugInfoProto.DebugInfo.message', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timing', full_name='DebugInfoProto.DebugInfo.timing', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_DEBUGINFO_TIMING, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=42,
  serialized_end=162,
)

_DEBUGINFO_TIMING.containing_type = _DEBUGINFO
_DEBUGINFO.fields_by_name['timing'].message_type = _DEBUGINFO_TIMING
DESCRIPTOR.message_types_by_name['DebugInfo'] = _DEBUGINFO

DebugInfo = _reflection.GeneratedProtocolMessageType('DebugInfo', (_message.Message,), dict(

  Timing = _reflection.GeneratedProtocolMessageType('Timing', (_message.Message,), dict(
    DESCRIPTOR = _DEBUGINFO_TIMING,
    __module__ = 'debug_info_proto_pb2'
    # @@protoc_insertion_point(class_scope:DebugInfoProto.DebugInfo.Timing)
    ))
  ,
  DESCRIPTOR = _DEBUGINFO,
  __module__ = 'debug_info_proto_pb2'
  # @@protoc_insertion_point(class_scope:DebugInfoProto.DebugInfo)
  ))
_sym_db.RegisterMessage(DebugInfo)
_sym_db.RegisterMessage(DebugInfo.Timing)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n com.google.android.finsky.protosB\016DebugInfoProto'))
# @@protoc_insertion_point(module_scope)
