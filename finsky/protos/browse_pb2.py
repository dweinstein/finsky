# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: browse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import resolve_link_pb2 as resolve__link__pb2
import play_survey_pb2 as play__survey__pb2
import common_pb2 as common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='browse.proto',
  package='Browse',
  syntax='proto2',
  serialized_pb=_b('\n\x0c\x62rowse.proto\x12\x06\x42rowse\x1a\x12resolve_link.proto\x1a\x11play_survey.proto\x1a\x0c\x63ommon.proto\"\xba\x01\n\tQuickLink\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1c\n\x05image\x18\x02 \x01(\x0b\x32\r.Common.Image\x12\'\n\x04link\x18\x03 \x01(\x0b\x32\x19.ResolveLink.ResolvedLink\x12\x17\n\x0f\x64isplayRequired\x18\x04 \x01(\x08\x12\x18\n\x10serverLogsCookie\x18\x05 \x01(\x0c\x12\x11\n\tbackendId\x18\x06 \x01(\x05\x12\x12\n\nprismStyle\x18\x07 \x01(\x08\"\x88\x03\n\x0e\x42rowseResponse\x12\x13\n\x0b\x63ontentsUrl\x18\x01 \x01(\t\x12\x10\n\x08promoUrl\x18\x02 \x01(\t\x12$\n\x08\x63\x61tegory\x18\x03 \x03(\x0b\x32\x12.Browse.BrowseLink\x12&\n\nbreadcrumb\x18\x04 \x03(\x0b\x32\x12.Browse.BrowseLink\x12$\n\tquickLink\x18\x05 \x03(\x0b\x32\x11.Browse.QuickLink\x12\x18\n\x10serverLogsCookie\x18\x06 \x01(\x0c\x12\r\n\x05title\x18\x07 \x01(\t\x12\x11\n\tbackendId\x18\x08 \x01(\x05\x12$\n\tbrowseTab\x18\t \x03(\x0b\x32\x11.Browse.BrowseTab\x12\x17\n\x0flandingTabIndex\x18\n \x01(\x05\x12\x19\n\x11quickLinkTabIndex\x18\x0b \x01(\x05\x12!\n\x19quickLinkFallbackTabIndex\x18\x0c \x01(\x05\x12\"\n\x06survey\x18\r \x01(\x0b\x32\x12.PlaySurvey.Survey\"k\n\tBrowseTab\x12\r\n\x05title\x18\x01 \x01(\t\x12\x18\n\x10serverLogsCookie\x18\x02 \x01(\x0c\x12\x0f\n\x07listUrl\x18\x03 \x01(\t\x12$\n\x08\x63\x61tegory\x18\x04 \x03(\x0b\x32\x12.Browse.BrowseLink\"E\n\nBrowseLink\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x64\x61taUrl\x18\x03 \x01(\t\x12\x18\n\x10serverLogsCookie\x18\x04 \x01(\x0c\x42*\n com.google.android.finsky.protosB\x06\x42rowse')
  ,
  dependencies=[resolve__link__pb2.DESCRIPTOR,play__survey__pb2.DESCRIPTOR,common__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_QUICKLINK = _descriptor.Descriptor(
  name='QuickLink',
  full_name='Browse.QuickLink',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Browse.QuickLink.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='image', full_name='Browse.QuickLink.image', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='link', full_name='Browse.QuickLink.link', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='displayRequired', full_name='Browse.QuickLink.displayRequired', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='serverLogsCookie', full_name='Browse.QuickLink.serverLogsCookie', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='backendId', full_name='Browse.QuickLink.backendId', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='prismStyle', full_name='Browse.QuickLink.prismStyle', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=78,
  serialized_end=264,
)


_BROWSERESPONSE = _descriptor.Descriptor(
  name='BrowseResponse',
  full_name='Browse.BrowseResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='contentsUrl', full_name='Browse.BrowseResponse.contentsUrl', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='promoUrl', full_name='Browse.BrowseResponse.promoUrl', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='category', full_name='Browse.BrowseResponse.category', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='breadcrumb', full_name='Browse.BrowseResponse.breadcrumb', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quickLink', full_name='Browse.BrowseResponse.quickLink', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='serverLogsCookie', full_name='Browse.BrowseResponse.serverLogsCookie', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='title', full_name='Browse.BrowseResponse.title', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='backendId', full_name='Browse.BrowseResponse.backendId', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='browseTab', full_name='Browse.BrowseResponse.browseTab', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='landingTabIndex', full_name='Browse.BrowseResponse.landingTabIndex', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quickLinkTabIndex', full_name='Browse.BrowseResponse.quickLinkTabIndex', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quickLinkFallbackTabIndex', full_name='Browse.BrowseResponse.quickLinkFallbackTabIndex', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='survey', full_name='Browse.BrowseResponse.survey', index=12,
      number=13, type=11, cpp_type=10, label=1,
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
  serialized_start=267,
  serialized_end=659,
)


_BROWSETAB = _descriptor.Descriptor(
  name='BrowseTab',
  full_name='Browse.BrowseTab',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='Browse.BrowseTab.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='serverLogsCookie', full_name='Browse.BrowseTab.serverLogsCookie', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='listUrl', full_name='Browse.BrowseTab.listUrl', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='category', full_name='Browse.BrowseTab.category', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=661,
  serialized_end=768,
)


_BROWSELINK = _descriptor.Descriptor(
  name='BrowseLink',
  full_name='Browse.BrowseLink',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Browse.BrowseLink.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dataUrl', full_name='Browse.BrowseLink.dataUrl', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='serverLogsCookie', full_name='Browse.BrowseLink.serverLogsCookie', index=2,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=770,
  serialized_end=839,
)

_QUICKLINK.fields_by_name['image'].message_type = common__pb2._IMAGE
_QUICKLINK.fields_by_name['link'].message_type = resolve__link__pb2._RESOLVEDLINK
_BROWSERESPONSE.fields_by_name['category'].message_type = _BROWSELINK
_BROWSERESPONSE.fields_by_name['breadcrumb'].message_type = _BROWSELINK
_BROWSERESPONSE.fields_by_name['quickLink'].message_type = _QUICKLINK
_BROWSERESPONSE.fields_by_name['browseTab'].message_type = _BROWSETAB
_BROWSERESPONSE.fields_by_name['survey'].message_type = play__survey__pb2._SURVEY
_BROWSETAB.fields_by_name['category'].message_type = _BROWSELINK
DESCRIPTOR.message_types_by_name['QuickLink'] = _QUICKLINK
DESCRIPTOR.message_types_by_name['BrowseResponse'] = _BROWSERESPONSE
DESCRIPTOR.message_types_by_name['BrowseTab'] = _BROWSETAB
DESCRIPTOR.message_types_by_name['BrowseLink'] = _BROWSELINK

QuickLink = _reflection.GeneratedProtocolMessageType('QuickLink', (_message.Message,), dict(
  DESCRIPTOR = _QUICKLINK,
  __module__ = 'browse_pb2'
  # @@protoc_insertion_point(class_scope:Browse.QuickLink)
  ))
_sym_db.RegisterMessage(QuickLink)

BrowseResponse = _reflection.GeneratedProtocolMessageType('BrowseResponse', (_message.Message,), dict(
  DESCRIPTOR = _BROWSERESPONSE,
  __module__ = 'browse_pb2'
  # @@protoc_insertion_point(class_scope:Browse.BrowseResponse)
  ))
_sym_db.RegisterMessage(BrowseResponse)

BrowseTab = _reflection.GeneratedProtocolMessageType('BrowseTab', (_message.Message,), dict(
  DESCRIPTOR = _BROWSETAB,
  __module__ = 'browse_pb2'
  # @@protoc_insertion_point(class_scope:Browse.BrowseTab)
  ))
_sym_db.RegisterMessage(BrowseTab)

BrowseLink = _reflection.GeneratedProtocolMessageType('BrowseLink', (_message.Message,), dict(
  DESCRIPTOR = _BROWSELINK,
  __module__ = 'browse_pb2'
  # @@protoc_insertion_point(class_scope:Browse.BrowseLink)
  ))
_sym_db.RegisterMessage(BrowseLink)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n com.google.android.finsky.protosB\006Browse'))
# @@protoc_insertion_point(module_scope)
