# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: instrosetta/interfaces/light_analysis/monochromator.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='instrosetta/interfaces/light_analysis/monochromator.proto',
  package='instrosetta.interfaces.light_analysis.monochromator',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n9instrosetta/interfaces/light_analysis/monochromator.proto\x12\x33instrosetta.interfaces.light_analysis.monochromator\"m\n\x0e\x43onnectRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rserial_number\x18\x02 \x01(\t\x12\x13\n\x0bserial_port\x18\x03 \x01(\t\x12\x10\n\x08\x62\x61udrate\x18\x04 \x01(\r\x12\x0f\n\x07timeout\x18\x06 \x01(\x02\"\x1f\n\x0f\x43onnectResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\"!\n\x11\x44isconnectRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\"\n\x12\x44isconnectResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\")\n\x19GetWavelengthRangeRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"[\n\x1aGetWavelengthRangeResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07minimum\x18\x02 \x01(\x02\x12\x0f\n\x07maximum\x18\x03 \x01(\x02\x12\r\n\x05units\x18\x04 \x01(\t\"$\n\x14GetWavelengthRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"H\n\x15GetWavelengthResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nwavelength\x18\x02 \x01(\x02\x12\r\n\x05units\x18\x03 \x01(\t\"G\n\x14SetWavelengthRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nwavelength\x18\x02 \x01(\x02\x12\r\n\x05units\x18\x03 \x01(\t\"H\n\x15SetWavelengthResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nwavelength\x18\x02 \x01(\x02\x12\r\n\x05units\x18\x03 \x01(\t\"(\n\x18GetGratingOptionsRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\":\n\x19GetGratingOptionsResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07options\x18\x02 \x03(\r\"!\n\x11GetGratingRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"3\n\x12GetGratingResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07grating\x18\x02 \x01(\r\"2\n\x11SetGratingRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07grating\x18\x02 \x01(\r\"3\n\x12SetGratingResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07grating\x18\x02 \x01(\r2\xd3\n\n\rMonochromator\x12\x96\x01\n\x07\x43onnect\x12\x43.instrosetta.interfaces.light_analysis.monochromator.ConnectRequest\x1a\x44.instrosetta.interfaces.light_analysis.monochromator.ConnectResponse\"\x00\x12\x9f\x01\n\nDisconnect\x12\x46.instrosetta.interfaces.light_analysis.monochromator.DisconnectRequest\x1aG.instrosetta.interfaces.light_analysis.monochromator.DisconnectResponse\"\x00\x12\xb7\x01\n\x12GetWavelengthRange\x12N.instrosetta.interfaces.light_analysis.monochromator.GetWavelengthRangeRequest\x1aO.instrosetta.interfaces.light_analysis.monochromator.GetWavelengthRangeResponse\"\x00\x12\xa8\x01\n\rGetWavelength\x12I.instrosetta.interfaces.light_analysis.monochromator.GetWavelengthRequest\x1aJ.instrosetta.interfaces.light_analysis.monochromator.GetWavelengthResponse\"\x00\x12\xa8\x01\n\rSetWavelength\x12I.instrosetta.interfaces.light_analysis.monochromator.SetWavelengthRequest\x1aJ.instrosetta.interfaces.light_analysis.monochromator.SetWavelengthResponse\"\x00\x12\xb2\x01\n\x0fGetGratingRange\x12M.instrosetta.interfaces.light_analysis.monochromator.GetGratingOptionsRequest\x1aN.instrosetta.interfaces.light_analysis.monochromator.GetGratingOptionsResponse\"\x00\x12\x9f\x01\n\nGetGrating\x12\x46.instrosetta.interfaces.light_analysis.monochromator.GetGratingRequest\x1aG.instrosetta.interfaces.light_analysis.monochromator.GetGratingResponse\"\x00\x12\x9f\x01\n\nSetGrating\x12\x46.instrosetta.interfaces.light_analysis.monochromator.SetGratingRequest\x1aG.instrosetta.interfaces.light_analysis.monochromator.SetGratingResponse\"\x00\x62\x06proto3')
)




_CONNECTREQUEST = _descriptor.Descriptor(
  name='ConnectRequest',
  full_name='instrosetta.interfaces.light_analysis.monochromator.ConnectRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='instrosetta.interfaces.light_analysis.monochromator.ConnectRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='serial_number', full_name='instrosetta.interfaces.light_analysis.monochromator.ConnectRequest.serial_number', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='serial_port', full_name='instrosetta.interfaces.light_analysis.monochromator.ConnectRequest.serial_port', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='baudrate', full_name='instrosetta.interfaces.light_analysis.monochromator.ConnectRequest.baudrate', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='instrosetta.interfaces.light_analysis.monochromator.ConnectRequest.timeout', index=4,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=114,
  serialized_end=223,
)


_CONNECTRESPONSE = _descriptor.Descriptor(
  name='ConnectResponse',
  full_name='instrosetta.interfaces.light_analysis.monochromator.ConnectResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='instrosetta.interfaces.light_analysis.monochromator.ConnectResponse.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=225,
  serialized_end=256,
)


_DISCONNECTREQUEST = _descriptor.Descriptor(
  name='DisconnectRequest',
  full_name='instrosetta.interfaces.light_analysis.monochromator.DisconnectRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='instrosetta.interfaces.light_analysis.monochromator.DisconnectRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=258,
  serialized_end=291,
)


_DISCONNECTRESPONSE = _descriptor.Descriptor(
  name='DisconnectResponse',
  full_name='instrosetta.interfaces.light_analysis.monochromator.DisconnectResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='instrosetta.interfaces.light_analysis.monochromator.DisconnectResponse.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=293,
  serialized_end=327,
)


_GETWAVELENGTHRANGEREQUEST = _descriptor.Descriptor(
  name='GetWavelengthRangeRequest',
  full_name='instrosetta.interfaces.light_analysis.monochromator.GetWavelengthRangeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='instrosetta.interfaces.light_analysis.monochromator.GetWavelengthRangeRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=329,
  serialized_end=370,
)


_GETWAVELENGTHRANGERESPONSE = _descriptor.Descriptor(
  name='GetWavelengthRangeResponse',
  full_name='instrosetta.interfaces.light_analysis.monochromator.GetWavelengthRangeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='instrosetta.interfaces.light_analysis.monochromator.GetWavelengthRangeResponse.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minimum', full_name='instrosetta.interfaces.light_analysis.monochromator.GetWavelengthRangeResponse.minimum', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maximum', full_name='instrosetta.interfaces.light_analysis.monochromator.GetWavelengthRangeResponse.maximum', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='units', full_name='instrosetta.interfaces.light_analysis.monochromator.GetWavelengthRangeResponse.units', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=372,
  serialized_end=463,
)


_GETWAVELENGTHREQUEST = _descriptor.Descriptor(
  name='GetWavelengthRequest',
  full_name='instrosetta.interfaces.light_analysis.monochromator.GetWavelengthRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='instrosetta.interfaces.light_analysis.monochromator.GetWavelengthRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=465,
  serialized_end=501,
)


_GETWAVELENGTHRESPONSE = _descriptor.Descriptor(
  name='GetWavelengthResponse',
  full_name='instrosetta.interfaces.light_analysis.monochromator.GetWavelengthResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='instrosetta.interfaces.light_analysis.monochromator.GetWavelengthResponse.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wavelength', full_name='instrosetta.interfaces.light_analysis.monochromator.GetWavelengthResponse.wavelength', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='units', full_name='instrosetta.interfaces.light_analysis.monochromator.GetWavelengthResponse.units', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=503,
  serialized_end=575,
)


_SETWAVELENGTHREQUEST = _descriptor.Descriptor(
  name='SetWavelengthRequest',
  full_name='instrosetta.interfaces.light_analysis.monochromator.SetWavelengthRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='instrosetta.interfaces.light_analysis.monochromator.SetWavelengthRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wavelength', full_name='instrosetta.interfaces.light_analysis.monochromator.SetWavelengthRequest.wavelength', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='units', full_name='instrosetta.interfaces.light_analysis.monochromator.SetWavelengthRequest.units', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=577,
  serialized_end=648,
)


_SETWAVELENGTHRESPONSE = _descriptor.Descriptor(
  name='SetWavelengthResponse',
  full_name='instrosetta.interfaces.light_analysis.monochromator.SetWavelengthResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='instrosetta.interfaces.light_analysis.monochromator.SetWavelengthResponse.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wavelength', full_name='instrosetta.interfaces.light_analysis.monochromator.SetWavelengthResponse.wavelength', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='units', full_name='instrosetta.interfaces.light_analysis.monochromator.SetWavelengthResponse.units', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=650,
  serialized_end=722,
)


_GETGRATINGOPTIONSREQUEST = _descriptor.Descriptor(
  name='GetGratingOptionsRequest',
  full_name='instrosetta.interfaces.light_analysis.monochromator.GetGratingOptionsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='instrosetta.interfaces.light_analysis.monochromator.GetGratingOptionsRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=724,
  serialized_end=764,
)


_GETGRATINGOPTIONSRESPONSE = _descriptor.Descriptor(
  name='GetGratingOptionsResponse',
  full_name='instrosetta.interfaces.light_analysis.monochromator.GetGratingOptionsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='instrosetta.interfaces.light_analysis.monochromator.GetGratingOptionsResponse.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='options', full_name='instrosetta.interfaces.light_analysis.monochromator.GetGratingOptionsResponse.options', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=766,
  serialized_end=824,
)


_GETGRATINGREQUEST = _descriptor.Descriptor(
  name='GetGratingRequest',
  full_name='instrosetta.interfaces.light_analysis.monochromator.GetGratingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='instrosetta.interfaces.light_analysis.monochromator.GetGratingRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=826,
  serialized_end=859,
)


_GETGRATINGRESPONSE = _descriptor.Descriptor(
  name='GetGratingResponse',
  full_name='instrosetta.interfaces.light_analysis.monochromator.GetGratingResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='instrosetta.interfaces.light_analysis.monochromator.GetGratingResponse.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='grating', full_name='instrosetta.interfaces.light_analysis.monochromator.GetGratingResponse.grating', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=861,
  serialized_end=912,
)


_SETGRATINGREQUEST = _descriptor.Descriptor(
  name='SetGratingRequest',
  full_name='instrosetta.interfaces.light_analysis.monochromator.SetGratingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='instrosetta.interfaces.light_analysis.monochromator.SetGratingRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='grating', full_name='instrosetta.interfaces.light_analysis.monochromator.SetGratingRequest.grating', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=914,
  serialized_end=964,
)


_SETGRATINGRESPONSE = _descriptor.Descriptor(
  name='SetGratingResponse',
  full_name='instrosetta.interfaces.light_analysis.monochromator.SetGratingResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='instrosetta.interfaces.light_analysis.monochromator.SetGratingResponse.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='grating', full_name='instrosetta.interfaces.light_analysis.monochromator.SetGratingResponse.grating', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=966,
  serialized_end=1017,
)

DESCRIPTOR.message_types_by_name['ConnectRequest'] = _CONNECTREQUEST
DESCRIPTOR.message_types_by_name['ConnectResponse'] = _CONNECTRESPONSE
DESCRIPTOR.message_types_by_name['DisconnectRequest'] = _DISCONNECTREQUEST
DESCRIPTOR.message_types_by_name['DisconnectResponse'] = _DISCONNECTRESPONSE
DESCRIPTOR.message_types_by_name['GetWavelengthRangeRequest'] = _GETWAVELENGTHRANGEREQUEST
DESCRIPTOR.message_types_by_name['GetWavelengthRangeResponse'] = _GETWAVELENGTHRANGERESPONSE
DESCRIPTOR.message_types_by_name['GetWavelengthRequest'] = _GETWAVELENGTHREQUEST
DESCRIPTOR.message_types_by_name['GetWavelengthResponse'] = _GETWAVELENGTHRESPONSE
DESCRIPTOR.message_types_by_name['SetWavelengthRequest'] = _SETWAVELENGTHREQUEST
DESCRIPTOR.message_types_by_name['SetWavelengthResponse'] = _SETWAVELENGTHRESPONSE
DESCRIPTOR.message_types_by_name['GetGratingOptionsRequest'] = _GETGRATINGOPTIONSREQUEST
DESCRIPTOR.message_types_by_name['GetGratingOptionsResponse'] = _GETGRATINGOPTIONSRESPONSE
DESCRIPTOR.message_types_by_name['GetGratingRequest'] = _GETGRATINGREQUEST
DESCRIPTOR.message_types_by_name['GetGratingResponse'] = _GETGRATINGRESPONSE
DESCRIPTOR.message_types_by_name['SetGratingRequest'] = _SETGRATINGREQUEST
DESCRIPTOR.message_types_by_name['SetGratingResponse'] = _SETGRATINGRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConnectRequest = _reflection.GeneratedProtocolMessageType('ConnectRequest', (_message.Message,), dict(
  DESCRIPTOR = _CONNECTREQUEST,
  __module__ = 'instrosetta.interfaces.light_analysis.monochromator_pb2'
  # @@protoc_insertion_point(class_scope:instrosetta.interfaces.light_analysis.monochromator.ConnectRequest)
  ))
_sym_db.RegisterMessage(ConnectRequest)

ConnectResponse = _reflection.GeneratedProtocolMessageType('ConnectResponse', (_message.Message,), dict(
  DESCRIPTOR = _CONNECTRESPONSE,
  __module__ = 'instrosetta.interfaces.light_analysis.monochromator_pb2'
  # @@protoc_insertion_point(class_scope:instrosetta.interfaces.light_analysis.monochromator.ConnectResponse)
  ))
_sym_db.RegisterMessage(ConnectResponse)

DisconnectRequest = _reflection.GeneratedProtocolMessageType('DisconnectRequest', (_message.Message,), dict(
  DESCRIPTOR = _DISCONNECTREQUEST,
  __module__ = 'instrosetta.interfaces.light_analysis.monochromator_pb2'
  # @@protoc_insertion_point(class_scope:instrosetta.interfaces.light_analysis.monochromator.DisconnectRequest)
  ))
_sym_db.RegisterMessage(DisconnectRequest)

DisconnectResponse = _reflection.GeneratedProtocolMessageType('DisconnectResponse', (_message.Message,), dict(
  DESCRIPTOR = _DISCONNECTRESPONSE,
  __module__ = 'instrosetta.interfaces.light_analysis.monochromator_pb2'
  # @@protoc_insertion_point(class_scope:instrosetta.interfaces.light_analysis.monochromator.DisconnectResponse)
  ))
_sym_db.RegisterMessage(DisconnectResponse)

GetWavelengthRangeRequest = _reflection.GeneratedProtocolMessageType('GetWavelengthRangeRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETWAVELENGTHRANGEREQUEST,
  __module__ = 'instrosetta.interfaces.light_analysis.monochromator_pb2'
  # @@protoc_insertion_point(class_scope:instrosetta.interfaces.light_analysis.monochromator.GetWavelengthRangeRequest)
  ))
_sym_db.RegisterMessage(GetWavelengthRangeRequest)

GetWavelengthRangeResponse = _reflection.GeneratedProtocolMessageType('GetWavelengthRangeResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETWAVELENGTHRANGERESPONSE,
  __module__ = 'instrosetta.interfaces.light_analysis.monochromator_pb2'
  # @@protoc_insertion_point(class_scope:instrosetta.interfaces.light_analysis.monochromator.GetWavelengthRangeResponse)
  ))
_sym_db.RegisterMessage(GetWavelengthRangeResponse)

GetWavelengthRequest = _reflection.GeneratedProtocolMessageType('GetWavelengthRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETWAVELENGTHREQUEST,
  __module__ = 'instrosetta.interfaces.light_analysis.monochromator_pb2'
  # @@protoc_insertion_point(class_scope:instrosetta.interfaces.light_analysis.monochromator.GetWavelengthRequest)
  ))
_sym_db.RegisterMessage(GetWavelengthRequest)

GetWavelengthResponse = _reflection.GeneratedProtocolMessageType('GetWavelengthResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETWAVELENGTHRESPONSE,
  __module__ = 'instrosetta.interfaces.light_analysis.monochromator_pb2'
  # @@protoc_insertion_point(class_scope:instrosetta.interfaces.light_analysis.monochromator.GetWavelengthResponse)
  ))
_sym_db.RegisterMessage(GetWavelengthResponse)

SetWavelengthRequest = _reflection.GeneratedProtocolMessageType('SetWavelengthRequest', (_message.Message,), dict(
  DESCRIPTOR = _SETWAVELENGTHREQUEST,
  __module__ = 'instrosetta.interfaces.light_analysis.monochromator_pb2'
  # @@protoc_insertion_point(class_scope:instrosetta.interfaces.light_analysis.monochromator.SetWavelengthRequest)
  ))
_sym_db.RegisterMessage(SetWavelengthRequest)

SetWavelengthResponse = _reflection.GeneratedProtocolMessageType('SetWavelengthResponse', (_message.Message,), dict(
  DESCRIPTOR = _SETWAVELENGTHRESPONSE,
  __module__ = 'instrosetta.interfaces.light_analysis.monochromator_pb2'
  # @@protoc_insertion_point(class_scope:instrosetta.interfaces.light_analysis.monochromator.SetWavelengthResponse)
  ))
_sym_db.RegisterMessage(SetWavelengthResponse)

GetGratingOptionsRequest = _reflection.GeneratedProtocolMessageType('GetGratingOptionsRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETGRATINGOPTIONSREQUEST,
  __module__ = 'instrosetta.interfaces.light_analysis.monochromator_pb2'
  # @@protoc_insertion_point(class_scope:instrosetta.interfaces.light_analysis.monochromator.GetGratingOptionsRequest)
  ))
_sym_db.RegisterMessage(GetGratingOptionsRequest)

GetGratingOptionsResponse = _reflection.GeneratedProtocolMessageType('GetGratingOptionsResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETGRATINGOPTIONSRESPONSE,
  __module__ = 'instrosetta.interfaces.light_analysis.monochromator_pb2'
  # @@protoc_insertion_point(class_scope:instrosetta.interfaces.light_analysis.monochromator.GetGratingOptionsResponse)
  ))
_sym_db.RegisterMessage(GetGratingOptionsResponse)

GetGratingRequest = _reflection.GeneratedProtocolMessageType('GetGratingRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETGRATINGREQUEST,
  __module__ = 'instrosetta.interfaces.light_analysis.monochromator_pb2'
  # @@protoc_insertion_point(class_scope:instrosetta.interfaces.light_analysis.monochromator.GetGratingRequest)
  ))
_sym_db.RegisterMessage(GetGratingRequest)

GetGratingResponse = _reflection.GeneratedProtocolMessageType('GetGratingResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETGRATINGRESPONSE,
  __module__ = 'instrosetta.interfaces.light_analysis.monochromator_pb2'
  # @@protoc_insertion_point(class_scope:instrosetta.interfaces.light_analysis.monochromator.GetGratingResponse)
  ))
_sym_db.RegisterMessage(GetGratingResponse)

SetGratingRequest = _reflection.GeneratedProtocolMessageType('SetGratingRequest', (_message.Message,), dict(
  DESCRIPTOR = _SETGRATINGREQUEST,
  __module__ = 'instrosetta.interfaces.light_analysis.monochromator_pb2'
  # @@protoc_insertion_point(class_scope:instrosetta.interfaces.light_analysis.monochromator.SetGratingRequest)
  ))
_sym_db.RegisterMessage(SetGratingRequest)

SetGratingResponse = _reflection.GeneratedProtocolMessageType('SetGratingResponse', (_message.Message,), dict(
  DESCRIPTOR = _SETGRATINGRESPONSE,
  __module__ = 'instrosetta.interfaces.light_analysis.monochromator_pb2'
  # @@protoc_insertion_point(class_scope:instrosetta.interfaces.light_analysis.monochromator.SetGratingResponse)
  ))
_sym_db.RegisterMessage(SetGratingResponse)



_MONOCHROMATOR = _descriptor.ServiceDescriptor(
  name='Monochromator',
  full_name='instrosetta.interfaces.light_analysis.monochromator.Monochromator',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1020,
  serialized_end=2383,
  methods=[
  _descriptor.MethodDescriptor(
    name='Connect',
    full_name='instrosetta.interfaces.light_analysis.monochromator.Monochromator.Connect',
    index=0,
    containing_service=None,
    input_type=_CONNECTREQUEST,
    output_type=_CONNECTRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Disconnect',
    full_name='instrosetta.interfaces.light_analysis.monochromator.Monochromator.Disconnect',
    index=1,
    containing_service=None,
    input_type=_DISCONNECTREQUEST,
    output_type=_DISCONNECTRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetWavelengthRange',
    full_name='instrosetta.interfaces.light_analysis.monochromator.Monochromator.GetWavelengthRange',
    index=2,
    containing_service=None,
    input_type=_GETWAVELENGTHRANGEREQUEST,
    output_type=_GETWAVELENGTHRANGERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetWavelength',
    full_name='instrosetta.interfaces.light_analysis.monochromator.Monochromator.GetWavelength',
    index=3,
    containing_service=None,
    input_type=_GETWAVELENGTHREQUEST,
    output_type=_GETWAVELENGTHRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SetWavelength',
    full_name='instrosetta.interfaces.light_analysis.monochromator.Monochromator.SetWavelength',
    index=4,
    containing_service=None,
    input_type=_SETWAVELENGTHREQUEST,
    output_type=_SETWAVELENGTHRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetGratingRange',
    full_name='instrosetta.interfaces.light_analysis.monochromator.Monochromator.GetGratingRange',
    index=5,
    containing_service=None,
    input_type=_GETGRATINGOPTIONSREQUEST,
    output_type=_GETGRATINGOPTIONSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetGrating',
    full_name='instrosetta.interfaces.light_analysis.monochromator.Monochromator.GetGrating',
    index=6,
    containing_service=None,
    input_type=_GETGRATINGREQUEST,
    output_type=_GETGRATINGRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SetGrating',
    full_name='instrosetta.interfaces.light_analysis.monochromator.Monochromator.SetGrating',
    index=7,
    containing_service=None,
    input_type=_SETGRATINGREQUEST,
    output_type=_SETGRATINGRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MONOCHROMATOR)

DESCRIPTOR.services_by_name['Monochromator'] = _MONOCHROMATOR

# @@protoc_insertion_point(module_scope)
