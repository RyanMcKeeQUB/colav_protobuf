# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: colav_proto/missionResponse.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!colav_proto/missionResponse.proto\x12\x05\x63olav\"\x90\x02\n\x0fMissionResponse\x12\x13\n\x0bmission_tag\x18\x01 \x02(\t\x12\x1f\n\x17mission_start_timestamp\x18\x02 \x02(\t\x12\x44\n\x10mission_response\x18\x03 \x02(\x0e\x32*.colav.MissionResponse.MissionResponseEnum\x12 \n\x18mission_response_details\x18\x04 \x02(\t\"_\n\x13MissionResponseEnum\x12\n\n\x06UNKOWN\x10\x00\x12\x14\n\x10MISSION_STARTING\x10\x01\x12\x11\n\rMISSION_ERROR\x10\x02\x12\x13\n\x0fMISSION_INVALID\x10\x03')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'colav_proto.missionResponse_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_MISSIONRESPONSE']._serialized_start=45
  _globals['_MISSIONRESPONSE']._serialized_end=317
  _globals['_MISSIONRESPONSE_MISSIONRESPONSEENUM']._serialized_start=222
  _globals['_MISSIONRESPONSE_MISSIONRESPONSEENUM']._serialized_end=317
# @@protoc_insertion_point(module_scope)
