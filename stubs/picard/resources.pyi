from _typeshed import Incomplete

qt_resource_data: bytes
qt_resource_name: bytes
qt_resource_struct_v1: bytes
qt_resource_struct_v2: bytes
qt_version: Incomplete
rcc_version: int
qt_resource_struct = qt_resource_struct_v1
qt_resource_struct = qt_resource_struct_v2

def qInitResources() -> None: ...
def qCleanupResources() -> None: ...
