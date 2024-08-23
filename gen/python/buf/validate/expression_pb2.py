# Copyright 2024 IBM Corp.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: buf/validate/expression.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x62uf/validate/expression.proto\x12\x0c\x62uf.validate\"V\n\nConstraint\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12\x1e\n\nexpression\x18\x03 \x01(\tR\nexpression\"E\n\nViolations\x12\x37\n\nviolations\x18\x01 \x03(\x0b\x32\x17.buf.validate.ViolationR\nviolations\"\x82\x01\n\tViolation\x12\x1d\n\nfield_path\x18\x01 \x01(\tR\tfieldPath\x12#\n\rconstraint_id\x18\x02 \x01(\tR\x0c\x63onstraintId\x12\x18\n\x07message\x18\x03 \x01(\tR\x07message\x12\x17\n\x07\x66or_key\x18\x04 \x01(\x08R\x06\x66orKeyBp\n\x12\x62uild.buf.validateB\x0f\x45xpressionProtoP\x01ZGbuf.build/gen/go/bufbuild/protovalidate/protocolbuffers/go/buf/validateb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'buf.validate.expression_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\022build.buf.validateB\017ExpressionProtoP\001ZGbuf.build/gen/go/bufbuild/protovalidate/protocolbuffers/go/buf/validate'
  _globals['_CONSTRAINT']._serialized_start=47
  _globals['_CONSTRAINT']._serialized_end=133
  _globals['_VIOLATIONS']._serialized_start=135
  _globals['_VIOLATIONS']._serialized_end=204
  _globals['_VIOLATION']._serialized_start=207
  _globals['_VIOLATION']._serialized_end=337
# @@protoc_insertion_point(module_scope)
