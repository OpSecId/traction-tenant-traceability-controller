from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse
from config import settings
from app.controllers.traction import TractionController
from app.controllers.askar import AskarController
from app.controllers import auth
from app.models.web_requests import (
    IssueCredentialSchema,
    UpdateCredentialStatusSchema,
    VerifyCredentialSchema,
)
from app.auth.bearer import JWTBearer
import uuid

router = APIRouter()


@router.get(
    "/credentials/tenure-titles/{title_id}",
    tags=["IPS"]
)
async def get_tenure_title_credential(title_id: str, request: Request):
    credential = {}
    return JSONResponse(status_code=200, content=credential)


@router.post(
    "/credentials/tenure-titles/{title_id}",
    tags=["IPS"],
    dependencies=[Depends(JWTBearer())]
)
async def issue_tenure_title_credential(title_id: str, request: Request):
    vc = {}
    return JSONResponse(status_code=201, content={'verifiableCredential': vc})