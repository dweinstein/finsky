# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: video_doc_details.proto

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
  name='video_doc_details.proto',
  package='VideoDocDetails',
  syntax='proto2',
  serialized_pb=_b('\n\x17video_doc_details.proto\x12\x0fVideoDocDetails\"W\n\x10TvEpisodeDetails\x12\x18\n\x10parentDetailsUrl\x18\x01 \x01(\t\x12\x14\n\x0c\x65pisodeIndex\x18\x02 \x01(\x05\x12\x13\n\x0breleaseDate\x18\x03 \x01(\t\"\x9e\x01\n\x0fTvSeasonDetails\x12\x18\n\x10parentDetailsUrl\x18\x01 \x01(\t\x12\x13\n\x0bseasonIndex\x18\x02 \x01(\x05\x12\x13\n\x0breleaseDate\x18\x03 \x01(\t\x12\x13\n\x0b\x62roadcaster\x18\x04 \x01(\t\x12\x14\n\x0c\x65pisodeCount\x18\x05 \x01(\x05\x12\x1c\n\x14\x65xpectedEpisodeCount\x18\x06 \x01(\x05\"\xb0\x01\n\x0fVideoRentalTerm\x12\x11\n\tofferType\x18\x01 \x01(\x05\x12\x19\n\x11offerAbbreviation\x18\x02 \x01(\t\x12\x14\n\x0crentalHeader\x18\x03 \x01(\t\x12\x33\n\x04term\x18\x04 \x03(\x0b\x32%.VideoDocDetails.VideoRentalTerm.Term\x1a$\n\x04Term\x12\x0e\n\x06header\x18\x05 \x01(\t\x12\x0c\n\x04\x62ody\x18\x06 \x01(\t\"?\n\x0bVideoCredit\x12\x12\n\ncreditType\x18\x01 \x01(\x05\x12\x0e\n\x06\x63redit\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x03(\t\"]\n\rTvShowDetails\x12\x13\n\x0bseasonCount\x18\x01 \x01(\x05\x12\x11\n\tstartYear\x18\x02 \x01(\x05\x12\x0f\n\x07\x65ndYear\x18\x03 \x01(\x05\x12\x13\n\x0b\x62roadcaster\x18\x04 \x01(\t\"\xbb\x02\n\x0cVideoDetails\x12,\n\x06\x63redit\x18\x01 \x03(\x0b\x32\x1c.VideoDocDetails.VideoCredit\x12\x10\n\x08\x64uration\x18\x02 \x01(\t\x12\x13\n\x0breleaseDate\x18\x03 \x01(\t\x12\x15\n\rcontentRating\x18\x04 \x01(\t\x12\r\n\x05likes\x18\x05 \x01(\x03\x12\x10\n\x08\x64islikes\x18\x06 \x01(\x03\x12\r\n\x05genre\x18\x07 \x03(\t\x12)\n\x07trailer\x18\x08 \x03(\x0b\x32\x18.VideoDocDetails.Trailer\x12\x34\n\nrentalTerm\x18\t \x03(\x0b\x32 .VideoDocDetails.VideoRentalTerm\x12\x15\n\raudioLanguage\x18\n \x03(\t\x12\x17\n\x0f\x63\x61ptionLanguage\x18\x0b \x03(\t\"e\n\x07Trailer\x12\x11\n\ttrailerId\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x14\n\x0cthumbnailUrl\x18\x03 \x01(\t\x12\x10\n\x08watchUrl\x18\x04 \x01(\t\x12\x10\n\x08\x64uration\x18\x05 \x01(\tB3\n com.google.android.finsky.protosB\x0fVideoDocDetails')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_TVEPISODEDETAILS = _descriptor.Descriptor(
  name='TvEpisodeDetails',
  full_name='VideoDocDetails.TvEpisodeDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parentDetailsUrl', full_name='VideoDocDetails.TvEpisodeDetails.parentDetailsUrl', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='episodeIndex', full_name='VideoDocDetails.TvEpisodeDetails.episodeIndex', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='releaseDate', full_name='VideoDocDetails.TvEpisodeDetails.releaseDate', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=44,
  serialized_end=131,
)


_TVSEASONDETAILS = _descriptor.Descriptor(
  name='TvSeasonDetails',
  full_name='VideoDocDetails.TvSeasonDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parentDetailsUrl', full_name='VideoDocDetails.TvSeasonDetails.parentDetailsUrl', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='seasonIndex', full_name='VideoDocDetails.TvSeasonDetails.seasonIndex', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='releaseDate', full_name='VideoDocDetails.TvSeasonDetails.releaseDate', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='broadcaster', full_name='VideoDocDetails.TvSeasonDetails.broadcaster', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='episodeCount', full_name='VideoDocDetails.TvSeasonDetails.episodeCount', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='expectedEpisodeCount', full_name='VideoDocDetails.TvSeasonDetails.expectedEpisodeCount', index=5,
      number=6, type=5, cpp_type=1, label=1,
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
  serialized_start=134,
  serialized_end=292,
)


_VIDEORENTALTERM_TERM = _descriptor.Descriptor(
  name='Term',
  full_name='VideoDocDetails.VideoRentalTerm.Term',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='VideoDocDetails.VideoRentalTerm.Term.header', index=0,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='body', full_name='VideoDocDetails.VideoRentalTerm.Term.body', index=1,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=435,
  serialized_end=471,
)

_VIDEORENTALTERM = _descriptor.Descriptor(
  name='VideoRentalTerm',
  full_name='VideoDocDetails.VideoRentalTerm',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='offerType', full_name='VideoDocDetails.VideoRentalTerm.offerType', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='offerAbbreviation', full_name='VideoDocDetails.VideoRentalTerm.offerAbbreviation', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rentalHeader', full_name='VideoDocDetails.VideoRentalTerm.rentalHeader', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='term', full_name='VideoDocDetails.VideoRentalTerm.term', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_VIDEORENTALTERM_TERM, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=295,
  serialized_end=471,
)


_VIDEOCREDIT = _descriptor.Descriptor(
  name='VideoCredit',
  full_name='VideoDocDetails.VideoCredit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='creditType', full_name='VideoDocDetails.VideoCredit.creditType', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='credit', full_name='VideoDocDetails.VideoCredit.credit', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='VideoDocDetails.VideoCredit.name', index=2,
      number=3, type=9, cpp_type=9, label=3,
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
  serialized_start=473,
  serialized_end=536,
)


_TVSHOWDETAILS = _descriptor.Descriptor(
  name='TvShowDetails',
  full_name='VideoDocDetails.TvShowDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='seasonCount', full_name='VideoDocDetails.TvShowDetails.seasonCount', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='startYear', full_name='VideoDocDetails.TvShowDetails.startYear', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='endYear', full_name='VideoDocDetails.TvShowDetails.endYear', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='broadcaster', full_name='VideoDocDetails.TvShowDetails.broadcaster', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=538,
  serialized_end=631,
)


_VIDEODETAILS = _descriptor.Descriptor(
  name='VideoDetails',
  full_name='VideoDocDetails.VideoDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='credit', full_name='VideoDocDetails.VideoDetails.credit', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='duration', full_name='VideoDocDetails.VideoDetails.duration', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='releaseDate', full_name='VideoDocDetails.VideoDetails.releaseDate', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='contentRating', full_name='VideoDocDetails.VideoDetails.contentRating', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='likes', full_name='VideoDocDetails.VideoDetails.likes', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dislikes', full_name='VideoDocDetails.VideoDetails.dislikes', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='genre', full_name='VideoDocDetails.VideoDetails.genre', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trailer', full_name='VideoDocDetails.VideoDetails.trailer', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rentalTerm', full_name='VideoDocDetails.VideoDetails.rentalTerm', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='audioLanguage', full_name='VideoDocDetails.VideoDetails.audioLanguage', index=9,
      number=10, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='captionLanguage', full_name='VideoDocDetails.VideoDetails.captionLanguage', index=10,
      number=11, type=9, cpp_type=9, label=3,
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
  serialized_start=634,
  serialized_end=949,
)


_TRAILER = _descriptor.Descriptor(
  name='Trailer',
  full_name='VideoDocDetails.Trailer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trailerId', full_name='VideoDocDetails.Trailer.trailerId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='title', full_name='VideoDocDetails.Trailer.title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='thumbnailUrl', full_name='VideoDocDetails.Trailer.thumbnailUrl', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='watchUrl', full_name='VideoDocDetails.Trailer.watchUrl', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='duration', full_name='VideoDocDetails.Trailer.duration', index=4,
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
  serialized_start=951,
  serialized_end=1052,
)

_VIDEORENTALTERM_TERM.containing_type = _VIDEORENTALTERM
_VIDEORENTALTERM.fields_by_name['term'].message_type = _VIDEORENTALTERM_TERM
_VIDEODETAILS.fields_by_name['credit'].message_type = _VIDEOCREDIT
_VIDEODETAILS.fields_by_name['trailer'].message_type = _TRAILER
_VIDEODETAILS.fields_by_name['rentalTerm'].message_type = _VIDEORENTALTERM
DESCRIPTOR.message_types_by_name['TvEpisodeDetails'] = _TVEPISODEDETAILS
DESCRIPTOR.message_types_by_name['TvSeasonDetails'] = _TVSEASONDETAILS
DESCRIPTOR.message_types_by_name['VideoRentalTerm'] = _VIDEORENTALTERM
DESCRIPTOR.message_types_by_name['VideoCredit'] = _VIDEOCREDIT
DESCRIPTOR.message_types_by_name['TvShowDetails'] = _TVSHOWDETAILS
DESCRIPTOR.message_types_by_name['VideoDetails'] = _VIDEODETAILS
DESCRIPTOR.message_types_by_name['Trailer'] = _TRAILER

TvEpisodeDetails = _reflection.GeneratedProtocolMessageType('TvEpisodeDetails', (_message.Message,), dict(
  DESCRIPTOR = _TVEPISODEDETAILS,
  __module__ = 'video_doc_details_pb2'
  # @@protoc_insertion_point(class_scope:VideoDocDetails.TvEpisodeDetails)
  ))
_sym_db.RegisterMessage(TvEpisodeDetails)

TvSeasonDetails = _reflection.GeneratedProtocolMessageType('TvSeasonDetails', (_message.Message,), dict(
  DESCRIPTOR = _TVSEASONDETAILS,
  __module__ = 'video_doc_details_pb2'
  # @@protoc_insertion_point(class_scope:VideoDocDetails.TvSeasonDetails)
  ))
_sym_db.RegisterMessage(TvSeasonDetails)

VideoRentalTerm = _reflection.GeneratedProtocolMessageType('VideoRentalTerm', (_message.Message,), dict(

  Term = _reflection.GeneratedProtocolMessageType('Term', (_message.Message,), dict(
    DESCRIPTOR = _VIDEORENTALTERM_TERM,
    __module__ = 'video_doc_details_pb2'
    # @@protoc_insertion_point(class_scope:VideoDocDetails.VideoRentalTerm.Term)
    ))
  ,
  DESCRIPTOR = _VIDEORENTALTERM,
  __module__ = 'video_doc_details_pb2'
  # @@protoc_insertion_point(class_scope:VideoDocDetails.VideoRentalTerm)
  ))
_sym_db.RegisterMessage(VideoRentalTerm)
_sym_db.RegisterMessage(VideoRentalTerm.Term)

VideoCredit = _reflection.GeneratedProtocolMessageType('VideoCredit', (_message.Message,), dict(
  DESCRIPTOR = _VIDEOCREDIT,
  __module__ = 'video_doc_details_pb2'
  # @@protoc_insertion_point(class_scope:VideoDocDetails.VideoCredit)
  ))
_sym_db.RegisterMessage(VideoCredit)

TvShowDetails = _reflection.GeneratedProtocolMessageType('TvShowDetails', (_message.Message,), dict(
  DESCRIPTOR = _TVSHOWDETAILS,
  __module__ = 'video_doc_details_pb2'
  # @@protoc_insertion_point(class_scope:VideoDocDetails.TvShowDetails)
  ))
_sym_db.RegisterMessage(TvShowDetails)

VideoDetails = _reflection.GeneratedProtocolMessageType('VideoDetails', (_message.Message,), dict(
  DESCRIPTOR = _VIDEODETAILS,
  __module__ = 'video_doc_details_pb2'
  # @@protoc_insertion_point(class_scope:VideoDocDetails.VideoDetails)
  ))
_sym_db.RegisterMessage(VideoDetails)

Trailer = _reflection.GeneratedProtocolMessageType('Trailer', (_message.Message,), dict(
  DESCRIPTOR = _TRAILER,
  __module__ = 'video_doc_details_pb2'
  # @@protoc_insertion_point(class_scope:VideoDocDetails.Trailer)
  ))
_sym_db.RegisterMessage(Trailer)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n com.google.android.finsky.protosB\017VideoDocDetails'))
# @@protoc_insertion_point(module_scope)
