from sqlalchemy import *

pre_meta = MetaData()
post_meta = MetaData()

post = Table('administrador', post_meta,
    Column('cpf', String(length=15), primary_key=True),
    Column('dataNasc', Date),
)

def upgrade(migrate_engine):
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['administrador'].create()


def downgrade(migrate_engine):
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['administrador'].drop()
