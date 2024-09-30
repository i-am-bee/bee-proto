from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExecuteRequest(_message.Message):
    __slots__ = ("source_code", "files")
    class FilesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SOURCE_CODE_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    source_code: str
    files: _containers.ScalarMap[str, str]
    def __init__(self, source_code: _Optional[str] = ..., files: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ExecuteResponse(_message.Message):
    __slots__ = ("stdout", "stderr", "exit_code", "files")
    class FilesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    STDOUT_FIELD_NUMBER: _ClassVar[int]
    STDERR_FIELD_NUMBER: _ClassVar[int]
    EXIT_CODE_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    stdout: str
    stderr: str
    exit_code: int
    files: _containers.ScalarMap[str, str]
    def __init__(self, stdout: _Optional[str] = ..., stderr: _Optional[str] = ..., exit_code: _Optional[int] = ..., files: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ParseCustomToolRequest(_message.Message):
    __slots__ = ("tool_source_code",)
    TOOL_SOURCE_CODE_FIELD_NUMBER: _ClassVar[int]
    tool_source_code: str
    def __init__(self, tool_source_code: _Optional[str] = ...) -> None: ...

class ParseCustomToolResponseSuccess(_message.Message):
    __slots__ = ("tool_name", "tool_description", "tool_input_schema_json")
    TOOL_NAME_FIELD_NUMBER: _ClassVar[int]
    TOOL_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TOOL_INPUT_SCHEMA_JSON_FIELD_NUMBER: _ClassVar[int]
    tool_name: str
    tool_description: str
    tool_input_schema_json: str
    def __init__(self, tool_name: _Optional[str] = ..., tool_description: _Optional[str] = ..., tool_input_schema_json: _Optional[str] = ...) -> None: ...

class ParseCustomToolResponseError(_message.Message):
    __slots__ = ("error_messages",)
    ERROR_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    error_messages: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, error_messages: _Optional[_Iterable[str]] = ...) -> None: ...

class ParseCustomToolResponse(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: ParseCustomToolResponseSuccess
    error: ParseCustomToolResponseError
    def __init__(self, success: _Optional[_Union[ParseCustomToolResponseSuccess, _Mapping]] = ..., error: _Optional[_Union[ParseCustomToolResponseError, _Mapping]] = ...) -> None: ...

class ExecuteCustomToolRequest(_message.Message):
    __slots__ = ("tool_source_code", "tool_input_json")
    TOOL_SOURCE_CODE_FIELD_NUMBER: _ClassVar[int]
    TOOL_INPUT_JSON_FIELD_NUMBER: _ClassVar[int]
    tool_source_code: str
    tool_input_json: str
    def __init__(self, tool_source_code: _Optional[str] = ..., tool_input_json: _Optional[str] = ...) -> None: ...

class ExecuteCustomToolResponseSuccess(_message.Message):
    __slots__ = ("tool_output_json",)
    TOOL_OUTPUT_JSON_FIELD_NUMBER: _ClassVar[int]
    tool_output_json: str
    def __init__(self, tool_output_json: _Optional[str] = ...) -> None: ...

class ExecuteCustomToolResponseError(_message.Message):
    __slots__ = ("stderr",)
    STDERR_FIELD_NUMBER: _ClassVar[int]
    stderr: str
    def __init__(self, stderr: _Optional[str] = ...) -> None: ...

class ExecuteCustomToolResponse(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: ExecuteCustomToolResponseSuccess
    error: ExecuteCustomToolResponseError
    def __init__(self, success: _Optional[_Union[ExecuteCustomToolResponseSuccess, _Mapping]] = ..., error: _Optional[_Union[ExecuteCustomToolResponseError, _Mapping]] = ...) -> None: ...
