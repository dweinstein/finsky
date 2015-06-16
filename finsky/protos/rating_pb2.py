# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rating.proto

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
  name='rating.proto',
  package='Rating',
  syntax='proto2',
  serialized_pb=_b('\n\x0crating.proto\x12\x06Rating\"\xc1\x02\n\x0f\x41ggregateRating\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12\x12\n\nstarRating\x18\x02 \x01(\x02\x12\x14\n\x0cratingsCount\x18\x03 \x01(\x03\x12\x16\n\x0eoneStarRatings\x18\x04 \x01(\x03\x12\x16\n\x0etwoStarRatings\x18\x05 \x01(\x03\x12\x18\n\x10threeStarRatings\x18\x06 \x01(\x03\x12\x17\n\x0f\x66ourStarRatings\x18\x07 \x01(\x03\x12\x17\n\x0f\x66iveStarRatings\x18\x08 \x01(\x03\x12\x15\n\rthumbsUpCount\x18\t \x01(\x03\x12\x17\n\x0fthumbsDownCount\x18\n \x01(\x03\x12\x14\n\x0c\x63ommentCount\x18\x0b \x01(\x03\x12\x1a\n\x12\x62\x61yesianMeanRating\x18\x0c \x01(\x01\x12\x18\n\x03tip\x18\r \x03(\x0b\x32\x0b.Rating.Tip\"[\n\x03Tip\x12\r\n\x05tipId\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x10\n\x08polarity\x18\x03 \x01(\x05\x12\x13\n\x0breviewCount\x18\x04 \x01(\x03\x12\x10\n\x08language\x18\x05 \x01(\tB*\n com.google.android.finsky.protosB\x06Rating')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_AGGREGATERATING = _descriptor.Descriptor(
  name='AggregateRating',
  full_name='Rating.AggregateRating',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Rating.AggregateRating.type', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='starRating', full_name='Rating.AggregateRating.starRating', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ratingsCount', full_name='Rating.AggregateRating.ratingsCount', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='oneStarRatings', full_name='Rating.AggregateRating.oneStarRatings', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='twoStarRatings', full_name='Rating.AggregateRating.twoStarRatings', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='threeStarRatings', full_name='Rating.AggregateRating.threeStarRatings', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fourStarRatings', full_name='Rating.AggregateRating.fourStarRatings', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fiveStarRatings', full_name='Rating.AggregateRating.fiveStarRatings', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='thumbsUpCount', full_name='Rating.AggregateRating.thumbsUpCount', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='thumbsDownCount', full_name='Rating.AggregateRating.thumbsDownCount', index=9,
      number=10, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='commentCount', full_name='Rating.AggregateRating.commentCount', index=10,
      number=11, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bayesianMeanRating', full_name='Rating.AggregateRating.bayesianMeanRating', index=11,
      number=12, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tip', full_name='Rating.AggregateRating.tip', index=12,
      number=13, type=11, cpp_type=10, label=3,
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
  serialized_start=25,
  serialized_end=346,
)


_TIP = _descriptor.Descriptor(
  name='Tip',
  full_name='Rating.Tip',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tipId', full_name='Rating.Tip.tipId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='text', full_name='Rating.Tip.text', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='polarity', full_name='Rating.Tip.polarity', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reviewCount', full_name='Rating.Tip.reviewCount', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='language', full_name='Rating.Tip.language', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=348,
  serialized_end=439,
)

_AGGREGATERATING.fields_by_name['tip'].message_type = _TIP
DESCRIPTOR.message_types_by_name['AggregateRating'] = _AGGREGATERATING
DESCRIPTOR.message_types_by_name['Tip'] = _TIP

AggregateRating = _reflection.GeneratedProtocolMessageType('AggregateRating', (_message.Message,), dict(
  DESCRIPTOR = _AGGREGATERATING,
  __module__ = 'rating_pb2'
  # @@protoc_insertion_point(class_scope:Rating.AggregateRating)
  ))
_sym_db.RegisterMessage(AggregateRating)

Tip = _reflection.GeneratedProtocolMessageType('Tip', (_message.Message,), dict(
  DESCRIPTOR = _TIP,
  __module__ = 'rating_pb2'
  # @@protoc_insertion_point(class_scope:Rating.Tip)
  ))
_sym_db.RegisterMessage(Tip)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n com.google.android.finsky.protosB\006Rating'))
# @@protoc_insertion_point(module_scope)
