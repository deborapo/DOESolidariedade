from app import db

class Usuario(db.Model):
    __table_args__ = {'extend_existing': True}
    idUsuario = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(64), index=True)
    permissao = db.Column(db.String(15))
    email = db.Column(db.String(120), index=True)

    #relacionamentos
    administrador = db.relationship('Administrador', backref='user-admin', lazy='dynamic')
    organizacao = db.relationship('Organizacao', backref='user-org', lazy='dynamic')

    def __repr__(self):
        return '<Usuario %r %r %r>' % (self.nome,self.permissao,self.email)

class Administrador(db.Model):
    __table_args__ = {'extend_existing': True}
    cpf = db.Column(db.String(15), primary_key=True)
    dataNasc = db.Column(db.Date)

    # chaves estrangeiras
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.idUsuario'))

    # relacionamentos
    telefone = db.relationship('Telefone_Admin', backref='admin-tel', lazy='dynamic')
    relatorio = db.relationship('Relatorio', backref='admin-rel', lazy='dynamic')
    gerenciamento = db.relationship('Gerenciamento', backref='admin-ger', lazy='dynamic')

    def __repr__(self):
        return '<Administrador %r %r>' % (self.cpf,self.dataNasc)

class Organizacao(db.Model):
    __table_args__ = {'extend_existing': True}
    cnpj =  db.Column(db.String(15), primary_key=True)
    representanteLegal = db.Column(db.String(100))
    razaoSocial = db.Column(db.String(400))
    dataFundacao = db.Column(db.Date)

    # chaves estrangeiras
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.idUsuario'))
    gerenciamento_id = db.Column(db.Integer, db.ForeignKey('gerenciamento.idGerenciamento'))

    # relacionamentos
    telefone = db.relationship('Telefone_Orgn', backref='orgn-tel', lazy='dynamic')
    endereco = db.relationship('Endereco', backref='orgn-end', lazy='dynamic')
    imagens = db.relationship('Imagens', backref='orgn-img', lazy='dynamic')
    publicacao = db.relationship('Publicacao', backref='orgn-public', lazy='dynamic')

    def __repr__(self):
        return '<Organizacao %r %r %r>' % (self.representanteLegal,self.razaoSocial,self.dataFundacao)

class Gerenciamento(db.Model):
    __table_args__ = {'extend_existing': True}
    idGerenciamento = db.Column(db.Integer, primary_key=True)
    descricaoG = db.Column(db.String(5000))

    #chave estrangeira
    administrador_id = db.Column(db.String(15),db.ForeignKey('administrador.cpf'))

    #relacionamentos
    organizacoes = db.relationship('Organizacao', backref='geren-orgn', lazy='dynamic')

    def __repr__(self):
        return '<Gerenciamento %r>' % (self.descricaoG)

class Relatorio(db.Model):
    __table_args__ = {'extend_existing': True}
    idRelatorio = db.Column(db.Integer, primary_key=True)
    descricaoR = db.Column(db.String(5000))
    tipo =  db.Column(db.String(200))

    #chaves estrangeiras
    administrador_id = db.Column(db.String(15), db.ForeignKey('administrador.cpf'))

    def __repr__(self):
        return '<Relatorio %r %r>' % (self.tipo,self.descricaoR)

class Telefone_Admin(db.Model):
    __table_args__ = {'extend_existing': True}
    idTelefone = db.Column(db.Integer, primary_key=True)
    num_telefone = db.Column(db.String(14))

    # chaves estrangeiras
    administrador_id = db.Column(db.String(15), db.ForeignKey('administrador.cpf'))

    def __repr__(self):
        return '<Telefone_Admin %r %r>' % (self.num_telefone)

class Publicacao(db.Model):
    __table_args__ = {'extend_existing': True}
    idPublicacao = db.Column(db.Integer, primary_key=True)
    autor = db.Column(db.String(100))
    titulo = db.Column(db.String(200))
    conteudo = db.Column(db.String(10000))

    #Chaves estrangeiras
    organizacao_id = db.Column(db.String(15), db.ForeignKey('organizacao.cnpj'))

    #relacionamentos
    imagens = db.relationship('Imagens', backref='public-img', lazy='dynamic')

    def __repr__(self):
        return '<Publicacao %r %r %r>' % (self.autor,self.titulo,self.conteudo)

class Imagens(db.Model):
    __table_args__ = {'extend_existing': True}
    idImagem = db.Column(db.Integer, primary_key=True)
    URLimagem = db.Column(db.String(400))

    #chaves estrangeiras
    publicacao_id = db.Column(db.Integer, db.ForeignKey('publicacao.idPublicacao'))
    organizacao_id = db.Column(db.String,db.ForeignKey('organizacao.cnpj'))

    def __repr__(self):
        return '<Imagens %r>' % (self.URLimagem)

class Telefone_Orgn(db.Model):
    __table_args__ = {'extend_existing': True}
    idTelefone = db.Column(db.Integer, primary_key=True)
    num_telefone = db.Column(db.String(14))

    # chaves estrangeiras
    organizacao_id = db.Column(db.String(15), db.ForeignKey('organizacao.cnpj'))

    def __repr__(self):
        return '<Telefone_Orgn %r>' % (self.num_telefone)

class Endereco(db.Model):
    __table_args__ = {'extend_existing': True}
    idEndereco = db.Column(db.Integer, primary_key=True)
    cidade = db.Column(db.String(45))
    uf = db.Column(db.String(2))
    cep = db.Column(db.String(9))
    complemento = db.Column(db.String(200))
    bairro = db.Column(db.String(40))
    rua = db.Column(db.String(100))
    numero = db.Column(db.Integer)

    # chaves estrangeiras
    organizacao_id =  db.Column(db.String(15),db.ForeignKey('organizacao.cnpj'))

    def __repr__(self):
        return '<Endereco %r %r %r %r %r %r %r>' % (self.rua,self.numero,self.bairro,self.complemento,self.cidade,self.uf,self.cep)

