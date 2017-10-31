from sqlalchemy import *

pre_meta = MetaData()
post_meta = MetaData()

post = Table('organizacao', post_meta,
    Column('cnpj', String(length=15), primary_key=True),
    Column('representanteLegal', String(length=100)),
	Column('razaoSocial', String(length=400)),
	Column('dataFundacao', Date),
)

def upgrade(migrate_engine):
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['organizacao'].create()

def downgrade(migrate_engine):
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['organizacao'].drop()
