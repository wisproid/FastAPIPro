from typing import Union, Optional
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel
from datetime import datetime as dt

class BaseModelSchema(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        alias_generator=to_camel,
        populate_by_name=True,
        from_attributes=True,
        # alias_generator=AliasGenerator(
        #     validation_alias=to_camel,
        #     serialization_alias=to_camel,
        # ),
        json_encoders={
            # custom serializer for datetime to include timezone
            # ex. "2022-01-01T00:00:00+00:00"
            dt: lambda v: v.isoformat(),
        }
    )

class ResponseSchema(BaseModelSchema):
    status: str
    success: bool
    message: str
    version: str

class PaginationSchema(BaseModelSchema):
    page: Union[int, None] = None
    page_total: Union[int, None] = None
    page_size: Union[int, None] = None
    total_count: Union[int, None] = None

class ResponseExampleDataSchema(BaseModelSchema):
    file_name: str
    file_size: int
    lpn: str = ""
    lpn_score: int = -1
    lpn_bbox: list = []
    car_bbox: list = []
    car_score: int = -1
    # datetime_utc: Union[dt, None] = Field(examples=["2022-01-01T00:00:00+00:00"])
    # datetime: Union[dt, None] = Field(examples=["2022-01-01T07:00:00+07:00"])

class ResponseExampleSchema(ResponseSchema):
    data: ResponseExampleDataSchema
    pagination: Optional[PaginationSchema]