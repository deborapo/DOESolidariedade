from sqlalchemy import *

pre_meta = MetaData()
post_meta = MetaData()

post = Table('usuario', post_meta,
    Column('idUsuario', Integer, primary_key=True),
	Column('nome', String(length=64)),
    Column('permissao', String(length=15)),
    Column('email', String(length=120)),
)

def upgrade(migrate_engine):
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['usuario'].create()


def downgrade(migrate_engine):
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['usuario'].drop()
