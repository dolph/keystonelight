from keystonelight import models
from keystonelight import test
from keystonelight.backends import yubico


class YubicoIdentity(test.TestCase):
  def setUp(self):
    super(YubicoIdentity, self).setUp()
    self.options = self.appconfig('yubico_backend')

    self.identity_api = yubico.YubicoIdentity(options=self.options, db={})
    self._load_fixtures()

  def _load_fixtures(self):
    self.tenant_bar = self.identity_api.create_tenant(
        'bar',
        models.Tenant(id='bar', name='BAR'))
    self.user_foo = self.identity_api.create_user(
        'foo',
        models.User(id='foo',
                    name='FOO',
                    password='foo2',
                    tenants=[self.tenant_bar['id']]))
    self.extras_foobar = self.identity_api.create_extras(
        'foo', 'bar',
        {'extra': 'extra'})

  def test_authenticate_otp(self):
    user_ref, tenant_ref, extras_ref = self.identity_api.authenticate(
        'ccccccclvlvnklluikcbtfflfrnjifvnvetftblrhhui')
    self.assertEquals(user_ref['id'], 'ccccccclvlvn')
