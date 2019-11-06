# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .device_authentication_mechanism_py3 import DeviceAuthenticationMechanism


class TpmDeviceAuthenticationMechanism(DeviceAuthenticationMechanism):
    """TpmDeviceAuthenticationMechanism.

    All required parameters must be populated in order to send to Azure.

    :param device_authentication_type: Required. Constant filled by server.
    :type device_authentication_type: str
    :param endorsement_key: Required. TPM endorsement key.
    :type endorsement_key: str
    :param storage_root_key: TPM storage root key.
    :type storage_root_key: str
    """

    _validation = {
        "device_authentication_type": {"required": True},
        "endorsement_key": {"required": True},
    }

    _attribute_map = {
        "device_authentication_type": {"key": "deviceAuthenticationType", "type": "str"},
        "endorsement_key": {"key": "endorsementKey", "type": "str"},
        "storage_root_key": {"key": "storageRootKey", "type": "str"},
    }

    def __init__(self, *, endorsement_key: str, storage_root_key: str = None, **kwargs) -> None:
        super(TpmDeviceAuthenticationMechanism, self).__init__(**kwargs)
        self.endorsement_key = endorsement_key
        self.storage_root_key = storage_root_key
        self.device_authentication_type = "TpmDeviceAuthenticationMechanism"