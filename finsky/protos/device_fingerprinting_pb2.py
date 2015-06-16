# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: device_fingerprinting.proto

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
  name='device_fingerprinting.proto',
  package='DeviceFingerprinting',
  syntax='proto2',
  serialized_pb=_b('\n\x1b\x64\x65vice_fingerprinting.proto\x12\x14\x44\x65viceFingerprinting\"\x91\t\n\x14\x44\x65viceFingerprinting\x12\x41\n\x06parsed\x18\x02 \x01(\x0b\x32\x31.DeviceFingerprinting.DeviceFingerprinting.Parsed\x1a\xb5\x08\n\x06Parsed\x12P\n\nproperties\x18\x01 \x01(\x0b\x32<.DeviceFingerprinting.DeviceFingerprinting.Parsed.Properties\x12\x46\n\x05state\x18\x02 \x01(\x0b\x32\x37.DeviceFingerprinting.DeviceFingerprinting.Parsed.State\x1a\xfd\x04\n\x05State\x12^\n\x11installedPackages\x18\x01 \x03(\x0b\x32\x43.DeviceFingerprinting.DeviceFingerprinting.Parsed.State.PackageInfo\x12\x15\n\remailAccounts\x18\x02 \x03(\t\x12\x16\n\x0epercentBattery\x18\x03 \x01(\x05\x12\x17\n\x0fgmtOffsetMillis\x18\x04 \x01(\x03\x12Y\n\x0flastGpsLocation\x18\x06 \x01(\x0b\x32@.DeviceFingerprinting.DeviceFingerprinting.Parsed.State.Location\x12\x11\n\tdevModeOn\x18\x07 \x01(\x08\x12\x1d\n\x15nonPlayInstallAllowed\x18\x08 \x01(\x08\x12\x10\n\x08language\x18\t \x01(\t\x12\x0e\n\x06ipAddr\x18\n \x03(\t\x12\x0e\n\x06locale\x18\x0b \x01(\t\x12\x14\n\x0c\x63\x65llOperator\x18\x0e \x01(\t\x12\x13\n\x0bsimOperator\x18\x0f \x01(\t\x1a\x65\n\x08Location\x12\x10\n\x08\x61ltitude\x18\x01 \x01(\x01\x12\x10\n\x08latitude\x18\x02 \x01(\x01\x12\x11\n\tlongitude\x18\x03 \x01(\x01\x12\x10\n\x08\x61\x63\x63uracy\x18\x04 \x01(\x02\x12\x10\n\x08timeInMs\x18\x05 \x01(\x01\x1a{\n\x0bPackageInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0bversionCode\x18\x02 \x01(\t\x12\x16\n\x0elastUpdateTime\x18\x03 \x01(\x03\x12\x18\n\x10\x66irstInstallTime\x18\x04 \x01(\x03\x12\x17\n\x0finstallLocation\x18\x05 \x01(\t\x1a\x90\x02\n\nProperties\x12\x17\n\x0foperatingSystem\x18\x01 \x01(\x05\x12\x0c\n\x04imei\x18\x02 \x01(\t\x12\x0c\n\x04meid\x18\x03 \x01(\t\x12\x0b\n\x03\x65sn\x18\x05 \x01(\t\x12\x13\n\x0bphoneNumber\x18\x06 \x01(\t\x12\x11\n\tandroidId\x18\x07 \x01(\x03\x12\x12\n\ndeviceName\x18\t \x01(\t\x12\x13\n\x0bproductName\x18\n \x01(\t\x12\x11\n\tmodelName\x18\x0b \x01(\t\x12\x14\n\x0cmanufacturer\x18\x0c \x01(\t\x12\x18\n\x10\x62uildFingerprint\x18\r \x01(\t\x12\x11\n\tosVersion\x18\x0f \x01(\t\x12\x19\n\x11\x61ndroidBuildBrand\x18\x15 \x01(\tB-\n\x13paymentfraud.mobileB\x14\x44\x65viceFingerprintingP\x01')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_DEVICEFINGERPRINTING_PARSED_STATE_LOCATION = _descriptor.Descriptor(
  name='Location',
  full_name='DeviceFingerprinting.DeviceFingerprinting.Parsed.State.Location',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='altitude', full_name='DeviceFingerprinting.DeviceFingerprinting.Parsed.State.Location.altitude', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='DeviceFingerprinting.DeviceFingerprinting.Parsed.State.Location.latitude', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='DeviceFingerprinting.DeviceFingerprinting.Parsed.State.Location.longitude', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='accuracy', full_name='DeviceFingerprinting.DeviceFingerprinting.Parsed.State.Location.accuracy', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timeInMs', full_name='DeviceFingerprinting.DeviceFingerprinting.Parsed.State.Location.timeInMs', index=4,
      number=5, type=1, cpp_type=5, label=1,
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
  serialized_start=722,
  serialized_end=823,
)

_DEVICEFINGERPRINTING_PARSED_STATE_PACKAGEINFO = _descriptor.Descriptor(
  name='PackageInfo',
  full_name='DeviceFingerprinting.DeviceFingerprinting.Parsed.State.PackageInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='DeviceFingerprinting.DeviceFingerprinting.Parsed.State.PackageInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='versionCode', full_name='DeviceFingerprinting.DeviceFingerprinting.Parsed.State.PackageInfo.versionCode', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lastUpdateTime', full_name='DeviceFingerprinting.DeviceFingerprinting.Parsed.State.PackageInfo.lastUpdateTime', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='firstInstallTime', full_name='DeviceFingerprinting.DeviceFingerprinting.Parsed.State.PackageInfo.firstInstallTime', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='installLocation', full_name='DeviceFingerprinting.DeviceFingerprinting.Parsed.State.PackageInfo.installLocation', index=4,
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
  serialized_start=825,
  serialized_end=948,
)

_DEVICEFINGERPRINTING_PARSED_STATE = _descriptor.Descriptor(
  name='State',
  full_name='DeviceFingerprinting.DeviceFingerprinting.Parsed.State',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='installedPackages', full_name='DeviceFingerprinting.DeviceFingerprinting.Parsed.State.installedPackages', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='emailAccounts', full_name='DeviceFingerprinting.DeviceFingerprinting.Parsed.State.emailAccounts', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='percentBattery', full_name='DeviceFingerprinting.DeviceFingerprinting.Parsed.State.percentBattery', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gmtOffsetMillis', full_name='DeviceFingerprinting.DeviceFingerprinting.Parsed.State.gmtOffsetMillis', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lastGpsLocation', full_name='DeviceFingerprinting.DeviceFingerprinting.Parsed.State.lastGpsLocation', index=4,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='devModeOn', full_name='DeviceFingerprinting.DeviceFingerprinting.Parsed.State.devModeOn', index=5,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nonPlayInstallAllowed', full_name='DeviceFingerprinting.DeviceFingerprinting.Parsed.State.nonPlayInstallAllowed', index=6,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='language', full_name='DeviceFingerprinting.DeviceFingerprinting.Parsed.State.language', index=7,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ipAddr', full_name='DeviceFingerprinting.DeviceFingerprinting.Parsed.State.ipAddr', index=8,
      number=10, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='locale', full_name='DeviceFingerprinting.DeviceFingerprinting.Parsed.State.locale', index=9,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cellOperator', full_name='DeviceFingerprinting.DeviceFingerprinting.Parsed.State.cellOperator', index=10,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='simOperator', full_name='DeviceFingerprinting.DeviceFingerprinting.Parsed.State.simOperator', index=11,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_DEVICEFINGERPRINTING_PARSED_STATE_LOCATION, _DEVICEFINGERPRINTING_PARSED_STATE_PACKAGEINFO, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=311,
  serialized_end=948,
)

_DEVICEFINGERPRINTING_PARSED_PROPERTIES = _descriptor.Descriptor(
  name='Properties',
  full_name='DeviceFingerprinting.DeviceFingerprinting.Parsed.Properties',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='operatingSystem', full_name='DeviceFingerprinting.DeviceFingerprinting.Parsed.Properties.operatingSystem', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='imei', full_name='DeviceFingerprinting.DeviceFingerprinting.Parsed.Properties.imei', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='meid', full_name='DeviceFingerprinting.DeviceFingerprinting.Parsed.Properties.meid', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='esn', full_name='DeviceFingerprinting.DeviceFingerprinting.Parsed.Properties.esn', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='phoneNumber', full_name='DeviceFingerprinting.DeviceFingerprinting.Parsed.Properties.phoneNumber', index=4,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='androidId', full_name='DeviceFingerprinting.DeviceFingerprinting.Parsed.Properties.androidId', index=5,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deviceName', full_name='DeviceFingerprinting.DeviceFingerprinting.Parsed.Properties.deviceName', index=6,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='productName', full_name='DeviceFingerprinting.DeviceFingerprinting.Parsed.Properties.productName', index=7,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='modelName', full_name='DeviceFingerprinting.DeviceFingerprinting.Parsed.Properties.modelName', index=8,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='manufacturer', full_name='DeviceFingerprinting.DeviceFingerprinting.Parsed.Properties.manufacturer', index=9,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='buildFingerprint', full_name='DeviceFingerprinting.DeviceFingerprinting.Parsed.Properties.buildFingerprint', index=10,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='osVersion', full_name='DeviceFingerprinting.DeviceFingerprinting.Parsed.Properties.osVersion', index=11,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='androidBuildBrand', full_name='DeviceFingerprinting.DeviceFingerprinting.Parsed.Properties.androidBuildBrand', index=12,
      number=21, type=9, cpp_type=9, label=1,
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
  serialized_end=1223,
)

_DEVICEFINGERPRINTING_PARSED = _descriptor.Descriptor(
  name='Parsed',
  full_name='DeviceFingerprinting.DeviceFingerprinting.Parsed',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='properties', full_name='DeviceFingerprinting.DeviceFingerprinting.Parsed.properties', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='state', full_name='DeviceFingerprinting.DeviceFingerprinting.Parsed.state', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_DEVICEFINGERPRINTING_PARSED_STATE, _DEVICEFINGERPRINTING_PARSED_PROPERTIES, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=146,
  serialized_end=1223,
)

_DEVICEFINGERPRINTING = _descriptor.Descriptor(
  name='DeviceFingerprinting',
  full_name='DeviceFingerprinting.DeviceFingerprinting',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parsed', full_name='DeviceFingerprinting.DeviceFingerprinting.parsed', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_DEVICEFINGERPRINTING_PARSED, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=1223,
)

_DEVICEFINGERPRINTING_PARSED_STATE_LOCATION.containing_type = _DEVICEFINGERPRINTING_PARSED_STATE
_DEVICEFINGERPRINTING_PARSED_STATE_PACKAGEINFO.containing_type = _DEVICEFINGERPRINTING_PARSED_STATE
_DEVICEFINGERPRINTING_PARSED_STATE.fields_by_name['installedPackages'].message_type = _DEVICEFINGERPRINTING_PARSED_STATE_PACKAGEINFO
_DEVICEFINGERPRINTING_PARSED_STATE.fields_by_name['lastGpsLocation'].message_type = _DEVICEFINGERPRINTING_PARSED_STATE_LOCATION
_DEVICEFINGERPRINTING_PARSED_STATE.containing_type = _DEVICEFINGERPRINTING_PARSED
_DEVICEFINGERPRINTING_PARSED_PROPERTIES.containing_type = _DEVICEFINGERPRINTING_PARSED
_DEVICEFINGERPRINTING_PARSED.fields_by_name['properties'].message_type = _DEVICEFINGERPRINTING_PARSED_PROPERTIES
_DEVICEFINGERPRINTING_PARSED.fields_by_name['state'].message_type = _DEVICEFINGERPRINTING_PARSED_STATE
_DEVICEFINGERPRINTING_PARSED.containing_type = _DEVICEFINGERPRINTING
_DEVICEFINGERPRINTING.fields_by_name['parsed'].message_type = _DEVICEFINGERPRINTING_PARSED
DESCRIPTOR.message_types_by_name['DeviceFingerprinting'] = _DEVICEFINGERPRINTING

DeviceFingerprinting = _reflection.GeneratedProtocolMessageType('DeviceFingerprinting', (_message.Message,), dict(

  Parsed = _reflection.GeneratedProtocolMessageType('Parsed', (_message.Message,), dict(

    State = _reflection.GeneratedProtocolMessageType('State', (_message.Message,), dict(

      Location = _reflection.GeneratedProtocolMessageType('Location', (_message.Message,), dict(
        DESCRIPTOR = _DEVICEFINGERPRINTING_PARSED_STATE_LOCATION,
        __module__ = 'device_fingerprinting_pb2'
        # @@protoc_insertion_point(class_scope:DeviceFingerprinting.DeviceFingerprinting.Parsed.State.Location)
        ))
      ,

      PackageInfo = _reflection.GeneratedProtocolMessageType('PackageInfo', (_message.Message,), dict(
        DESCRIPTOR = _DEVICEFINGERPRINTING_PARSED_STATE_PACKAGEINFO,
        __module__ = 'device_fingerprinting_pb2'
        # @@protoc_insertion_point(class_scope:DeviceFingerprinting.DeviceFingerprinting.Parsed.State.PackageInfo)
        ))
      ,
      DESCRIPTOR = _DEVICEFINGERPRINTING_PARSED_STATE,
      __module__ = 'device_fingerprinting_pb2'
      # @@protoc_insertion_point(class_scope:DeviceFingerprinting.DeviceFingerprinting.Parsed.State)
      ))
    ,

    Properties = _reflection.GeneratedProtocolMessageType('Properties', (_message.Message,), dict(
      DESCRIPTOR = _DEVICEFINGERPRINTING_PARSED_PROPERTIES,
      __module__ = 'device_fingerprinting_pb2'
      # @@protoc_insertion_point(class_scope:DeviceFingerprinting.DeviceFingerprinting.Parsed.Properties)
      ))
    ,
    DESCRIPTOR = _DEVICEFINGERPRINTING_PARSED,
    __module__ = 'device_fingerprinting_pb2'
    # @@protoc_insertion_point(class_scope:DeviceFingerprinting.DeviceFingerprinting.Parsed)
    ))
  ,
  DESCRIPTOR = _DEVICEFINGERPRINTING,
  __module__ = 'device_fingerprinting_pb2'
  # @@protoc_insertion_point(class_scope:DeviceFingerprinting.DeviceFingerprinting)
  ))
_sym_db.RegisterMessage(DeviceFingerprinting)
_sym_db.RegisterMessage(DeviceFingerprinting.Parsed)
_sym_db.RegisterMessage(DeviceFingerprinting.Parsed.State)
_sym_db.RegisterMessage(DeviceFingerprinting.Parsed.State.Location)
_sym_db.RegisterMessage(DeviceFingerprinting.Parsed.State.PackageInfo)
_sym_db.RegisterMessage(DeviceFingerprinting.Parsed.Properties)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\023paymentfraud.mobileB\024DeviceFingerprintingP\001'))
# @@protoc_insertion_point(module_scope)
