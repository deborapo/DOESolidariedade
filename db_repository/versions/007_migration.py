from sqlalchemy import *

pre_meta = MetaData()
post_meta = MetaData()

post = Table('publicacao', post_meta,
    Column('idPublicacao', Integer, primary_key=True),
	Column('autor', String(length=100)),
    Column('titulo', String(length=200)),
    Column('conteudo', String(length=10000)),
)

def upgrade(migrate_engine):
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['publicacao'].create()


def downgrade(migrate_engine):
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['publicacao'].drop()