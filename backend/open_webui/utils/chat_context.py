from contextvars import ContextVar
temporarychatenabled: ContextVar[str] = ContextVar(
    "temporarychatenabled", default="false"
)
