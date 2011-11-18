# vim: tabstop=4 shiftwidth=4 softtabstop=4

from __future__ import absolute_import

from yubico import yubico

from keystonelight.backends import kvs


class YubicoIdentity(kvs.KvsIdentity):
    """Very basic identity based on Yubico."""

    def __init__(self, options, *args, **kwargs):
        super(YubicoIdentity, self).__init__(options, *args, **kwargs)

        self.client_id = options.get('yubico_client_id')
        self.secret_key = options.get('yubico_secret_key')

        self.yubico = yubico.Yubico(self.client_id, self.secret_key)

    def authenticate(self, otp, **kwargs):
        assert self.yubico.verify(otp)

        tenant_ref = self.get_tenant(otp[:12])
        user_ref = self.get_user(otp[:12])

        extras = {
            'is_admin': False}

        return (tenant_ref, user_ref, extras)
