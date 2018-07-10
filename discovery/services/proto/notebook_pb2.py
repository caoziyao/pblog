# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/notebook.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto import user_pb2 as proto_dot_user__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/notebook.proto',
  package='notebook',
  syntax='proto3',
  serialized_pb=_b('\n\x14proto/notebook.proto\x12\x08notebook\x1a\x10proto/user.proto\"$\n\x12GetNoteBookRequest\x12\x0e\n\x06userId\x18\x01 \x01(\t\"X\n\x0bMsgNoteBook\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0f\n\x07summary\x18\x02 \x01(\t\x12\r\n\x05image\x18\x03 \x01(\t\x12\x0e\n\x06userId\x18\x04 \x01(\t\x12\n\n\x02id\x18\x05 \x01(\t\"W\n\x13GetNoteBookResponse\x12#\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x15.notebook.MsgNoteBook\x12\x1b\n\x04user\x18\x02 \x01(\x0b\x32\r.user.MsgUser\"<\n\rErrorResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\t2Z\n\x08Notebook\x12N\n\x0fGetNotebookInfo\x12\x1c.notebook.GetNoteBookRequest\x1a\x1d.notebook.GetNoteBookResponseb\x06proto3')
  ,
  dependencies=[proto_dot_user__pb2.DESCRIPTOR,])




_GETNOTEBOOKREQUEST = _descriptor.Descriptor(
  name='GetNoteBookRequest',
  full_name='notebook.GetNoteBookRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='userId', full_name='notebook.GetNoteBookRequest.userId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=52,
  serialized_end=88,
)


_MSGNOTEBOOK = _descriptor.Descriptor(
  name='MsgNoteBook',
  full_name='notebook.MsgNoteBook',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='notebook.MsgNoteBook.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='summary', full_name='notebook.MsgNoteBook.summary', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='image', full_name='notebook.MsgNoteBook.image', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userId', full_name='notebook.MsgNoteBook.userId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='notebook.MsgNoteBook.id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=90,
  serialized_end=178,
)


_GETNOTEBOOKRESPONSE = _descriptor.Descriptor(
  name='GetNoteBookResponse',
  full_name='notebook.GetNoteBookResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='notebook.GetNoteBookResponse.data', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user', full_name='notebook.GetNoteBookResponse.user', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=180,
  serialized_end=267,
)


_ERRORRESPONSE = _descriptor.Descriptor(
  name='ErrorResponse',
  full_name='notebook.ErrorResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='notebook.ErrorResponse.code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='notebook.ErrorResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='notebook.ErrorResponse.data', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=269,
  serialized_end=329,
)

_GETNOTEBOOKRESPONSE.fields_by_name['data'].message_type = _MSGNOTEBOOK
_GETNOTEBOOKRESPONSE.fields_by_name['user'].message_type = proto_dot_user__pb2._MSGUSER
DESCRIPTOR.message_types_by_name['GetNoteBookRequest'] = _GETNOTEBOOKREQUEST
DESCRIPTOR.message_types_by_name['MsgNoteBook'] = _MSGNOTEBOOK
DESCRIPTOR.message_types_by_name['GetNoteBookResponse'] = _GETNOTEBOOKRESPONSE
DESCRIPTOR.message_types_by_name['ErrorResponse'] = _ERRORRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetNoteBookRequest = _reflection.GeneratedProtocolMessageType('GetNoteBookRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETNOTEBOOKREQUEST,
  __module__ = 'proto.notebook_pb2'
  # @@protoc_insertion_point(class_scope:notebook.GetNoteBookRequest)
  ))
_sym_db.RegisterMessage(GetNoteBookRequest)

MsgNoteBook = _reflection.GeneratedProtocolMessageType('MsgNoteBook', (_message.Message,), dict(
  DESCRIPTOR = _MSGNOTEBOOK,
  __module__ = 'proto.notebook_pb2'
  # @@protoc_insertion_point(class_scope:notebook.MsgNoteBook)
  ))
_sym_db.RegisterMessage(MsgNoteBook)

GetNoteBookResponse = _reflection.GeneratedProtocolMessageType('GetNoteBookResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETNOTEBOOKRESPONSE,
  __module__ = 'proto.notebook_pb2'
  # @@protoc_insertion_point(class_scope:notebook.GetNoteBookResponse)
  ))
_sym_db.RegisterMessage(GetNoteBookResponse)

ErrorResponse = _reflection.GeneratedProtocolMessageType('ErrorResponse', (_message.Message,), dict(
  DESCRIPTOR = _ERRORRESPONSE,
  __module__ = 'proto.notebook_pb2'
  # @@protoc_insertion_point(class_scope:notebook.ErrorResponse)
  ))
_sym_db.RegisterMessage(ErrorResponse)



_NOTEBOOK = _descriptor.ServiceDescriptor(
  name='Notebook',
  full_name='notebook.Notebook',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=331,
  serialized_end=421,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetNotebookInfo',
    full_name='notebook.Notebook.GetNotebookInfo',
    index=0,
    containing_service=None,
    input_type=_GETNOTEBOOKREQUEST,
    output_type=_GETNOTEBOOKRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_NOTEBOOK)

DESCRIPTOR.services_by_name['Notebook'] = _NOTEBOOK

# @@protoc_insertion_point(module_scope)