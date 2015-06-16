# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: credit_card.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import image_with_caption_outer_class_pb2 as image__with__caption__outer__class__pb2
import legal_message_set_outer_class_pb2 as legal__message__set__outer__class__pb2
import address_form_outer_class_pb2 as address__form__outer__class__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='credit_card.proto',
  package='CreditCard',
  syntax='proto2',
  serialized_pb=_b('\n\x11\x63redit_card.proto\x12\nCreditCard\x1a$image_with_caption_outer_class.proto\x1a#legal_message_set_outer_class.proto\x1a\x1e\x61\x64\x64ress_form_outer_class.proto\"\xd7\x02\n\x1c\x43reditCardExpirationDateForm\x12\x11\n\tcardLabel\x18\x02 \x01(\t\x12\x11\n\tcvcLength\x18\x03 \x01(\x05\x12\x10\n\x08minMonth\x18\x04 \x01(\x05\x12\x0f\n\x07minYear\x18\x05 \x01(\x05\x12\x10\n\x08maxMonth\x18\x06 \x01(\x05\x12\x0f\n\x07maxYear\x18\x07 \x01(\x05\x12\n\n\x02id\x18\x08 \x01(\t\x12:\n\x04icon\x18\t \x01(\x0b\x32,.ImageWithCaptionOuterClass.ImageWithCaption\x12\x13\n\x0bhiddenField\x18\n \x03(\x05\x12\x42\n\x0c\x63vcHintImage\x18\x0b \x01(\x0b\x32,.ImageWithCaptionOuterClass.ImageWithCaption\x12\x13\n\x0b\x63vcHintText\x18\x0c \x01(\t\x12\x15\n\rcvcHintHeader\x18\r \x01(\t\"\xe1\x03\n\x0e\x43reditCardForm\x12:\n\x0e\x62illingAddress\x18\x02 \x01(\x0b\x32\".AddressFormOuterClass.AddressForm\x12\x35\n\x0cinitialValue\x18\x03 \x01(\x0b\x32\x1f.CreditCard.CreditCardFormValue\x12\x41\n\rlegalMessages\x18\x04 \x01(\x0b\x32*.LegalMessageSetOuterClass.LegalMessageSet\x12\n\n\x02id\x18\x05 \x01(\t\x12-\n\x0f\x61llowedCardType\x18\x06 \x03(\x0b\x32\x14.CreditCard.CardType\x12(\n\ninvalidBin\x18\x07 \x03(\x0b\x32\x14.CreditCard.BinRange\x12\x1a\n\x12minExpirationMonth\x18\x08 \x01(\x05\x12\x19\n\x11minExpirationYear\x18\t \x01(\x05\x12\x1a\n\x12maxExpirationMonth\x18\n \x01(\x05\x12\x19\n\x11maxExpirationYear\x18\x0b \x01(\x05\x12\x18\n\x10\x61llowCameraInput\x18\x0c \x01(\x08\x12\r\n\x05title\x18\r \x01(\t\x12\x1d\n\x15\x63\x61meraInputPreference\x18\x0f \x01(\x05\"\x8d\x02\n\x13\x43reditCardFormValue\x12\x12\n\ncardNumber\x18\x01 \x01(\t\x12\x0b\n\x03\x63vc\x18\x02 \x01(\t\x12\x17\n\x0f\x65xpirationMonth\x18\x03 \x01(\x05\x12\x16\n\x0e\x65xpirationYear\x18\x04 \x01(\x05\x12\x16\n\x0elastFourDigits\x18\x06 \x01(\t\x12\x16\n\x0e\x63\x61rdholderName\x18\t \x01(\t\x12?\n\x0e\x62illingAddress\x18\n \x01(\x0b\x32\'.AddressFormOuterClass.AddressFormValue\x12\x11\n\ttypeToken\x18\x0b \x01(\x0c\x12\x14\n\x0clegalDocData\x18\x0c \x01(\t\x12\n\n\x02id\x18\r \x01(\t\"\x84\x02\n\x08\x43\x61rdType\x12&\n\x08\x62inRange\x18\x01 \x03(\x0b\x32\x14.CreditCard.BinRange\x12\x11\n\tcvcLength\x18\x03 \x01(\x05\x12\x11\n\ttypeToken\x18\x04 \x01(\x0c\x12\x13\n\x0b\x63vcHintText\x18\x07 \x01(\t\x12\x15\n\rcvcHintHeader\x18\x08 \x01(\t\x12:\n\x04icon\x18\t \x01(\x0b\x32,.ImageWithCaptionOuterClass.ImageWithCaption\x12\x42\n\x0c\x63vcHintImage\x18\x0b \x01(\x0b\x32,.ImageWithCaptionOuterClass.ImageWithCaption\"m\n\x08\x42inRange\x12\r\n\x05start\x18\x01 \x01(\t\x12\x0b\n\x03\x65nd\x18\x02 \x01(\t\x12\x18\n\x10\x63\x61rdNumberLength\x18\x03 \x01(\x05\x12\x15\n\rdigitGrouping\x18\x04 \x03(\x05\x12\x14\n\x0c\x65rrorMessage\x18\x05 \x01(\t\"S\n!CreditCardExpirationDateFormValue\x12\x10\n\x08newMonth\x18\x01 \x01(\x05\x12\x0f\n\x07newYear\x18\x02 \x01(\x05\x12\x0b\n\x03\x63vc\x18\x03 \x01(\tBd\nVcom.google.commerce.payments.orchestration.proto.ui.common.components.instrument.typesB\nCreditCard')
  ,
  dependencies=[image__with__caption__outer__class__pb2.DESCRIPTOR,legal__message__set__outer__class__pb2.DESCRIPTOR,address__form__outer__class__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CREDITCARDEXPIRATIONDATEFORM = _descriptor.Descriptor(
  name='CreditCardExpirationDateForm',
  full_name='CreditCard.CreditCardExpirationDateForm',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cardLabel', full_name='CreditCard.CreditCardExpirationDateForm.cardLabel', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cvcLength', full_name='CreditCard.CreditCardExpirationDateForm.cvcLength', index=1,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='minMonth', full_name='CreditCard.CreditCardExpirationDateForm.minMonth', index=2,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='minYear', full_name='CreditCard.CreditCardExpirationDateForm.minYear', index=3,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='maxMonth', full_name='CreditCard.CreditCardExpirationDateForm.maxMonth', index=4,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='maxYear', full_name='CreditCard.CreditCardExpirationDateForm.maxYear', index=5,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='CreditCard.CreditCardExpirationDateForm.id', index=6,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='icon', full_name='CreditCard.CreditCardExpirationDateForm.icon', index=7,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hiddenField', full_name='CreditCard.CreditCardExpirationDateForm.hiddenField', index=8,
      number=10, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cvcHintImage', full_name='CreditCard.CreditCardExpirationDateForm.cvcHintImage', index=9,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cvcHintText', full_name='CreditCard.CreditCardExpirationDateForm.cvcHintText', index=10,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cvcHintHeader', full_name='CreditCard.CreditCardExpirationDateForm.cvcHintHeader', index=11,
      number=13, type=9, cpp_type=9, label=1,
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
  serialized_start=141,
  serialized_end=484,
)


_CREDITCARDFORM = _descriptor.Descriptor(
  name='CreditCardForm',
  full_name='CreditCard.CreditCardForm',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='billingAddress', full_name='CreditCard.CreditCardForm.billingAddress', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='initialValue', full_name='CreditCard.CreditCardForm.initialValue', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='legalMessages', full_name='CreditCard.CreditCardForm.legalMessages', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='CreditCard.CreditCardForm.id', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='allowedCardType', full_name='CreditCard.CreditCardForm.allowedCardType', index=4,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='invalidBin', full_name='CreditCard.CreditCardForm.invalidBin', index=5,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='minExpirationMonth', full_name='CreditCard.CreditCardForm.minExpirationMonth', index=6,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='minExpirationYear', full_name='CreditCard.CreditCardForm.minExpirationYear', index=7,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='maxExpirationMonth', full_name='CreditCard.CreditCardForm.maxExpirationMonth', index=8,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='maxExpirationYear', full_name='CreditCard.CreditCardForm.maxExpirationYear', index=9,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='allowCameraInput', full_name='CreditCard.CreditCardForm.allowCameraInput', index=10,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='title', full_name='CreditCard.CreditCardForm.title', index=11,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cameraInputPreference', full_name='CreditCard.CreditCardForm.cameraInputPreference', index=12,
      number=15, type=5, cpp_type=1, label=1,
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
  serialized_start=487,
  serialized_end=968,
)


_CREDITCARDFORMVALUE = _descriptor.Descriptor(
  name='CreditCardFormValue',
  full_name='CreditCard.CreditCardFormValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cardNumber', full_name='CreditCard.CreditCardFormValue.cardNumber', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cvc', full_name='CreditCard.CreditCardFormValue.cvc', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='expirationMonth', full_name='CreditCard.CreditCardFormValue.expirationMonth', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='expirationYear', full_name='CreditCard.CreditCardFormValue.expirationYear', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lastFourDigits', full_name='CreditCard.CreditCardFormValue.lastFourDigits', index=4,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cardholderName', full_name='CreditCard.CreditCardFormValue.cardholderName', index=5,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='billingAddress', full_name='CreditCard.CreditCardFormValue.billingAddress', index=6,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='typeToken', full_name='CreditCard.CreditCardFormValue.typeToken', index=7,
      number=11, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='legalDocData', full_name='CreditCard.CreditCardFormValue.legalDocData', index=8,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='CreditCard.CreditCardFormValue.id', index=9,
      number=13, type=9, cpp_type=9, label=1,
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
  serialized_start=971,
  serialized_end=1240,
)


_CARDTYPE = _descriptor.Descriptor(
  name='CardType',
  full_name='CreditCard.CardType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='binRange', full_name='CreditCard.CardType.binRange', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cvcLength', full_name='CreditCard.CardType.cvcLength', index=1,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='typeToken', full_name='CreditCard.CardType.typeToken', index=2,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cvcHintText', full_name='CreditCard.CardType.cvcHintText', index=3,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cvcHintHeader', full_name='CreditCard.CardType.cvcHintHeader', index=4,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='icon', full_name='CreditCard.CardType.icon', index=5,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cvcHintImage', full_name='CreditCard.CardType.cvcHintImage', index=6,
      number=11, type=11, cpp_type=10, label=1,
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
  serialized_start=1243,
  serialized_end=1503,
)


_BINRANGE = _descriptor.Descriptor(
  name='BinRange',
  full_name='CreditCard.BinRange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='CreditCard.BinRange.start', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end', full_name='CreditCard.BinRange.end', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cardNumberLength', full_name='CreditCard.BinRange.cardNumberLength', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='digitGrouping', full_name='CreditCard.BinRange.digitGrouping', index=3,
      number=4, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='errorMessage', full_name='CreditCard.BinRange.errorMessage', index=4,
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
  serialized_start=1505,
  serialized_end=1614,
)


_CREDITCARDEXPIRATIONDATEFORMVALUE = _descriptor.Descriptor(
  name='CreditCardExpirationDateFormValue',
  full_name='CreditCard.CreditCardExpirationDateFormValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='newMonth', full_name='CreditCard.CreditCardExpirationDateFormValue.newMonth', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='newYear', full_name='CreditCard.CreditCardExpirationDateFormValue.newYear', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cvc', full_name='CreditCard.CreditCardExpirationDateFormValue.cvc', index=2,
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
  serialized_start=1616,
  serialized_end=1699,
)

_CREDITCARDEXPIRATIONDATEFORM.fields_by_name['icon'].message_type = image__with__caption__outer__class__pb2._IMAGEWITHCAPTION
_CREDITCARDEXPIRATIONDATEFORM.fields_by_name['cvcHintImage'].message_type = image__with__caption__outer__class__pb2._IMAGEWITHCAPTION
_CREDITCARDFORM.fields_by_name['billingAddress'].message_type = address__form__outer__class__pb2._ADDRESSFORM
_CREDITCARDFORM.fields_by_name['initialValue'].message_type = _CREDITCARDFORMVALUE
_CREDITCARDFORM.fields_by_name['legalMessages'].message_type = legal__message__set__outer__class__pb2._LEGALMESSAGESET
_CREDITCARDFORM.fields_by_name['allowedCardType'].message_type = _CARDTYPE
_CREDITCARDFORM.fields_by_name['invalidBin'].message_type = _BINRANGE
_CREDITCARDFORMVALUE.fields_by_name['billingAddress'].message_type = address__form__outer__class__pb2._ADDRESSFORMVALUE
_CARDTYPE.fields_by_name['binRange'].message_type = _BINRANGE
_CARDTYPE.fields_by_name['icon'].message_type = image__with__caption__outer__class__pb2._IMAGEWITHCAPTION
_CARDTYPE.fields_by_name['cvcHintImage'].message_type = image__with__caption__outer__class__pb2._IMAGEWITHCAPTION
DESCRIPTOR.message_types_by_name['CreditCardExpirationDateForm'] = _CREDITCARDEXPIRATIONDATEFORM
DESCRIPTOR.message_types_by_name['CreditCardForm'] = _CREDITCARDFORM
DESCRIPTOR.message_types_by_name['CreditCardFormValue'] = _CREDITCARDFORMVALUE
DESCRIPTOR.message_types_by_name['CardType'] = _CARDTYPE
DESCRIPTOR.message_types_by_name['BinRange'] = _BINRANGE
DESCRIPTOR.message_types_by_name['CreditCardExpirationDateFormValue'] = _CREDITCARDEXPIRATIONDATEFORMVALUE

CreditCardExpirationDateForm = _reflection.GeneratedProtocolMessageType('CreditCardExpirationDateForm', (_message.Message,), dict(
  DESCRIPTOR = _CREDITCARDEXPIRATIONDATEFORM,
  __module__ = 'credit_card_pb2'
  # @@protoc_insertion_point(class_scope:CreditCard.CreditCardExpirationDateForm)
  ))
_sym_db.RegisterMessage(CreditCardExpirationDateForm)

CreditCardForm = _reflection.GeneratedProtocolMessageType('CreditCardForm', (_message.Message,), dict(
  DESCRIPTOR = _CREDITCARDFORM,
  __module__ = 'credit_card_pb2'
  # @@protoc_insertion_point(class_scope:CreditCard.CreditCardForm)
  ))
_sym_db.RegisterMessage(CreditCardForm)

CreditCardFormValue = _reflection.GeneratedProtocolMessageType('CreditCardFormValue', (_message.Message,), dict(
  DESCRIPTOR = _CREDITCARDFORMVALUE,
  __module__ = 'credit_card_pb2'
  # @@protoc_insertion_point(class_scope:CreditCard.CreditCardFormValue)
  ))
_sym_db.RegisterMessage(CreditCardFormValue)

CardType = _reflection.GeneratedProtocolMessageType('CardType', (_message.Message,), dict(
  DESCRIPTOR = _CARDTYPE,
  __module__ = 'credit_card_pb2'
  # @@protoc_insertion_point(class_scope:CreditCard.CardType)
  ))
_sym_db.RegisterMessage(CardType)

BinRange = _reflection.GeneratedProtocolMessageType('BinRange', (_message.Message,), dict(
  DESCRIPTOR = _BINRANGE,
  __module__ = 'credit_card_pb2'
  # @@protoc_insertion_point(class_scope:CreditCard.BinRange)
  ))
_sym_db.RegisterMessage(BinRange)

CreditCardExpirationDateFormValue = _reflection.GeneratedProtocolMessageType('CreditCardExpirationDateFormValue', (_message.Message,), dict(
  DESCRIPTOR = _CREDITCARDEXPIRATIONDATEFORMVALUE,
  __module__ = 'credit_card_pb2'
  # @@protoc_insertion_point(class_scope:CreditCard.CreditCardExpirationDateFormValue)
  ))
_sym_db.RegisterMessage(CreditCardExpirationDateFormValue)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\nVcom.google.commerce.payments.orchestration.proto.ui.common.components.instrument.typesB\nCreditCard'))
# @@protoc_insertion_point(module_scope)
