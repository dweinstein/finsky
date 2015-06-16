# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: android_app_delivery.proto

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
  name='android_app_delivery.proto',
  package='AndroidAppDelivery',
  syntax='proto2',
  serialized_pb=_b('\n\x1a\x61ndroid_app_delivery.proto\x12\x12\x41ndroidAppDelivery\"K\n\x10\x45ncryptionParams\x12\x0f\n\x07version\x18\x01 \x01(\x05\x12\x15\n\rencryptionKey\x18\x02 \x01(\t\x12\x0f\n\x07hmacKey\x18\x03 \x01(\t\"\xd2\x01\n\x11SplitDeliveryData\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x0c\x64ownloadSize\x18\x02 \x01(\x03\x12\x1b\n\x13gzippedDownloadSize\x18\x03 \x01(\x03\x12\x11\n\tsignature\x18\x04 \x01(\t\x12\x13\n\x0b\x64ownloadUrl\x18\x05 \x01(\t\x12\x1a\n\x12gzippedDownloadUrl\x18\x06 \x01(\t\x12:\n\tpatchData\x18\x07 \x01(\x0b\x32\'.AndroidAppDelivery.AndroidAppPatchData\")\n\nHttpCookie\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\x85\x01\n\x13\x41ndroidAppPatchData\x12\x17\n\x0f\x62\x61seVersionCode\x18\x01 \x01(\x05\x12\x15\n\rbaseSignature\x18\x02 \x01(\t\x12\x13\n\x0b\x64ownloadUrl\x18\x03 \x01(\t\x12\x13\n\x0bpatchFormat\x18\x04 \x01(\x05\x12\x14\n\x0cmaxPatchSize\x18\x05 \x01(\x03\"\xeb\x04\n\x16\x41ndroidAppDeliveryData\x12\x14\n\x0c\x64ownloadSize\x18\x01 \x01(\x03\x12\x11\n\tsignature\x18\x02 \x01(\t\x12\x13\n\x0b\x64ownloadUrl\x18\x03 \x01(\t\x12;\n\x0e\x61\x64\x64itionalFile\x18\x04 \x03(\x0b\x32#.AndroidAppDelivery.AppFileMetadata\x12:\n\x12\x64ownloadAuthCookie\x18\x05 \x03(\x0b\x32\x1e.AndroidAppDelivery.HttpCookie\x12\x15\n\rforwardLocked\x18\x06 \x01(\x08\x12\x15\n\rrefundTimeout\x18\x07 \x01(\x03\x12\x17\n\x0fserverInitiated\x18\x08 \x01(\x08\x12%\n\x1dpostInstallRefundWindowMillis\x18\t \x01(\x03\x12\x1c\n\x14immediateStartNeeded\x18\n \x01(\x08\x12:\n\tpatchData\x18\x0b \x01(\x0b\x32\'.AndroidAppDelivery.AndroidAppPatchData\x12>\n\x10\x65ncryptionParams\x18\x0c \x01(\x0b\x32$.AndroidAppDelivery.EncryptionParams\x12\x1a\n\x12gzippedDownloadUrl\x18\r \x01(\t\x12\x1b\n\x13gzippedDownloadSize\x18\x0e \x01(\x03\x12@\n\x11splitDeliveryData\x18\x0f \x03(\x0b\x32%.AndroidAppDelivery.SplitDeliveryData\x12\x17\n\x0finstallLocation\x18\x10 \x01(\x05\"[\n\x0f\x41ppFileMetadata\x12\x10\n\x08\x66ileType\x18\x01 \x01(\x05\x12\x13\n\x0bversionCode\x18\x02 \x01(\x05\x12\x0c\n\x04size\x18\x03 \x01(\x03\x12\x13\n\x0b\x64ownloadUrl\x18\x04 \x01(\tB6\n com.google.android.finsky.protosB\x12\x41ndroidAppDelivery')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ENCRYPTIONPARAMS = _descriptor.Descriptor(
  name='EncryptionParams',
  full_name='AndroidAppDelivery.EncryptionParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='AndroidAppDelivery.EncryptionParams.version', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encryptionKey', full_name='AndroidAppDelivery.EncryptionParams.encryptionKey', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hmacKey', full_name='AndroidAppDelivery.EncryptionParams.hmacKey', index=2,
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
  serialized_start=50,
  serialized_end=125,
)


_SPLITDELIVERYDATA = _descriptor.Descriptor(
  name='SplitDeliveryData',
  full_name='AndroidAppDelivery.SplitDeliveryData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='AndroidAppDelivery.SplitDeliveryData.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='downloadSize', full_name='AndroidAppDelivery.SplitDeliveryData.downloadSize', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gzippedDownloadSize', full_name='AndroidAppDelivery.SplitDeliveryData.gzippedDownloadSize', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signature', full_name='AndroidAppDelivery.SplitDeliveryData.signature', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='downloadUrl', full_name='AndroidAppDelivery.SplitDeliveryData.downloadUrl', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gzippedDownloadUrl', full_name='AndroidAppDelivery.SplitDeliveryData.gzippedDownloadUrl', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='patchData', full_name='AndroidAppDelivery.SplitDeliveryData.patchData', index=6,
      number=7, type=11, cpp_type=10, label=1,
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
  serialized_start=128,
  serialized_end=338,
)


_HTTPCOOKIE = _descriptor.Descriptor(
  name='HttpCookie',
  full_name='AndroidAppDelivery.HttpCookie',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='AndroidAppDelivery.HttpCookie.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='AndroidAppDelivery.HttpCookie.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=340,
  serialized_end=381,
)


_ANDROIDAPPPATCHDATA = _descriptor.Descriptor(
  name='AndroidAppPatchData',
  full_name='AndroidAppDelivery.AndroidAppPatchData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='baseVersionCode', full_name='AndroidAppDelivery.AndroidAppPatchData.baseVersionCode', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='baseSignature', full_name='AndroidAppDelivery.AndroidAppPatchData.baseSignature', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='downloadUrl', full_name='AndroidAppDelivery.AndroidAppPatchData.downloadUrl', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='patchFormat', full_name='AndroidAppDelivery.AndroidAppPatchData.patchFormat', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='maxPatchSize', full_name='AndroidAppDelivery.AndroidAppPatchData.maxPatchSize', index=4,
      number=5, type=3, cpp_type=2, label=1,
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
  serialized_start=384,
  serialized_end=517,
)


_ANDROIDAPPDELIVERYDATA = _descriptor.Descriptor(
  name='AndroidAppDeliveryData',
  full_name='AndroidAppDelivery.AndroidAppDeliveryData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='downloadSize', full_name='AndroidAppDelivery.AndroidAppDeliveryData.downloadSize', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signature', full_name='AndroidAppDelivery.AndroidAppDeliveryData.signature', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='downloadUrl', full_name='AndroidAppDelivery.AndroidAppDeliveryData.downloadUrl', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='additionalFile', full_name='AndroidAppDelivery.AndroidAppDeliveryData.additionalFile', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='downloadAuthCookie', full_name='AndroidAppDelivery.AndroidAppDeliveryData.downloadAuthCookie', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='forwardLocked', full_name='AndroidAppDelivery.AndroidAppDeliveryData.forwardLocked', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='refundTimeout', full_name='AndroidAppDelivery.AndroidAppDeliveryData.refundTimeout', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='serverInitiated', full_name='AndroidAppDelivery.AndroidAppDeliveryData.serverInitiated', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='postInstallRefundWindowMillis', full_name='AndroidAppDelivery.AndroidAppDeliveryData.postInstallRefundWindowMillis', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='immediateStartNeeded', full_name='AndroidAppDelivery.AndroidAppDeliveryData.immediateStartNeeded', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='patchData', full_name='AndroidAppDelivery.AndroidAppDeliveryData.patchData', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encryptionParams', full_name='AndroidAppDelivery.AndroidAppDeliveryData.encryptionParams', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gzippedDownloadUrl', full_name='AndroidAppDelivery.AndroidAppDeliveryData.gzippedDownloadUrl', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gzippedDownloadSize', full_name='AndroidAppDelivery.AndroidAppDeliveryData.gzippedDownloadSize', index=13,
      number=14, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='splitDeliveryData', full_name='AndroidAppDelivery.AndroidAppDeliveryData.splitDeliveryData', index=14,
      number=15, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='installLocation', full_name='AndroidAppDelivery.AndroidAppDeliveryData.installLocation', index=15,
      number=16, type=5, cpp_type=1, label=1,
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
  serialized_start=520,
  serialized_end=1139,
)


_APPFILEMETADATA = _descriptor.Descriptor(
  name='AppFileMetadata',
  full_name='AndroidAppDelivery.AppFileMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fileType', full_name='AndroidAppDelivery.AppFileMetadata.fileType', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='versionCode', full_name='AndroidAppDelivery.AppFileMetadata.versionCode', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='size', full_name='AndroidAppDelivery.AppFileMetadata.size', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='downloadUrl', full_name='AndroidAppDelivery.AppFileMetadata.downloadUrl', index=3,
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
  serialized_start=1141,
  serialized_end=1232,
)

_SPLITDELIVERYDATA.fields_by_name['patchData'].message_type = _ANDROIDAPPPATCHDATA
_ANDROIDAPPDELIVERYDATA.fields_by_name['additionalFile'].message_type = _APPFILEMETADATA
_ANDROIDAPPDELIVERYDATA.fields_by_name['downloadAuthCookie'].message_type = _HTTPCOOKIE
_ANDROIDAPPDELIVERYDATA.fields_by_name['patchData'].message_type = _ANDROIDAPPPATCHDATA
_ANDROIDAPPDELIVERYDATA.fields_by_name['encryptionParams'].message_type = _ENCRYPTIONPARAMS
_ANDROIDAPPDELIVERYDATA.fields_by_name['splitDeliveryData'].message_type = _SPLITDELIVERYDATA
DESCRIPTOR.message_types_by_name['EncryptionParams'] = _ENCRYPTIONPARAMS
DESCRIPTOR.message_types_by_name['SplitDeliveryData'] = _SPLITDELIVERYDATA
DESCRIPTOR.message_types_by_name['HttpCookie'] = _HTTPCOOKIE
DESCRIPTOR.message_types_by_name['AndroidAppPatchData'] = _ANDROIDAPPPATCHDATA
DESCRIPTOR.message_types_by_name['AndroidAppDeliveryData'] = _ANDROIDAPPDELIVERYDATA
DESCRIPTOR.message_types_by_name['AppFileMetadata'] = _APPFILEMETADATA

EncryptionParams = _reflection.GeneratedProtocolMessageType('EncryptionParams', (_message.Message,), dict(
  DESCRIPTOR = _ENCRYPTIONPARAMS,
  __module__ = 'android_app_delivery_pb2'
  # @@protoc_insertion_point(class_scope:AndroidAppDelivery.EncryptionParams)
  ))
_sym_db.RegisterMessage(EncryptionParams)

SplitDeliveryData = _reflection.GeneratedProtocolMessageType('SplitDeliveryData', (_message.Message,), dict(
  DESCRIPTOR = _SPLITDELIVERYDATA,
  __module__ = 'android_app_delivery_pb2'
  # @@protoc_insertion_point(class_scope:AndroidAppDelivery.SplitDeliveryData)
  ))
_sym_db.RegisterMessage(SplitDeliveryData)

HttpCookie = _reflection.GeneratedProtocolMessageType('HttpCookie', (_message.Message,), dict(
  DESCRIPTOR = _HTTPCOOKIE,
  __module__ = 'android_app_delivery_pb2'
  # @@protoc_insertion_point(class_scope:AndroidAppDelivery.HttpCookie)
  ))
_sym_db.RegisterMessage(HttpCookie)

AndroidAppPatchData = _reflection.GeneratedProtocolMessageType('AndroidAppPatchData', (_message.Message,), dict(
  DESCRIPTOR = _ANDROIDAPPPATCHDATA,
  __module__ = 'android_app_delivery_pb2'
  # @@protoc_insertion_point(class_scope:AndroidAppDelivery.AndroidAppPatchData)
  ))
_sym_db.RegisterMessage(AndroidAppPatchData)

AndroidAppDeliveryData = _reflection.GeneratedProtocolMessageType('AndroidAppDeliveryData', (_message.Message,), dict(
  DESCRIPTOR = _ANDROIDAPPDELIVERYDATA,
  __module__ = 'android_app_delivery_pb2'
  # @@protoc_insertion_point(class_scope:AndroidAppDelivery.AndroidAppDeliveryData)
  ))
_sym_db.RegisterMessage(AndroidAppDeliveryData)

AppFileMetadata = _reflection.GeneratedProtocolMessageType('AppFileMetadata', (_message.Message,), dict(
  DESCRIPTOR = _APPFILEMETADATA,
  __module__ = 'android_app_delivery_pb2'
  # @@protoc_insertion_point(class_scope:AndroidAppDelivery.AppFileMetadata)
  ))
_sym_db.RegisterMessage(AppFileMetadata)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n com.google.android.finsky.protosB\022AndroidAppDelivery'))
# @@protoc_insertion_point(module_scope)
