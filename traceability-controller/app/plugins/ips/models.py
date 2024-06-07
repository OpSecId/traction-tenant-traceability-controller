from typing import Union, List, Dict
from pydantic import BaseModel, Field, AliasChoices, field_validator
from app.validations import (
    ValidationException,
    valid_xml_timestamp,
    valid_credential_subject,
    valid_issuer,
    valid_type,
    valid_context_v1,
    valid_status_update_value,
    valid_status_purpose
)
from .proofs import Proof


class Organization(BaseModel):
    type: str =  Field(None)
    url: str =  Field(None)
    name: str =  Field(None)
    description: str = Field(None)

class Issuer(BaseModel):
    type: str =  Field(None)
    id: str = Field(None)
    url: str =  Field(None)
    name: str = Field(None)
    description: str = Field(None)
    memberOf: Organization = Field(None)


class Tract(BaseModel):
    id: str = Field(None)
    locations: List[str] = Field()
    rightsIncluded: List[str] = Field(None)
    rightsExcluded: List[str] = Field(None)
    notes: List[str] = Field(None)


class TitleHolder(BaseModel):
    id: str = Field(None)
    url: str = Field(None)
    name: str = Field(None)
    interest: float = Field(None)


class TitleOrigin(BaseModel):
    type: str = Field(None)
    identifier: str = Field(None)


class TenureTitle(BaseModel):
    type: str = Field(None)
    identifier: str = Field(None)
    origin: TitleOrigin = Field(None)
    validFrom: str = Field(None)
    issuanceDate: str = Field(None)
    expirationDate: str = Field(None)
    wells: List[str] = Field(None)
    tracts: List[Tract] = Field(None)
    caveats: List[str] = Field(None)
    holders: List[TitleHolder] = Field(None)


class BitstringStatuslistEntry(BaseModel):
    type: str = Field(None)
    id: str = Field()


class TermsOfUse(BaseModel):
    type: str = Field(None)
    id: str = Field()


class RenderMethod(BaseModel):
    type: str = Field(None)
    id: str = Field()


class UNTPConformityCredential(BaseModel):
    context: List[str] = Field([''])
    type: List[str] = Field(['VerifiableCredential', 'ConformityCredential'])
    id: str = Field()
    issuer: Issuer = Field()
    credentialSubject: TenureTitle = Field()
    credentialStatus: List[BitstringStatuslistEntry] = Field()
    renderMethod: List[RenderMethod] = Field()
    termsOfUse: TermsOfUse = Field()