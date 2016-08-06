from extensions import db
from flask.ext.security import UserMixin, RoleMixin
import datetime

# Define models
roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __unicode__(self):
        return '%s' % self.name


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean(), default=False)
    confirmed_at = db.Column(db.DateTime())
    created_at = db.Column(db.DateTime(), default=datetime.datetime.now)
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))
    username = db.Column(db.String(255))
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(255))
    current_login_ip = db.Column(db.String(255))
    login_count = db.Column(db.Integer())

    def __unicode__(self):
        return '%s_%s' % (self.email, str(self.id))

    def __repr__(self):
        return "%s %s %s" % (self.username, self.id, self.email)

    def get_id(self):
        return unicode(self.id)

