# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modify_library.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import library_update_proto_pb2 as library__update__proto__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='modify_library.proto',
  package='ModifyLibrary',
  syntax='proto2',
  serialized_pb=_b('\n\x14modify_library.proto\x12\rModifyLibrary\x1a\x1alibrary_update_proto.proto\"Q\n\x15ModifyLibraryResponse\x12\x38\n\rlibraryUpdate\x18\x01 \x01(\x0b\x32!.LibraryUpdateProto.LibraryUpdate\"p\n\x14ModifyLibraryRequest\x12\x11\n\tlibraryId\x18\x01 \x01(\t\x12\x13\n\x0b\x66orAddDocid\x18\x02 \x03(\t\x12\x17\n\x0f\x66orRemovalDocid\x18\x03 \x03(\t\x12\x17\n\x0f\x66orArchiveDocid\x18\x04 \x03(\tB1\n com.google.android.finsky.protosB\rModifyLibrary')
  ,
  dependencies=[library__update__proto__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_MODIFYLIBRARYRESPONSE = _descriptor.Descriptor(
  name='ModifyLibraryResponse',
  full_name='ModifyLibrary.ModifyLibraryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='libraryUpdate', full_name='ModifyLibrary.ModifyLibraryResponse.libraryUpdate', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=67,
  serialized_end=148,
)


_MODIFYLIBRARYREQUEST = _descriptor.Descriptor(
  name='ModifyLibraryRequest',
  full_name='ModifyLibrary.ModifyLibraryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='libraryId', full_name='ModifyLibrary.ModifyLibraryRequest.libraryId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='forAddDocid', full_name='ModifyLibrary.ModifyLibraryRequest.forAddDocid', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='forRemovalDocid', full_name='ModifyLibrary.ModifyLibraryRequest.forRemovalDocid', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='forArchiveDocid', full_name='ModifyLibrary.ModifyLibraryRequest.forArchiveDocid', index=3,
      number=4, type=9, cpp_type=9, label=3,
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
  serialized_start=150,
  serialized_end=262,
)

_MODIFYLIBRARYRESPONSE.fields_by_name['libraryUpdate'].message_type = library__update__proto__pb2._LIBRARYUPDATE
DESCRIPTOR.message_types_by_name['ModifyLibraryResponse'] = _MODIFYLIBRARYRESPONSE
DESCRIPTOR.message_types_by_name['ModifyLibraryRequest'] = _MODIFYLIBRARYREQUEST

ModifyLibraryResponse = _reflection.GeneratedProtocolMessageType('ModifyLibraryResponse', (_message.Message,), dict(
  DESCRIPTOR = _MODIFYLIBRARYRESPONSE,
  __module__ = 'modify_library_pb2'
  # @@protoc_insertion_point(class_scope:ModifyLibrary.ModifyLibraryResponse)
  ))
_sym_db.RegisterMessage(ModifyLibraryResponse)

ModifyLibraryRequest = _reflection.GeneratedProtocolMessageType('ModifyLibraryRequest', (_message.Message,), dict(
  DESCRIPTOR = _MODIFYLIBRARYREQUEST,
  __module__ = 'modify_library_pb2'
  # @@protoc_insertion_point(class_scope:ModifyLibrary.ModifyLibraryRequest)
  ))
_sym_db.RegisterMessage(ModifyLibraryRequest)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n com.google.android.finsky.protosB\rModifyLibrary'))
# @@protoc_insertion_point(module_scope)
