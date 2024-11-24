from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context

# Importuj modele
from models import Base  # Zakładając, że `Base` jest w models.py

config = context.config

# Interpretacja pliku konfiguracyjnego dla logowania
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Ustaw obiekt MetaData z Twoich modeli
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Przeprowadź migracje w trybie 'offline'."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Przeprowadź migracje w trybie 'online'."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
