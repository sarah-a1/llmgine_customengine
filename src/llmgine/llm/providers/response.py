# parsing a response for a unified interface


import logging
from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from llmgine.llm.tools.toolCall import ToolCall

# Set up logging
logger = logging.getLogger(__name__)


@dataclass
class ResponseTokens:
    # TODO: better structure, cost calculation, etc
    prompt_tokens: Optional[int] = None
    reasoning_tokens: Optional[int] = None
    completion_tokens: Optional[int] = None
    total_tokens: Optional[int] = None


@dataclass
class ResponseMetrics:
    # TODO: better structure, cost calculation, etc
    tokens: Optional[ResponseTokens] = None
    cost: Optional[float] = None
    ttf: Optional[float] = None
    tps: Optional[float] = None


# Base class for LLM responses
class LLMResponse:
    def __init__(self, raw_response: Any):
        self.raw = raw_response

    @property
    def content(self) -> str:
        raise NotImplementedError

    @property
    def tool_calls(self) -> List[ToolCall]:
        raise NotImplementedError

    @property
    def has_tool_calls(self) -> bool:
        raise NotImplementedError

    @property
    def finish_reason(self) -> str:
        raise NotImplementedError

    @property
    def tokens(self) -> ResponseTokens:
        raise NotImplementedError

    @property
    def metrics(self) -> Dict[str, Any]:
        raise NotImplementedError

    @property
    def model(self) -> Dict[str, Any]:
        raise NotImplementedError

    @property
    def reasoning(self) -> str:
        raise NotImplementedError
