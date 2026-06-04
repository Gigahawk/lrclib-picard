from _typeshed import Incomplete

def port_from_qurl(qurl): ...
def hostkey_from_url(url): ...
def host_port_to_url(
    host,
    port,
    path: Incomplete | None = None,
    scheme: Incomplete | None = None,
    as_string: bool = False,
): ...
