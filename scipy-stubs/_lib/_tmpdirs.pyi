from _typeshed import FileDescriptorOrPath
from contextlib import _GeneratorContextManager

def tempdir() -> _GeneratorContextManager[str]: ...
def in_tempdir() -> _GeneratorContextManager[str]: ...
def in_dir(dir: FileDescriptorOrPath | None = None) -> _GeneratorContextManager[str]: ...
