from peewee import CharField, Model


class OrmMessage(Model):
    header = CharField()
    body = CharField()
