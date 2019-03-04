# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: devices/motion/linear/singleaxis.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='devices/motion/linear/singleaxis.proto',
  package='devices.motion.linear.singleaxis',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n&devices/motion/linear/singleaxis.proto\x12 devices.motion.linear.singleaxis\"\x14\n\x12ScanDevicesRequest\"\xb2\x01\n\x06\x44\x65vice\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rserial_number\x18\x02 \x01(\r\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x46\n\nmotor_type\x18\x04 \x01(\x0e\x32\x32.devices.motion.linear.singleaxis.Device.MotorType\"&\n\tMotorType\x12\x0c\n\x08\x44\x43_SERVO\x10\x00\x12\x0b\n\x07STEPPER\x10\x01\"X\n\x0e\x43onnectRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x38\n\x06\x64\x65vice\x18\x02 \x01(\x0b\x32(.devices.motion.linear.singleaxis.Device\".\n\x0fGetRangeRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05units\x18\x02 \x01(\t\"W\n\nStageRange\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05units\x18\x02 \x01(\t\x12\x0b\n\x03min\x18\x03 \x01(\x01\x12\x0b\n\x03max\x18\x04 \x01(\x01\x12\x12\n\nresolution\x18\x05 \x01(\x01\"#\n\x12GetPositionRequest\x12\r\n\x05units\x18\x01 \x01(\t\"(\n\x08\x44istance\x12\r\n\x05value\x18\x01 \x01(\x01\x12\r\n\x05units\x18\x02 \x01(\t\"(\n\x08Position\x12\r\n\x05value\x18\x01 \x01(\x01\x12\r\n\x05units\x18\x02 \x01(\t2\xa4\x05\n\x10SingleLinearAxis\x12q\n\x0bScanDevices\x12\x34.devices.motion.linear.singleaxis.ScanDevicesRequest\x1a(.devices.motion.linear.singleaxis.Device\"\x00\x30\x01\x12g\n\x07\x43onnect\x12\x30.devices.motion.linear.singleaxis.ConnectRequest\x1a(.devices.motion.linear.singleaxis.Device\"\x00\x12m\n\x08GetRange\x12\x31.devices.motion.linear.singleaxis.GetRangeRequest\x1a,.devices.motion.linear.singleaxis.StageRange\"\x00\x12q\n\x0bGetPosition\x12\x34.devices.motion.linear.singleaxis.GetPositionRequest\x1a*.devices.motion.linear.singleaxis.Position\"\x00\x12h\n\x0cMoveAbsolute\x12*.devices.motion.linear.singleaxis.Position\x1a*.devices.motion.linear.singleaxis.Position\"\x00\x12h\n\x0cMoveRelative\x12*.devices.motion.linear.singleaxis.Distance\x1a*.devices.motion.linear.singleaxis.Distance\"\x00\x62\x06proto3')
)



_DEVICE_MOTORTYPE = _descriptor.EnumDescriptor(
  name='MotorType',
  full_name='devices.motion.linear.singleaxis.Device.MotorType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DC_SERVO', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STEPPER', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=239,
  serialized_end=277,
)
_sym_db.RegisterEnumDescriptor(_DEVICE_MOTORTYPE)


_SCANDEVICESREQUEST = _descriptor.Descriptor(
  name='ScanDevicesRequest',
  full_name='devices.motion.linear.singleaxis.ScanDevicesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=76,
  serialized_end=96,
)


_DEVICE = _descriptor.Descriptor(
  name='Device',
  full_name='devices.motion.linear.singleaxis.Device',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='devices.motion.linear.singleaxis.Device.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='serial_number', full_name='devices.motion.linear.singleaxis.Device.serial_number', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='devices.motion.linear.singleaxis.Device.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='motor_type', full_name='devices.motion.linear.singleaxis.Device.motor_type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DEVICE_MOTORTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=99,
  serialized_end=277,
)


_CONNECTREQUEST = _descriptor.Descriptor(
  name='ConnectRequest',
  full_name='devices.motion.linear.singleaxis.ConnectRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='devices.motion.linear.singleaxis.ConnectRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device', full_name='devices.motion.linear.singleaxis.ConnectRequest.device', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=279,
  serialized_end=367,
)


_GETRANGEREQUEST = _descriptor.Descriptor(
  name='GetRangeRequest',
  full_name='devices.motion.linear.singleaxis.GetRangeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='devices.motion.linear.singleaxis.GetRangeRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='units', full_name='devices.motion.linear.singleaxis.GetRangeRequest.units', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=369,
  serialized_end=415,
)


_STAGERANGE = _descriptor.Descriptor(
  name='StageRange',
  full_name='devices.motion.linear.singleaxis.StageRange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='devices.motion.linear.singleaxis.StageRange.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='units', full_name='devices.motion.linear.singleaxis.StageRange.units', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min', full_name='devices.motion.linear.singleaxis.StageRange.min', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max', full_name='devices.motion.linear.singleaxis.StageRange.max', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resolution', full_name='devices.motion.linear.singleaxis.StageRange.resolution', index=4,
      number=5, type=1, cpp_type=5, label=1,
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
  serialized_start=417,
  serialized_end=504,
)


_GETPOSITIONREQUEST = _descriptor.Descriptor(
  name='GetPositionRequest',
  full_name='devices.motion.linear.singleaxis.GetPositionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='units', full_name='devices.motion.linear.singleaxis.GetPositionRequest.units', index=0,
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
  serialized_start=506,
  serialized_end=541,
)


_DISTANCE = _descriptor.Descriptor(
  name='Distance',
  full_name='devices.motion.linear.singleaxis.Distance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='devices.motion.linear.singleaxis.Distance.value', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='units', full_name='devices.motion.linear.singleaxis.Distance.units', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=543,
  serialized_end=583,
)


_POSITION = _descriptor.Descriptor(
  name='Position',
  full_name='devices.motion.linear.singleaxis.Position',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='devices.motion.linear.singleaxis.Position.value', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='units', full_name='devices.motion.linear.singleaxis.Position.units', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=585,
  serialized_end=625,
)

_DEVICE.fields_by_name['motor_type'].enum_type = _DEVICE_MOTORTYPE
_DEVICE_MOTORTYPE.containing_type = _DEVICE
_CONNECTREQUEST.fields_by_name['device'].message_type = _DEVICE
DESCRIPTOR.message_types_by_name['ScanDevicesRequest'] = _SCANDEVICESREQUEST
DESCRIPTOR.message_types_by_name['Device'] = _DEVICE
DESCRIPTOR.message_types_by_name['ConnectRequest'] = _CONNECTREQUEST
DESCRIPTOR.message_types_by_name['GetRangeRequest'] = _GETRANGEREQUEST
DESCRIPTOR.message_types_by_name['StageRange'] = _STAGERANGE
DESCRIPTOR.message_types_by_name['GetPositionRequest'] = _GETPOSITIONREQUEST
DESCRIPTOR.message_types_by_name['Distance'] = _DISTANCE
DESCRIPTOR.message_types_by_name['Position'] = _POSITION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ScanDevicesRequest = _reflection.GeneratedProtocolMessageType('ScanDevicesRequest', (_message.Message,), dict(
  DESCRIPTOR = _SCANDEVICESREQUEST,
  __module__ = 'devices.motion.linear.singleaxis_pb2'
  # @@protoc_insertion_point(class_scope:devices.motion.linear.singleaxis.ScanDevicesRequest)
  ))
_sym_db.RegisterMessage(ScanDevicesRequest)

Device = _reflection.GeneratedProtocolMessageType('Device', (_message.Message,), dict(
  DESCRIPTOR = _DEVICE,
  __module__ = 'devices.motion.linear.singleaxis_pb2'
  # @@protoc_insertion_point(class_scope:devices.motion.linear.singleaxis.Device)
  ))
_sym_db.RegisterMessage(Device)

ConnectRequest = _reflection.GeneratedProtocolMessageType('ConnectRequest', (_message.Message,), dict(
  DESCRIPTOR = _CONNECTREQUEST,
  __module__ = 'devices.motion.linear.singleaxis_pb2'
  # @@protoc_insertion_point(class_scope:devices.motion.linear.singleaxis.ConnectRequest)
  ))
_sym_db.RegisterMessage(ConnectRequest)

GetRangeRequest = _reflection.GeneratedProtocolMessageType('GetRangeRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETRANGEREQUEST,
  __module__ = 'devices.motion.linear.singleaxis_pb2'
  # @@protoc_insertion_point(class_scope:devices.motion.linear.singleaxis.GetRangeRequest)
  ))
_sym_db.RegisterMessage(GetRangeRequest)

StageRange = _reflection.GeneratedProtocolMessageType('StageRange', (_message.Message,), dict(
  DESCRIPTOR = _STAGERANGE,
  __module__ = 'devices.motion.linear.singleaxis_pb2'
  # @@protoc_insertion_point(class_scope:devices.motion.linear.singleaxis.StageRange)
  ))
_sym_db.RegisterMessage(StageRange)

GetPositionRequest = _reflection.GeneratedProtocolMessageType('GetPositionRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETPOSITIONREQUEST,
  __module__ = 'devices.motion.linear.singleaxis_pb2'
  # @@protoc_insertion_point(class_scope:devices.motion.linear.singleaxis.GetPositionRequest)
  ))
_sym_db.RegisterMessage(GetPositionRequest)

Distance = _reflection.GeneratedProtocolMessageType('Distance', (_message.Message,), dict(
  DESCRIPTOR = _DISTANCE,
  __module__ = 'devices.motion.linear.singleaxis_pb2'
  # @@protoc_insertion_point(class_scope:devices.motion.linear.singleaxis.Distance)
  ))
_sym_db.RegisterMessage(Distance)

Position = _reflection.GeneratedProtocolMessageType('Position', (_message.Message,), dict(
  DESCRIPTOR = _POSITION,
  __module__ = 'devices.motion.linear.singleaxis_pb2'
  # @@protoc_insertion_point(class_scope:devices.motion.linear.singleaxis.Position)
  ))
_sym_db.RegisterMessage(Position)



_SINGLELINEARAXIS = _descriptor.ServiceDescriptor(
  name='SingleLinearAxis',
  full_name='devices.motion.linear.singleaxis.SingleLinearAxis',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=628,
  serialized_end=1304,
  methods=[
  _descriptor.MethodDescriptor(
    name='ScanDevices',
    full_name='devices.motion.linear.singleaxis.SingleLinearAxis.ScanDevices',
    index=0,
    containing_service=None,
    input_type=_SCANDEVICESREQUEST,
    output_type=_DEVICE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Connect',
    full_name='devices.motion.linear.singleaxis.SingleLinearAxis.Connect',
    index=1,
    containing_service=None,
    input_type=_CONNECTREQUEST,
    output_type=_DEVICE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetRange',
    full_name='devices.motion.linear.singleaxis.SingleLinearAxis.GetRange',
    index=2,
    containing_service=None,
    input_type=_GETRANGEREQUEST,
    output_type=_STAGERANGE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetPosition',
    full_name='devices.motion.linear.singleaxis.SingleLinearAxis.GetPosition',
    index=3,
    containing_service=None,
    input_type=_GETPOSITIONREQUEST,
    output_type=_POSITION,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='MoveAbsolute',
    full_name='devices.motion.linear.singleaxis.SingleLinearAxis.MoveAbsolute',
    index=4,
    containing_service=None,
    input_type=_POSITION,
    output_type=_POSITION,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='MoveRelative',
    full_name='devices.motion.linear.singleaxis.SingleLinearAxis.MoveRelative',
    index=5,
    containing_service=None,
    input_type=_DISTANCE,
    output_type=_DISTANCE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SINGLELINEARAXIS)

DESCRIPTOR.services_by_name['SingleLinearAxis'] = _SINGLELINEARAXIS

# @@protoc_insertion_point(module_scope)
