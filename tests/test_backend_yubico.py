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
    self.tenant_yubico = self.identity_api.create_tenant(
        'ccccccclvlvn',
        models.Tenant(id='ccccccclvlvn', name='Yubico Sample Fob'))
    self.user_yubico = self.identity_api.create_user(
        'ccccccclvlvn',
        models.User(id='ccccccclvlvn',
                    name='Yubico Sample Fob',
                    tenants=[self.tenant_yubico['id']]))

  def test_authenticate_otp(self):
    # This needs to be regenerated by a yubi, since it's one time use...
    user_ref, tenant_ref, extras_ref = self.identity_api.authenticate(
        'ccccccclvlvndivnlntjfldfrvfkruggfngeelevhgvr')

    self.assertEquals(tenant_ref['id'], self.tenant_yubico['id'])
    self.assertEquals(user_ref['id'], self.user_yubico['id'])
