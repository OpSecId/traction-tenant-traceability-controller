from typing import Union, List, Dict
from pydantic import BaseModel, Field, AliasChoices, field_validator


class ReferenceRegulation(BaseModel):
    id: str = Field('https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96293_01')
    name: str = Field('Petrolium and Natural Gas Act')
    issuingBody: str = Field()

class SubjectFacility(BaseModel):
    ''' Tract or Well '''
    type: str = Field()
    id: str = Field()
    locations: List[str] = Field()
    rightsIncluded: List[str] = Field()
    rightsExcluded: List[str] = Field()
    notes: List[str] = Field()
    
class SubjectProducts(BaseModel):
    ''' Petrolium or NaturalGas '''
    type: str = Field()
    
class Assessment(BaseModel):
    topic: str = Field('Governance.Compliance')