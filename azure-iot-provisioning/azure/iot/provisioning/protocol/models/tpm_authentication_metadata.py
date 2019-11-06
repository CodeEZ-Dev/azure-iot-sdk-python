# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .authentication_metadata import AuthenticationMetadata


class TpmAuthenticationMetadata(AuthenticationMetadata):
    """TpmAuthenticationMetadata.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param authentication_metadata_type: Required. Constant filled by server.
    :type authentication_metadata_type: str
    :ivar endorsement_key: Tpm endorsement key.
    :vartype endorsement_key: str
    :ivar storage_root_key: Tpm storage root key.
    :vartype storage_root_key: str
    """

    _validation = {
        "authentication_metadata_type": {"required": True},
        "endorsement_key": {"readonly": True},
        "storage_root_key": {"readonly": True},
    }

    _attribute_map = {
        "authentication_metadata_type": {"key": "authenticationMetadataType", "type": "str"},
        "endorsement_key": {"key": "endorsementKey", "type": "str"},
        "storage_root_key": {"key": "storageRootKey", "type": "str"},
    }

    def __init__(self, **kwargs):
        super(TpmAuthenticationMetadata, self).__init__(**kwargs)
        self.endorsement_key = None
        self.storage_root_key = None
        self.authentication_metadata_type = "TpmAuthenticationMetadata"