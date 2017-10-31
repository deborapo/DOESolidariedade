from sqlalchemy import *

pre_meta = MetaData()
post_meta = MetaData()

post = Table('telefone_admin', post_meta,
    Column('idTelefone', Integer, primary_key=True),
	Column('num_telefone', String(length=14)),
)

def upgrade(migrate_engine):
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['telefone_admin'].create()


def downgrade(migrate_engine):
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['telefone_admin'].drop()