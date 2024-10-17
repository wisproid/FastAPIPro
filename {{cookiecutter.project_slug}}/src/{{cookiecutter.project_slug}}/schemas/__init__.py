from typing import Union, Optional
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel
from datetime import datetime as dt

from {{cookiecutter.project_slug}}.version import version

class BaseModelSchema(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        alias_generator=to_camel,
        populate_by_name=True,
        from_attributes=True,
        use_enum_values=True,
        # alias_generator=AliasGenerator(
        #     validation_alias=to_camel,
        #     serialization_alias=to_camel,
        # ),
        json_encoders={
            # custom serializer for datetime to include timezone
            # ex. "2022-01-01T00:00:00+00:00"
            # dt: lambda v: v.isoformat()
            dt: lambda v: v.strftime('%Y-%m-%dT%H:%M:%S%Z')
        }
    )

class ResponseSchema(BaseModelSchema):
    status: str = "success"
    success: bool = True
    message: str = dt.now().strftime('%Y-%m-%dT%H:%M:%S+0000')
    version: str = version

class PaginationSchema(BaseModelSchema):
    page: Union[int, None] = None
    per_page: Union[int, None] = None
    total_page: Union[int, None] = None
    total_count: Union[int, None] = None

class ResponseExampleDataSchema(BaseModelSchema):
    file_name: str

class ResponseExampleSchema(ResponseSchema):
    data: ResponseExampleDataSchema
    pagination: Optional[PaginationSchema]