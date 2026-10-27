from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
)
from app.core.config import db_settings

_engine: AsyncEngine | None = None

# 创建引擎
def get_engine() -> AsyncEngine:
    global _engine

    if _engine is None:
        url = f"postgresql+asyncpg://{db_settings.user}:{db_settings.password}@{db_settings.host}:{db_settings.port}/{db_settings.name}"
        _engine = create_async_engine(
            url, pool_size=10, max_overflow=20, pool_pre_ping=True, echo=False
        )

    return _engine


_session_factory: async_sessionmaker[AsyncSession] | None = None

# 创建会话工厂
def get_session_factory() -> async_sessionmaker[AsyncSession]:
    global _session_factory

    if _session_factory is None:
        _session_factory = async_sessionmaker(
            get_engine(), # 会话工厂需要引擎来创建
            class_=AsyncSession,  # 明确指定使用异步 Session（默认）
            expire_on_commit=False,
        )

    return _session_factory
