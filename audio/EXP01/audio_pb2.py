# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: 2.audio.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='2.audio.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\r2.audio.proto\"\x15\n\x05\x41udio\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x62\x06proto3'
)




_AUDIO = _descriptor.Descriptor(
  name='Audio',
  full_name='Audio',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='Audio.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=17,
  serialized_end=38,
)

DESCRIPTOR.message_types_by_name['Audio'] = _AUDIO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Audio = _reflection.GeneratedProtocolMessageType('Audio', (_message.Message,), {
  'DESCRIPTOR' : _AUDIO,
  '__module__' : '2.audio_pb2'
  # @@protoc_insertion_point(class_scope:Audio)
  })
_sym_db.RegisterMessage(Audio)


# @@protoc_insertion_point(module_scope)
