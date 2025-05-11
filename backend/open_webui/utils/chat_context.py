from contextvars import ContextVar
temporarychatenabled: ContextVar[str] = ContextVar(
    "temporarychatenabled", default="false"
)

temporray_user_id: ContextVar[str] = ContextVar(
    "user_id", default=""
)