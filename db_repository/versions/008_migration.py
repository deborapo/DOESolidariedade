from sqlalchemy import *

pre_meta = MetaData()
post_meta = MetaData()

post = Table('imagens', post_meta,
    Column('idImagem', Integer, primary_key=True),
	Column('URLImagem', String(length=400)),
)

def upgrade(migrate_engine):
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['imagens'].create()


def downgrade(migrate_engine):
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['imagens'].drop()