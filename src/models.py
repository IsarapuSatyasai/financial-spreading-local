from pydantic import BaseModel, Field
from typing import Optional, List

class ExtractedAnswer(BaseModel):
    worksheet: str
    variable: str
    year: Optional[int] = None
    answer: str
    confidence: float = Field(ge=0.0, le=1.0)
    page_number: int = -1
    source_fields: List[str] = Field(default_factory=list)
    formula: Optional[str] = None

class ExtractionResponse(BaseModel):
    answers: List[ExtractedAnswer] = Field(default_factory=list)
    errors: List[str] = Field(default_factory=list)
