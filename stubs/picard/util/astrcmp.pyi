from picard.util._astrcmp import astrcmp as astrcmp_c

def astrcmp_py(a, b): ...

astrcmp = astrcmp_c
astrcmp_implementation: str
astrcmp = astrcmp_py
