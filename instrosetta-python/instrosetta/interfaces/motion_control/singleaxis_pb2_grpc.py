# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from instrosetta.interfaces.motion_control import singleaxis_pb2 as instrosetta_dot_interfaces_dot_motion__control_dot_singleaxis__pb2


class SingleAxisStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Echo = channel.unary_unary(
        '/instrosetta.interfaces.motion_control.singleaxis.SingleAxis/Echo',
        request_serializer=instrosetta_dot_interfaces_dot_motion__control_dot_singleaxis__pb2.TextMessage.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_motion__control_dot_singleaxis__pb2.TextMessage.FromString,
        )
    self.ScanDevices = channel.unary_stream(
        '/instrosetta.interfaces.motion_control.singleaxis.SingleAxis/ScanDevices',
        request_serializer=instrosetta_dot_interfaces_dot_motion__control_dot_singleaxis__pb2.ScanDevicesRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_motion__control_dot_singleaxis__pb2.Device.FromString,
        )
    self.Connect = channel.unary_unary(
        '/instrosetta.interfaces.motion_control.singleaxis.SingleAxis/Connect',
        request_serializer=instrosetta_dot_interfaces_dot_motion__control_dot_singleaxis__pb2.ConnectRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_motion__control_dot_singleaxis__pb2.Device.FromString,
        )
    self.Disconnect = channel.unary_unary(
        '/instrosetta.interfaces.motion_control.singleaxis.SingleAxis/Disconnect',
        request_serializer=instrosetta_dot_interfaces_dot_motion__control_dot_singleaxis__pb2.DisconnectRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_motion__control_dot_singleaxis__pb2.Device.FromString,
        )
    self.HomeMotor = channel.unary_unary(
        '/instrosetta.interfaces.motion_control.singleaxis.SingleAxis/HomeMotor',
        request_serializer=instrosetta_dot_interfaces_dot_motion__control_dot_singleaxis__pb2.HomeMotorRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_motion__control_dot_singleaxis__pb2.Position.FromString,
        )
    self.GetRange = channel.unary_unary(
        '/instrosetta.interfaces.motion_control.singleaxis.SingleAxis/GetRange',
        request_serializer=instrosetta_dot_interfaces_dot_motion__control_dot_singleaxis__pb2.GetRangeRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_motion__control_dot_singleaxis__pb2.StageRange.FromString,
        )
    self.GetPosition = channel.unary_unary(
        '/instrosetta.interfaces.motion_control.singleaxis.SingleAxis/GetPosition',
        request_serializer=instrosetta_dot_interfaces_dot_motion__control_dot_singleaxis__pb2.GetPositionRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_motion__control_dot_singleaxis__pb2.Position.FromString,
        )
    self.MoveAbsolute = channel.unary_stream(
        '/instrosetta.interfaces.motion_control.singleaxis.SingleAxis/MoveAbsolute',
        request_serializer=instrosetta_dot_interfaces_dot_motion__control_dot_singleaxis__pb2.MoveAbsoluteRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_motion__control_dot_singleaxis__pb2.Position.FromString,
        )
    self.MoveRelative = channel.unary_stream(
        '/instrosetta.interfaces.motion_control.singleaxis.SingleAxis/MoveRelative',
        request_serializer=instrosetta_dot_interfaces_dot_motion__control_dot_singleaxis__pb2.MoveRelativeRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_motion__control_dot_singleaxis__pb2.Position.FromString,
        )


class SingleAxisServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Echo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ScanDevices(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Connect(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Disconnect(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def HomeMotor(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetRange(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetPosition(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MoveAbsolute(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MoveRelative(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SingleAxisServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Echo': grpc.unary_unary_rpc_method_handler(
          servicer.Echo,
          request_deserializer=instrosetta_dot_interfaces_dot_motion__control_dot_singleaxis__pb2.TextMessage.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_motion__control_dot_singleaxis__pb2.TextMessage.SerializeToString,
      ),
      'ScanDevices': grpc.unary_stream_rpc_method_handler(
          servicer.ScanDevices,
          request_deserializer=instrosetta_dot_interfaces_dot_motion__control_dot_singleaxis__pb2.ScanDevicesRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_motion__control_dot_singleaxis__pb2.Device.SerializeToString,
      ),
      'Connect': grpc.unary_unary_rpc_method_handler(
          servicer.Connect,
          request_deserializer=instrosetta_dot_interfaces_dot_motion__control_dot_singleaxis__pb2.ConnectRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_motion__control_dot_singleaxis__pb2.Device.SerializeToString,
      ),
      'Disconnect': grpc.unary_unary_rpc_method_handler(
          servicer.Disconnect,
          request_deserializer=instrosetta_dot_interfaces_dot_motion__control_dot_singleaxis__pb2.DisconnectRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_motion__control_dot_singleaxis__pb2.Device.SerializeToString,
      ),
      'HomeMotor': grpc.unary_unary_rpc_method_handler(
          servicer.HomeMotor,
          request_deserializer=instrosetta_dot_interfaces_dot_motion__control_dot_singleaxis__pb2.HomeMotorRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_motion__control_dot_singleaxis__pb2.Position.SerializeToString,
      ),
      'GetRange': grpc.unary_unary_rpc_method_handler(
          servicer.GetRange,
          request_deserializer=instrosetta_dot_interfaces_dot_motion__control_dot_singleaxis__pb2.GetRangeRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_motion__control_dot_singleaxis__pb2.StageRange.SerializeToString,
      ),
      'GetPosition': grpc.unary_unary_rpc_method_handler(
          servicer.GetPosition,
          request_deserializer=instrosetta_dot_interfaces_dot_motion__control_dot_singleaxis__pb2.GetPositionRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_motion__control_dot_singleaxis__pb2.Position.SerializeToString,
      ),
      'MoveAbsolute': grpc.unary_stream_rpc_method_handler(
          servicer.MoveAbsolute,
          request_deserializer=instrosetta_dot_interfaces_dot_motion__control_dot_singleaxis__pb2.MoveAbsoluteRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_motion__control_dot_singleaxis__pb2.Position.SerializeToString,
      ),
      'MoveRelative': grpc.unary_stream_rpc_method_handler(
          servicer.MoveRelative,
          request_deserializer=instrosetta_dot_interfaces_dot_motion__control_dot_singleaxis__pb2.MoveRelativeRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_motion__control_dot_singleaxis__pb2.Position.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'instrosetta.interfaces.motion_control.singleaxis.SingleAxis', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
