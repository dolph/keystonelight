# vim: tabstop=4 shiftwidth=4 softtabstop=4

from __future__ import absolute_import

from yubico import yubico

from keystonelight.backends import kvs


class YubicoIdentity(kvs.KvsIdentity):
    """Very basic identity based on Yubico."""

    def __init__(self, *args, **kwargs):
        super(YubicoIdentity, self).__init__(*args, **kwargs)
        self.yubico = yubico.Yubico('6634', 'HdRb8AA24+Ud8VL2E+sEEZUiySg=')

    def authenticate(self, otp, **kwargs):
        assert self.yubico.verify(otp)

        extras = {
            'id_admin': False}
        tenant = {
            'id': otp[:12],
            'name': otp[:12]}
        user = {
            'id': otp[:12],
            'name': otp[:12]}

        return (tenant, user, extras)
