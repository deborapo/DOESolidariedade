from sqlalchemy import *

pre_meta = MetaData()
post_meta = MetaData()
post = Table('relatorio', post_meta,
    Column('idRelatorio', Integer, primary_key=True),
	Column('descricaoR', String(length=5000)),
    Column('tipo', String(length=200)),
)

def upgrade(migrate_engine):
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['relatorio'].create()


def downgrade(migrate_engine):
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['relatorio'].drop()
