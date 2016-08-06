from flask.ext.script import Command, prompt, Option
from flask.ext.security.script import CreateUserCommand, AddRoleCommand
from flask_security.utils import encrypt_password
from user.models import Role, User
from extensions import db


class InstallCommand(Command):
    def run(self, **kwargs):
        db.create_all()
        # check if admin exists
        a = Role.query.filter_by(name='admin').first()
        if a is None:
            db.session.add(Role(name='admin'))
            db.session.commit()
            u = prompt('Admin Email?', default='admin@enferno.io')
            p = prompt('Admin Password (min 6 characters)?', default='enferno')
            CreateUserCommand().run(email=u, password=p, active=1)
            AddRoleCommand().run(user_identifier=u, role_name='admin')
        else:
            print 'Seems like an Admin is already installed'


class ResetUserCommand(Command):
    option_list = (
        Option('-e', '--email', dest='email', default=None),
        Option('-p', '--password', dest='password', default=None),
    )

    def run(self, **kwargs):
        try:
            pwd = encrypt_password(kwargs['password'])
            User.objects(email=kwargs['email']).first().update(set__password=pwd)
        except Exception, e:
            print ('Error resetting user password: %s' % e)
