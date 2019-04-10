# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from instrosetta.common import connection_pb2 as instrosetta_dot_common_dot_connection__pb2
from instrosetta.interfaces.light_analysis import spectrograph_pb2 as instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2


class SpectrographStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Connect = channel.unary_unary(
        '/instrosetta.interfaces.light_analysis.spectrograph.v1.Spectrograph/Connect',
        request_serializer=instrosetta_dot_common_dot_connection__pb2.ConnectRequest.SerializeToString,
        response_deserializer=instrosetta_dot_common_dot_connection__pb2.ConnectResponse.FromString,
        )
    self.Disconnect = channel.unary_unary(
        '/instrosetta.interfaces.light_analysis.spectrograph.v1.Spectrograph/Disconnect',
        request_serializer=instrosetta_dot_common_dot_connection__pb2.DisconnectRequest.SerializeToString,
        response_deserializer=instrosetta_dot_common_dot_connection__pb2.DisconnectResponse.FromString,
        )
    self.Save = channel.unary_unary(
        '/instrosetta.interfaces.light_analysis.spectrograph.v1.Spectrograph/Save',
        request_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.SaveRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.SaveResponse.FromString,
        )
    self.Run = channel.unary_unary(
        '/instrosetta.interfaces.light_analysis.spectrograph.v1.Spectrograph/Run',
        request_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.RunRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.RunResponse.FromString,
        )
    self.GetGrating = channel.unary_unary(
        '/instrosetta.interfaces.light_analysis.spectrograph.v1.Spectrograph/GetGrating',
        request_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.GetGratingRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.GetGratingResponse.FromString,
        )
    self.GetGratingOptions = channel.unary_unary(
        '/instrosetta.interfaces.light_analysis.spectrograph.v1.Spectrograph/GetGratingOptions',
        request_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.GetGratingOptionsRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.GetGratingOptionsResponse.FromString,
        )
    self.SetGrating = channel.unary_unary(
        '/instrosetta.interfaces.light_analysis.spectrograph.v1.Spectrograph/SetGrating',
        request_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.SetGratingRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.SetGratingResponse.FromString,
        )
    self.GetShutterState = channel.unary_unary(
        '/instrosetta.interfaces.light_analysis.spectrograph.v1.Spectrograph/GetShutterState',
        request_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.GetShutterStateRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.GetShutterStateResponse.FromString,
        )
    self.SetShutterState = channel.unary_unary(
        '/instrosetta.interfaces.light_analysis.spectrograph.v1.Spectrograph/SetShutterState',
        request_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.SetShutterStateRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.SetShutterStateResponse.FromString,
        )
    self.GetWavelength = channel.unary_unary(
        '/instrosetta.interfaces.light_analysis.spectrograph.v1.Spectrograph/GetWavelength',
        request_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.GetWavelengthRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.GetWavelengthResponse.FromString,
        )
    self.SetWavelength = channel.unary_unary(
        '/instrosetta.interfaces.light_analysis.spectrograph.v1.Spectrograph/SetWavelength',
        request_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.SetWavelengthRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.SetWavelengthResponse.FromString,
        )
    self.GetExposure = channel.unary_unary(
        '/instrosetta.interfaces.light_analysis.spectrograph.v1.Spectrograph/GetExposure',
        request_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.GetExposureRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.GetExposureResponse.FromString,
        )
    self.SetExposure = channel.unary_unary(
        '/instrosetta.interfaces.light_analysis.spectrograph.v1.Spectrograph/SetExposure',
        request_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.SetExposureRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.SetExposureResponse.FromString,
        )
    self.GetSlitWidth = channel.unary_unary(
        '/instrosetta.interfaces.light_analysis.spectrograph.v1.Spectrograph/GetSlitWidth',
        request_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.GetSlitWidthRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.GetSlitWidthResponse.FromString,
        )
    self.SetSlitWidth = channel.unary_unary(
        '/instrosetta.interfaces.light_analysis.spectrograph.v1.Spectrograph/SetSlitWidth',
        request_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.SetSlitWidthRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.SetSlitWidthResponse.FromString,
        )
    self.GetConnectionDetails = channel.unary_unary(
        '/instrosetta.interfaces.light_analysis.spectrograph.v1.Spectrograph/GetConnectionDetails',
        request_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.GetConnectionDetailsRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.GetConnectionDetailsResponse.FromString,
        )
    self.SetConnectionDetails = channel.unary_unary(
        '/instrosetta.interfaces.light_analysis.spectrograph.v1.Spectrograph/SetConnectionDetails',
        request_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.SetConnectionDetailsRequest.SerializeToString,
        response_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.SetConnectionDetailsResponse.FromString,
        )


class SpectrographServicer(object):
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

  def Save(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Run(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetGrating(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetGratingOptions(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetGrating(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetShutterState(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetShutterState(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetWavelength(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetWavelength(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetExposure(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetExposure(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetSlitWidth(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetSlitWidth(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetConnectionDetails(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetConnectionDetails(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SpectrographServicer_to_server(servicer, server):
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
      'Save': grpc.unary_unary_rpc_method_handler(
          servicer.Save,
          request_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.SaveRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.SaveResponse.SerializeToString,
      ),
      'Run': grpc.unary_unary_rpc_method_handler(
          servicer.Run,
          request_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.RunRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.RunResponse.SerializeToString,
      ),
      'GetGrating': grpc.unary_unary_rpc_method_handler(
          servicer.GetGrating,
          request_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.GetGratingRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.GetGratingResponse.SerializeToString,
      ),
      'GetGratingOptions': grpc.unary_unary_rpc_method_handler(
          servicer.GetGratingOptions,
          request_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.GetGratingOptionsRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.GetGratingOptionsResponse.SerializeToString,
      ),
      'SetGrating': grpc.unary_unary_rpc_method_handler(
          servicer.SetGrating,
          request_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.SetGratingRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.SetGratingResponse.SerializeToString,
      ),
      'GetShutterState': grpc.unary_unary_rpc_method_handler(
          servicer.GetShutterState,
          request_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.GetShutterStateRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.GetShutterStateResponse.SerializeToString,
      ),
      'SetShutterState': grpc.unary_unary_rpc_method_handler(
          servicer.SetShutterState,
          request_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.SetShutterStateRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.SetShutterStateResponse.SerializeToString,
      ),
      'GetWavelength': grpc.unary_unary_rpc_method_handler(
          servicer.GetWavelength,
          request_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.GetWavelengthRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.GetWavelengthResponse.SerializeToString,
      ),
      'SetWavelength': grpc.unary_unary_rpc_method_handler(
          servicer.SetWavelength,
          request_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.SetWavelengthRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.SetWavelengthResponse.SerializeToString,
      ),
      'GetExposure': grpc.unary_unary_rpc_method_handler(
          servicer.GetExposure,
          request_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.GetExposureRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.GetExposureResponse.SerializeToString,
      ),
      'SetExposure': grpc.unary_unary_rpc_method_handler(
          servicer.SetExposure,
          request_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.SetExposureRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.SetExposureResponse.SerializeToString,
      ),
      'GetSlitWidth': grpc.unary_unary_rpc_method_handler(
          servicer.GetSlitWidth,
          request_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.GetSlitWidthRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.GetSlitWidthResponse.SerializeToString,
      ),
      'SetSlitWidth': grpc.unary_unary_rpc_method_handler(
          servicer.SetSlitWidth,
          request_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.SetSlitWidthRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.SetSlitWidthResponse.SerializeToString,
      ),
      'GetConnectionDetails': grpc.unary_unary_rpc_method_handler(
          servicer.GetConnectionDetails,
          request_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.GetConnectionDetailsRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.GetConnectionDetailsResponse.SerializeToString,
      ),
      'SetConnectionDetails': grpc.unary_unary_rpc_method_handler(
          servicer.SetConnectionDetails,
          request_deserializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.SetConnectionDetailsRequest.FromString,
          response_serializer=instrosetta_dot_interfaces_dot_light__analysis_dot_spectrograph__pb2.SetConnectionDetailsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'instrosetta.interfaces.light_analysis.spectrograph.v1.Spectrograph', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
