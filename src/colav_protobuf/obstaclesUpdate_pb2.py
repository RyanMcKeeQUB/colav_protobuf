# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: obstaclesUpdate.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='obstaclesUpdate.proto',
  package='colav',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x15obstaclesUpdate.proto\x12\x05\x63olav\"\xb4\t\n\x0fObstaclesUpdate\x12\x13\n\x0bmission_tag\x18\x01 \x01(\t\x12\x41\n\x11\x64ynamic_obstacles\x18\x02 \x03(\x0b\x32&.colav.ObstaclesUpdate.DynamicObstacle\x12?\n\x10static_obstacles\x18\x03 \x03(\x0b\x32%.colav.ObstaclesUpdate.StaticObstacle\x12\x11\n\ttimestamp\x18\x04 \x01(\t\x1a(\n\x05Point\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\x1a\x38\n\nQuaternion\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\x12\t\n\x01w\x18\x04 \x01(\x02\x1an\n\x04Pose\x12.\n\x08position\x18\x01 \x01(\x0b\x32\x1c.colav.ObstaclesUpdate.Point\x12\x36\n\x0borientation\x18\x02 \x01(\x0b\x32!.colav.ObstaclesUpdate.Quaternion\x1aV\n\x05State\x12)\n\x04pose\x18\x01 \x01(\x0b\x32\x1b.colav.ObstaclesUpdate.Pose\x12\x10\n\x08velocity\x18\x02 \x01(\x02\x12\x10\n\x08yaw_rate\x18\x03 \x01(\x02\x1aK\n\x17\x44ynamicObstacleGeometry\x12\x0b\n\x03loa\x18\x01 \x01(\x02\x12\x0c\n\x04\x62\x65\x61m\x18\x02 \x01(\x02\x12\x15\n\rsafety_radius\x18\x03 \x01(\x02\x1aj\n\x16StaticObstacleGeometry\x12\x36\n\x10polyshape_points\x18\x01 \x03(\x0b\x32\x1c.colav.ObstaclesUpdate.Point\x12\x18\n\x10inflation_radius\x18\x02 \x01(\x02\x1a\xc7\x01\n\x0f\x44ynamicObstacle\x12\x0b\n\x03tag\x18\x01 \x01(\t\x12\x38\n\x04type\x18\x02 \x01(\x0e\x32*.colav.ObstaclesUpdate.DynamicObstacleType\x12+\n\x05state\x18\x03 \x01(\x0b\x32\x1c.colav.ObstaclesUpdate.State\x12@\n\x08geometry\x18\x04 \x01(\x0b\x32..colav.ObstaclesUpdate.DynamicObstacleGeometry\x1a\xc2\x01\n\x0eStaticObstacle\x12\x0b\n\x03tag\x18\x01 \x01(\t\x12\x37\n\x04type\x18\x02 \x01(\x0e\x32).colav.ObstaclesUpdate.StaticObstacleType\x12)\n\x04pose\x18\x03 \x01(\x0b\x32\x1b.colav.ObstaclesUpdate.Pose\x12?\n\x08geometry\x18\x04 \x01(\x0b\x32-.colav.ObstaclesUpdate.StaticObstacleGeometry\":\n\x13\x44ynamicObstacleType\x12\x17\n\x13\x44YNAMIC_UNSPECIFIED\x10\x00\x12\n\n\x06VESSEL\x10\x01\"E\n\x12StaticObstacleType\x12\x16\n\x12STATIC_UNSPECIFIED\x10\x00\x12\r\n\tLAND_MASS\x10\x01\x12\x08\n\x04\x42UOY\x10\x02\x62\x06proto3'
)



_OBSTACLESUPDATE_DYNAMICOBSTACLETYPE = _descriptor.EnumDescriptor(
  name='DynamicObstacleType',
  full_name='colav.ObstaclesUpdate.DynamicObstacleType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DYNAMIC_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VESSEL', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1108,
  serialized_end=1166,
)
_sym_db.RegisterEnumDescriptor(_OBSTACLESUPDATE_DYNAMICOBSTACLETYPE)

_OBSTACLESUPDATE_STATICOBSTACLETYPE = _descriptor.EnumDescriptor(
  name='StaticObstacleType',
  full_name='colav.ObstaclesUpdate.StaticObstacleType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATIC_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LAND_MASS', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BUOY', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1168,
  serialized_end=1237,
)
_sym_db.RegisterEnumDescriptor(_OBSTACLESUPDATE_STATICOBSTACLETYPE)


_OBSTACLESUPDATE_POINT = _descriptor.Descriptor(
  name='Point',
  full_name='colav.ObstaclesUpdate.Point',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='colav.ObstaclesUpdate.Point.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='colav.ObstaclesUpdate.Point.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='z', full_name='colav.ObstaclesUpdate.Point.z', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=224,
  serialized_end=264,
)

_OBSTACLESUPDATE_QUATERNION = _descriptor.Descriptor(
  name='Quaternion',
  full_name='colav.ObstaclesUpdate.Quaternion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='colav.ObstaclesUpdate.Quaternion.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='colav.ObstaclesUpdate.Quaternion.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='z', full_name='colav.ObstaclesUpdate.Quaternion.z', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='w', full_name='colav.ObstaclesUpdate.Quaternion.w', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=266,
  serialized_end=322,
)

_OBSTACLESUPDATE_POSE = _descriptor.Descriptor(
  name='Pose',
  full_name='colav.ObstaclesUpdate.Pose',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='position', full_name='colav.ObstaclesUpdate.Pose.position', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='orientation', full_name='colav.ObstaclesUpdate.Pose.orientation', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=324,
  serialized_end=434,
)

_OBSTACLESUPDATE_STATE = _descriptor.Descriptor(
  name='State',
  full_name='colav.ObstaclesUpdate.State',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pose', full_name='colav.ObstaclesUpdate.State.pose', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='velocity', full_name='colav.ObstaclesUpdate.State.velocity', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='yaw_rate', full_name='colav.ObstaclesUpdate.State.yaw_rate', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_end=522,
)

_OBSTACLESUPDATE_DYNAMICOBSTACLEGEOMETRY = _descriptor.Descriptor(
  name='DynamicObstacleGeometry',
  full_name='colav.ObstaclesUpdate.DynamicObstacleGeometry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='loa', full_name='colav.ObstaclesUpdate.DynamicObstacleGeometry.loa', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='beam', full_name='colav.ObstaclesUpdate.DynamicObstacleGeometry.beam', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='safety_radius', full_name='colav.ObstaclesUpdate.DynamicObstacleGeometry.safety_radius', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=524,
  serialized_end=599,
)

_OBSTACLESUPDATE_STATICOBSTACLEGEOMETRY = _descriptor.Descriptor(
  name='StaticObstacleGeometry',
  full_name='colav.ObstaclesUpdate.StaticObstacleGeometry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='polyshape_points', full_name='colav.ObstaclesUpdate.StaticObstacleGeometry.polyshape_points', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='inflation_radius', full_name='colav.ObstaclesUpdate.StaticObstacleGeometry.inflation_radius', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=601,
  serialized_end=707,
)

_OBSTACLESUPDATE_DYNAMICOBSTACLE = _descriptor.Descriptor(
  name='DynamicObstacle',
  full_name='colav.ObstaclesUpdate.DynamicObstacle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tag', full_name='colav.ObstaclesUpdate.DynamicObstacle.tag', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='colav.ObstaclesUpdate.DynamicObstacle.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='colav.ObstaclesUpdate.DynamicObstacle.state', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='geometry', full_name='colav.ObstaclesUpdate.DynamicObstacle.geometry', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=710,
  serialized_end=909,
)

_OBSTACLESUPDATE_STATICOBSTACLE = _descriptor.Descriptor(
  name='StaticObstacle',
  full_name='colav.ObstaclesUpdate.StaticObstacle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tag', full_name='colav.ObstaclesUpdate.StaticObstacle.tag', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='colav.ObstaclesUpdate.StaticObstacle.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pose', full_name='colav.ObstaclesUpdate.StaticObstacle.pose', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='geometry', full_name='colav.ObstaclesUpdate.StaticObstacle.geometry', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=912,
  serialized_end=1106,
)

_OBSTACLESUPDATE = _descriptor.Descriptor(
  name='ObstaclesUpdate',
  full_name='colav.ObstaclesUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='mission_tag', full_name='colav.ObstaclesUpdate.mission_tag', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dynamic_obstacles', full_name='colav.ObstaclesUpdate.dynamic_obstacles', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='static_obstacles', full_name='colav.ObstaclesUpdate.static_obstacles', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='colav.ObstaclesUpdate.timestamp', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_OBSTACLESUPDATE_POINT, _OBSTACLESUPDATE_QUATERNION, _OBSTACLESUPDATE_POSE, _OBSTACLESUPDATE_STATE, _OBSTACLESUPDATE_DYNAMICOBSTACLEGEOMETRY, _OBSTACLESUPDATE_STATICOBSTACLEGEOMETRY, _OBSTACLESUPDATE_DYNAMICOBSTACLE, _OBSTACLESUPDATE_STATICOBSTACLE, ],
  enum_types=[
    _OBSTACLESUPDATE_DYNAMICOBSTACLETYPE,
    _OBSTACLESUPDATE_STATICOBSTACLETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=1237,
)

_OBSTACLESUPDATE_POINT.containing_type = _OBSTACLESUPDATE
_OBSTACLESUPDATE_QUATERNION.containing_type = _OBSTACLESUPDATE
_OBSTACLESUPDATE_POSE.fields_by_name['position'].message_type = _OBSTACLESUPDATE_POINT
_OBSTACLESUPDATE_POSE.fields_by_name['orientation'].message_type = _OBSTACLESUPDATE_QUATERNION
_OBSTACLESUPDATE_POSE.containing_type = _OBSTACLESUPDATE
_OBSTACLESUPDATE_STATE.fields_by_name['pose'].message_type = _OBSTACLESUPDATE_POSE
_OBSTACLESUPDATE_STATE.containing_type = _OBSTACLESUPDATE
_OBSTACLESUPDATE_DYNAMICOBSTACLEGEOMETRY.containing_type = _OBSTACLESUPDATE
_OBSTACLESUPDATE_STATICOBSTACLEGEOMETRY.fields_by_name['polyshape_points'].message_type = _OBSTACLESUPDATE_POINT
_OBSTACLESUPDATE_STATICOBSTACLEGEOMETRY.containing_type = _OBSTACLESUPDATE
_OBSTACLESUPDATE_DYNAMICOBSTACLE.fields_by_name['type'].enum_type = _OBSTACLESUPDATE_DYNAMICOBSTACLETYPE
_OBSTACLESUPDATE_DYNAMICOBSTACLE.fields_by_name['state'].message_type = _OBSTACLESUPDATE_STATE
_OBSTACLESUPDATE_DYNAMICOBSTACLE.fields_by_name['geometry'].message_type = _OBSTACLESUPDATE_DYNAMICOBSTACLEGEOMETRY
_OBSTACLESUPDATE_DYNAMICOBSTACLE.containing_type = _OBSTACLESUPDATE
_OBSTACLESUPDATE_STATICOBSTACLE.fields_by_name['type'].enum_type = _OBSTACLESUPDATE_STATICOBSTACLETYPE
_OBSTACLESUPDATE_STATICOBSTACLE.fields_by_name['pose'].message_type = _OBSTACLESUPDATE_POSE
_OBSTACLESUPDATE_STATICOBSTACLE.fields_by_name['geometry'].message_type = _OBSTACLESUPDATE_STATICOBSTACLEGEOMETRY
_OBSTACLESUPDATE_STATICOBSTACLE.containing_type = _OBSTACLESUPDATE
_OBSTACLESUPDATE.fields_by_name['dynamic_obstacles'].message_type = _OBSTACLESUPDATE_DYNAMICOBSTACLE
_OBSTACLESUPDATE.fields_by_name['static_obstacles'].message_type = _OBSTACLESUPDATE_STATICOBSTACLE
_OBSTACLESUPDATE_DYNAMICOBSTACLETYPE.containing_type = _OBSTACLESUPDATE
_OBSTACLESUPDATE_STATICOBSTACLETYPE.containing_type = _OBSTACLESUPDATE
DESCRIPTOR.message_types_by_name['ObstaclesUpdate'] = _OBSTACLESUPDATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ObstaclesUpdate = _reflection.GeneratedProtocolMessageType('ObstaclesUpdate', (_message.Message,), {

  'Point' : _reflection.GeneratedProtocolMessageType('Point', (_message.Message,), {
    'DESCRIPTOR' : _OBSTACLESUPDATE_POINT,
    '__module__' : 'obstaclesUpdate_pb2'
    # @@protoc_insertion_point(class_scope:colav.ObstaclesUpdate.Point)
    })
  ,

  'Quaternion' : _reflection.GeneratedProtocolMessageType('Quaternion', (_message.Message,), {
    'DESCRIPTOR' : _OBSTACLESUPDATE_QUATERNION,
    '__module__' : 'obstaclesUpdate_pb2'
    # @@protoc_insertion_point(class_scope:colav.ObstaclesUpdate.Quaternion)
    })
  ,

  'Pose' : _reflection.GeneratedProtocolMessageType('Pose', (_message.Message,), {
    'DESCRIPTOR' : _OBSTACLESUPDATE_POSE,
    '__module__' : 'obstaclesUpdate_pb2'
    # @@protoc_insertion_point(class_scope:colav.ObstaclesUpdate.Pose)
    })
  ,

  'State' : _reflection.GeneratedProtocolMessageType('State', (_message.Message,), {
    'DESCRIPTOR' : _OBSTACLESUPDATE_STATE,
    '__module__' : 'obstaclesUpdate_pb2'
    # @@protoc_insertion_point(class_scope:colav.ObstaclesUpdate.State)
    })
  ,

  'DynamicObstacleGeometry' : _reflection.GeneratedProtocolMessageType('DynamicObstacleGeometry', (_message.Message,), {
    'DESCRIPTOR' : _OBSTACLESUPDATE_DYNAMICOBSTACLEGEOMETRY,
    '__module__' : 'obstaclesUpdate_pb2'
    # @@protoc_insertion_point(class_scope:colav.ObstaclesUpdate.DynamicObstacleGeometry)
    })
  ,

  'StaticObstacleGeometry' : _reflection.GeneratedProtocolMessageType('StaticObstacleGeometry', (_message.Message,), {
    'DESCRIPTOR' : _OBSTACLESUPDATE_STATICOBSTACLEGEOMETRY,
    '__module__' : 'obstaclesUpdate_pb2'
    # @@protoc_insertion_point(class_scope:colav.ObstaclesUpdate.StaticObstacleGeometry)
    })
  ,

  'DynamicObstacle' : _reflection.GeneratedProtocolMessageType('DynamicObstacle', (_message.Message,), {
    'DESCRIPTOR' : _OBSTACLESUPDATE_DYNAMICOBSTACLE,
    '__module__' : 'obstaclesUpdate_pb2'
    # @@protoc_insertion_point(class_scope:colav.ObstaclesUpdate.DynamicObstacle)
    })
  ,

  'StaticObstacle' : _reflection.GeneratedProtocolMessageType('StaticObstacle', (_message.Message,), {
    'DESCRIPTOR' : _OBSTACLESUPDATE_STATICOBSTACLE,
    '__module__' : 'obstaclesUpdate_pb2'
    # @@protoc_insertion_point(class_scope:colav.ObstaclesUpdate.StaticObstacle)
    })
  ,
  'DESCRIPTOR' : _OBSTACLESUPDATE,
  '__module__' : 'obstaclesUpdate_pb2'
  # @@protoc_insertion_point(class_scope:colav.ObstaclesUpdate)
  })
_sym_db.RegisterMessage(ObstaclesUpdate)
_sym_db.RegisterMessage(ObstaclesUpdate.Point)
_sym_db.RegisterMessage(ObstaclesUpdate.Quaternion)
_sym_db.RegisterMessage(ObstaclesUpdate.Pose)
_sym_db.RegisterMessage(ObstaclesUpdate.State)
_sym_db.RegisterMessage(ObstaclesUpdate.DynamicObstacleGeometry)
_sym_db.RegisterMessage(ObstaclesUpdate.StaticObstacleGeometry)
_sym_db.RegisterMessage(ObstaclesUpdate.DynamicObstacle)
_sym_db.RegisterMessage(ObstaclesUpdate.StaticObstacle)


# @@protoc_insertion_point(module_scope)
