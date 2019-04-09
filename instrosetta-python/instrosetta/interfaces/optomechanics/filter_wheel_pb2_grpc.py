# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from instrosetta.common import connection_pb2 as instrosetta_dot_common_dot_connection__pb2
from instrosetta.interfaces.optomechanics import filter_wheel_pb2 as instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2


class FilterWheelStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Connect = channel.unary_unary(
        '/instrosetta.interfaces.optomechanics.filter_wheel.v1.FilterWheel/Connect',
        request_serializer=instrosetta_dot_common_dot_connection__pb2.ConnectRequest.SerializeToString,
        response_deserializer=instrosetta_dot_common_dot_connection__pb2.ConnectResponse.FromString,
        )
    self.Disconnect = channel.unary_unary(
        '/instrosetta.interfaces.optomechanics.filter_wheel.v1.FilterWheel/Disconnect',
        request_serializer=instrosetta_dot_common_dot_connection__pb2.DisconnectRequest.SerializeToString,
        response_deserializer=instrosetta_dot_common_dot_connection__pb2.DisconnectResponse.FromString,
        )
    self.GetSpeedOptions = channel.unary_unary(
        '/instrosetta.interfaces.optomechanics.filter_wheel.v1.FilterWheel/GetSpeedOptions',
        request_serializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.GetSpeedOptionsRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.GetSpeedOptionsResponse.FromString,
        )
    self.GetSpeed = channel.unary_unary(
        '/instrosetta.interfaces.optomechanics.filter_wheel.v1.FilterWheel/GetSpeed',
        request_serializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.GetSpeedRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.GetSpeedResponse.FromString,
        )
    self.SetSpeed = channel.unary_unary(
        '/instrosetta.interfaces.optomechanics.filter_wheel.v1.FilterWheel/SetSpeed',
        request_serializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.SetSpeedRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.SetSpeedResponse.FromString,
        )
    self.GetSensorsOptions = channel.unary_unary(
        '/instrosetta.interfaces.optomechanics.filter_wheel.v1.FilterWheel/GetSensorsOptions',
        request_serializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.GetSensorsOptionsRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.GetSensorsOptionsResponse.FromString,
        )
    self.GetSensors = channel.unary_unary(
        '/instrosetta.interfaces.optomechanics.filter_wheel.v1.FilterWheel/GetSensors',
        request_serializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.GetSensorsRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.GetSensorsResponse.FromString,
        )
    self.SetSensors = channel.unary_unary(
        '/instrosetta.interfaces.optomechanics.filter_wheel.v1.FilterWheel/SetSensors',
        request_serializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.SetSensorsRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.SetSensorsResponse.FromString,
        )
    self.GetPort = channel.unary_unary(
        '/instrosetta.interfaces.optomechanics.filter_wheel.v1.FilterWheel/GetPort',
        request_serializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.GetPortRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.GetPortResponse.FromString,
        )
    self.SetPort = channel.unary_unary(
        '/instrosetta.interfaces.optomechanics.filter_wheel.v1.FilterWheel/SetPort',
        request_serializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.SetPortRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.SetPortResponse.FromString,
        )
    self.GetFilterOptions = channel.unary_unary(
        '/instrosetta.interfaces.optomechanics.filter_wheel.v1.FilterWheel/GetFilterOptions',
        request_serializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.GetFilterOptionsRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.GetFilterOptionsResponse.FromString,
        )
    self.GetFilter = channel.unary_unary(
        '/instrosetta.interfaces.optomechanics.filter_wheel.v1.FilterWheel/GetFilter',
        request_serializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.GetFilterRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.GetFilterResponse.FromString,
        )
    self.SetFilter = channel.unary_unary(
        '/instrosetta.interfaces.optomechanics.filter_wheel.v1.FilterWheel/SetFilter',
        request_serializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.SetFilterRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.SetFilterResponse.FromString,
        )
    self.GetPositionOptions = channel.unary_unary(
        '/instrosetta.interfaces.optomechanics.filter_wheel.v1.FilterWheel/GetPositionOptions',
        request_serializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.GetPositionOptionsRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.GetPositionOptionsResponse.FromString,
        )
    self.GetPosition = channel.unary_unary(
        '/instrosetta.interfaces.optomechanics.filter_wheel.v1.FilterWheel/GetPosition',
        request_serializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.GetPositionRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.GetPositionResponse.FromString,
        )
    self.SetPosition = channel.unary_unary(
        '/instrosetta.interfaces.optomechanics.filter_wheel.v1.FilterWheel/SetPosition',
        request_serializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.SetPositionRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.SetPositionResponse.FromString,
        )


class FilterWheelServicer(object):
  # missing associated documentation comment in .proto file
  pass

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

  def GetSpeedOptions(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetSpeed(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetSpeed(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetSensorsOptions(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetSensors(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetSensors(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetPort(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetPort(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetFilterOptions(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetFilter(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetFilter(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetPositionOptions(self, request, context):
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

  def SetPosition(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_FilterWheelServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Connect': grpc.unary_unary_rpc_method_handler(
          servicer.Connect,
          request_deserializer=instrosetta_dot_common_dot_connection__pb2.ConnectRequest.FromString,
          response_serializer=instrosetta_dot_common_dot_connection__pb2.ConnectResponse.SerializeToString,
      ),
      'Disconnect': grpc.unary_unary_rpc_method_handler(
          servicer.Disconnect,
          request_deserializer=instrosetta_dot_common_dot_connection__pb2.DisconnectRequest.FromString,
          response_serializer=instrosetta_dot_common_dot_connection__pb2.DisconnectResponse.SerializeToString,
      ),
      'GetSpeedOptions': grpc.unary_unary_rpc_method_handler(
          servicer.GetSpeedOptions,
          request_deserializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.GetSpeedOptionsRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.GetSpeedOptionsResponse.SerializeToString,
      ),
      'GetSpeed': grpc.unary_unary_rpc_method_handler(
          servicer.GetSpeed,
          request_deserializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.GetSpeedRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.GetSpeedResponse.SerializeToString,
      ),
      'SetSpeed': grpc.unary_unary_rpc_method_handler(
          servicer.SetSpeed,
          request_deserializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.SetSpeedRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.SetSpeedResponse.SerializeToString,
      ),
      'GetSensorsOptions': grpc.unary_unary_rpc_method_handler(
          servicer.GetSensorsOptions,
          request_deserializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.GetSensorsOptionsRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.GetSensorsOptionsResponse.SerializeToString,
      ),
      'GetSensors': grpc.unary_unary_rpc_method_handler(
          servicer.GetSensors,
          request_deserializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.GetSensorsRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.GetSensorsResponse.SerializeToString,
      ),
      'SetSensors': grpc.unary_unary_rpc_method_handler(
          servicer.SetSensors,
          request_deserializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.SetSensorsRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.SetSensorsResponse.SerializeToString,
      ),
      'GetPort': grpc.unary_unary_rpc_method_handler(
          servicer.GetPort,
          request_deserializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.GetPortRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.GetPortResponse.SerializeToString,
      ),
      'SetPort': grpc.unary_unary_rpc_method_handler(
          servicer.SetPort,
          request_deserializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.SetPortRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.SetPortResponse.SerializeToString,
      ),
      'GetFilterOptions': grpc.unary_unary_rpc_method_handler(
          servicer.GetFilterOptions,
          request_deserializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.GetFilterOptionsRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.GetFilterOptionsResponse.SerializeToString,
      ),
      'GetFilter': grpc.unary_unary_rpc_method_handler(
          servicer.GetFilter,
          request_deserializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.GetFilterRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.GetFilterResponse.SerializeToString,
      ),
      'SetFilter': grpc.unary_unary_rpc_method_handler(
          servicer.SetFilter,
          request_deserializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.SetFilterRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.SetFilterResponse.SerializeToString,
      ),
      'GetPositionOptions': grpc.unary_unary_rpc_method_handler(
          servicer.GetPositionOptions,
          request_deserializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.GetPositionOptionsRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.GetPositionOptionsResponse.SerializeToString,
      ),
      'GetPosition': grpc.unary_unary_rpc_method_handler(
          servicer.GetPosition,
          request_deserializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.GetPositionRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.GetPositionResponse.SerializeToString,
      ),
      'SetPosition': grpc.unary_unary_rpc_method_handler(
          servicer.SetPosition,
          request_deserializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.SetPositionRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_optomechanics_dot_filter__wheel__pb2.SetPositionResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'instrosetta.interfaces.optomechanics.filter_wheel.v1.FilterWheel', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
