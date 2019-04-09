# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: instrosetta/interfaces/electronics/simple_switch.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from instrosetta.common import connection_pb2 as instrosetta_dot_common_dot_connection__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='instrosetta/interfaces/electronics/simple_switch.proto',
  package='instrosetta.interfaces.electronics.simple_switch.v1',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n6instrosetta/interfaces/electronics/simple_switch.proto\x12\x33instrosetta.interfaces.electronics.simple_switch.v1\x1a#instrosetta/common/connection.proto\"\x1b\n\x0b\x46lipRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"m\n\x0c\x46lipResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12O\n\x05state\x18\x02 \x01(\x0e\x32@.instrosetta.interfaces.electronics.simple_switch.v1.SwitchState\"\x1f\n\x0fGetStateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"q\n\x10GetStateResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12O\n\x05state\x18\x02 \x01(\x0e\x32@.instrosetta.interfaces.electronics.simple_switch.v1.SwitchState\"p\n\x0fSetStateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12O\n\x05state\x18\x02 \x01(\x0e\x32@.instrosetta.interfaces.electronics.simple_switch.v1.SwitchState\"q\n\x10SetStateResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12O\n\x05state\x18\x02 \x01(\x0e\x32@.instrosetta.interfaces.electronics.simple_switch.v1.SwitchState*+\n\x0bSwitchState\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x07\n\x03OFF\x10\x01\x12\x06\n\x02ON\x10\x02\x32\xbf\x04\n\x0cSimpleSwitch\x12.\n\x07\x43onnect\x12\x0f.ConnectRequest\x1a\x10.ConnectResponse\"\x00\x12\x37\n\nDisconnect\x12\x12.DisconnectRequest\x1a\x13.DisconnectResponse\"\x00\x12\x8d\x01\n\x04\x46lip\x12@.instrosetta.interfaces.electronics.simple_switch.v1.FlipRequest\x1a\x41.instrosetta.interfaces.electronics.simple_switch.v1.FlipResponse\"\x00\x12\x99\x01\n\x08GetState\x12\x44.instrosetta.interfaces.electronics.simple_switch.v1.GetStateRequest\x1a\x45.instrosetta.interfaces.electronics.simple_switch.v1.GetStateResponse\"\x00\x12\x99\x01\n\x08SetState\x12\x44.instrosetta.interfaces.electronics.simple_switch.v1.SetStateRequest\x1a\x45.instrosetta.interfaces.electronics.simple_switch.v1.SetStateResponse\"\x00\x62\x06proto3')
  ,
  dependencies=[instrosetta_dot_common_dot_connection__pb2.DESCRIPTOR,])

_SWITCHSTATE = _descriptor.EnumDescriptor(
  name='SwitchState',
  full_name='instrosetta.interfaces.electronics.simple_switch.v1.SwitchState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OFF', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ON', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=665,
  serialized_end=708,
)
_sym_db.RegisterEnumDescriptor(_SWITCHSTATE)

SwitchState = enum_type_wrapper.EnumTypeWrapper(_SWITCHSTATE)
UNKNOWN = 0
OFF = 1
ON = 2



_FLIPREQUEST = _descriptor.Descriptor(
  name='FlipRequest',
  full_name='instrosetta.interfaces.electronics.simple_switch.v1.FlipRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='instrosetta.interfaces.electronics.simple_switch.v1.FlipRequest.name', index=0,
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
  serialized_start=148,
  serialized_end=175,
)


_FLIPRESPONSE = _descriptor.Descriptor(
  name='FlipResponse',
  full_name='instrosetta.interfaces.electronics.simple_switch.v1.FlipResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='instrosetta.interfaces.electronics.simple_switch.v1.FlipResponse.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='instrosetta.interfaces.electronics.simple_switch.v1.FlipResponse.state', index=1,
      number=2, type=14, cpp_type=8, label=1,
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
  serialized_start=177,
  serialized_end=286,
)


_GETSTATEREQUEST = _descriptor.Descriptor(
  name='GetStateRequest',
  full_name='instrosetta.interfaces.electronics.simple_switch.v1.GetStateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='instrosetta.interfaces.electronics.simple_switch.v1.GetStateRequest.name', index=0,
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
  serialized_start=288,
  serialized_end=319,
)


_GETSTATERESPONSE = _descriptor.Descriptor(
  name='GetStateResponse',
  full_name='instrosetta.interfaces.electronics.simple_switch.v1.GetStateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='instrosetta.interfaces.electronics.simple_switch.v1.GetStateResponse.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='instrosetta.interfaces.electronics.simple_switch.v1.GetStateResponse.state', index=1,
      number=2, type=14, cpp_type=8, label=1,
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
  serialized_start=321,
  serialized_end=434,
)


_SETSTATEREQUEST = _descriptor.Descriptor(
  name='SetStateRequest',
  full_name='instrosetta.interfaces.electronics.simple_switch.v1.SetStateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='instrosetta.interfaces.electronics.simple_switch.v1.SetStateRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='instrosetta.interfaces.electronics.simple_switch.v1.SetStateRequest.state', index=1,
      number=2, type=14, cpp_type=8, label=1,
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
  serialized_start=436,
  serialized_end=548,
)


_SETSTATERESPONSE = _descriptor.Descriptor(
  name='SetStateResponse',
  full_name='instrosetta.interfaces.electronics.simple_switch.v1.SetStateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='instrosetta.interfaces.electronics.simple_switch.v1.SetStateResponse.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='instrosetta.interfaces.electronics.simple_switch.v1.SetStateResponse.state', index=1,
      number=2, type=14, cpp_type=8, label=1,
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
  serialized_start=550,
  serialized_end=663,
)

_FLIPRESPONSE.fields_by_name['state'].enum_type = _SWITCHSTATE
_GETSTATERESPONSE.fields_by_name['state'].enum_type = _SWITCHSTATE
_SETSTATEREQUEST.fields_by_name['state'].enum_type = _SWITCHSTATE
_SETSTATERESPONSE.fields_by_name['state'].enum_type = _SWITCHSTATE
DESCRIPTOR.message_types_by_name['FlipRequest'] = _FLIPREQUEST
DESCRIPTOR.message_types_by_name['FlipResponse'] = _FLIPRESPONSE
DESCRIPTOR.message_types_by_name['GetStateRequest'] = _GETSTATEREQUEST
DESCRIPTOR.message_types_by_name['GetStateResponse'] = _GETSTATERESPONSE
DESCRIPTOR.message_types_by_name['SetStateRequest'] = _SETSTATEREQUEST
DESCRIPTOR.message_types_by_name['SetStateResponse'] = _SETSTATERESPONSE
DESCRIPTOR.enum_types_by_name['SwitchState'] = _SWITCHSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FlipRequest = _reflection.GeneratedProtocolMessageType('FlipRequest', (_message.Message,), dict(
  DESCRIPTOR = _FLIPREQUEST,
  __module__ = 'instrosetta.interfaces.electronics.simple_switch_pb2'
  # @@protoc_insertion_point(class_scope:instrosetta.interfaces.electronics.simple_switch.v1.FlipRequest)
  ))
_sym_db.RegisterMessage(FlipRequest)

FlipResponse = _reflection.GeneratedProtocolMessageType('FlipResponse', (_message.Message,), dict(
  DESCRIPTOR = _FLIPRESPONSE,
  __module__ = 'instrosetta.interfaces.electronics.simple_switch_pb2'
  # @@protoc_insertion_point(class_scope:instrosetta.interfaces.electronics.simple_switch.v1.FlipResponse)
  ))
_sym_db.RegisterMessage(FlipResponse)

GetStateRequest = _reflection.GeneratedProtocolMessageType('GetStateRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETSTATEREQUEST,
  __module__ = 'instrosetta.interfaces.electronics.simple_switch_pb2'
  # @@protoc_insertion_point(class_scope:instrosetta.interfaces.electronics.simple_switch.v1.GetStateRequest)
  ))
_sym_db.RegisterMessage(GetStateRequest)

GetStateResponse = _reflection.GeneratedProtocolMessageType('GetStateResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETSTATERESPONSE,
  __module__ = 'instrosetta.interfaces.electronics.simple_switch_pb2'
  # @@protoc_insertion_point(class_scope:instrosetta.interfaces.electronics.simple_switch.v1.GetStateResponse)
  ))
_sym_db.RegisterMessage(GetStateResponse)

SetStateRequest = _reflection.GeneratedProtocolMessageType('SetStateRequest', (_message.Message,), dict(
  DESCRIPTOR = _SETSTATEREQUEST,
  __module__ = 'instrosetta.interfaces.electronics.simple_switch_pb2'
  # @@protoc_insertion_point(class_scope:instrosetta.interfaces.electronics.simple_switch.v1.SetStateRequest)
  ))
_sym_db.RegisterMessage(SetStateRequest)

SetStateResponse = _reflection.GeneratedProtocolMessageType('SetStateResponse', (_message.Message,), dict(
  DESCRIPTOR = _SETSTATERESPONSE,
  __module__ = 'instrosetta.interfaces.electronics.simple_switch_pb2'
  # @@protoc_insertion_point(class_scope:instrosetta.interfaces.electronics.simple_switch.v1.SetStateResponse)
  ))
_sym_db.RegisterMessage(SetStateResponse)



_SIMPLESWITCH = _descriptor.ServiceDescriptor(
  name='SimpleSwitch',
  full_name='instrosetta.interfaces.electronics.simple_switch.v1.SimpleSwitch',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=711,
  serialized_end=1286,
  methods=[
  _descriptor.MethodDescriptor(
    name='Connect',
    full_name='instrosetta.interfaces.electronics.simple_switch.v1.SimpleSwitch.Connect',
    index=0,
    containing_service=None,
    input_type=instrosetta_dot_common_dot_connection__pb2._CONNECTREQUEST,
    output_type=instrosetta_dot_common_dot_connection__pb2._CONNECTRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Disconnect',
    full_name='instrosetta.interfaces.electronics.simple_switch.v1.SimpleSwitch.Disconnect',
    index=1,
    containing_service=None,
    input_type=instrosetta_dot_common_dot_connection__pb2._DISCONNECTREQUEST,
    output_type=instrosetta_dot_common_dot_connection__pb2._DISCONNECTRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Flip',
    full_name='instrosetta.interfaces.electronics.simple_switch.v1.SimpleSwitch.Flip',
    index=2,
    containing_service=None,
    input_type=_FLIPREQUEST,
    output_type=_FLIPRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetState',
    full_name='instrosetta.interfaces.electronics.simple_switch.v1.SimpleSwitch.GetState',
    index=3,
    containing_service=None,
    input_type=_GETSTATEREQUEST,
    output_type=_GETSTATERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SetState',
    full_name='instrosetta.interfaces.electronics.simple_switch.v1.SimpleSwitch.SetState',
    index=4,
    containing_service=None,
    input_type=_SETSTATEREQUEST,
    output_type=_SETSTATERESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SIMPLESWITCH)

DESCRIPTOR.services_by_name['SimpleSwitch'] = _SIMPLESWITCH

# @@protoc_insertion_point(module_scope)
