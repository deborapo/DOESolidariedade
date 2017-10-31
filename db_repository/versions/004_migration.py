from sqlalchemy import *

pre_meta = MetaData()
post_meta = MetaData()
post = Table('gerenciamento', post_meta,
    Column('idGerenciamento', Integer, primary_key=True),
    Column('descricaoG', String(length=5000)),
)

def upgrade(migrate_engine):
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['gerenciamento'].create()


def downgrade(migrate_engine):
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['gerenciamento'].drop()
