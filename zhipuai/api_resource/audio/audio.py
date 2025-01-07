from __future__ import annotations

from typing import TYPE_CHECKING, List, Mapping, cast, Optional, Dict

from zhipuai.core._utils import extract_files

from zhipuai.types.sensitive_word_check import SensitiveWordCheckRequest
from zhipuai.types.audio import AudioSpeechParams
from ...types.audio import audio_customization_param

from zhipuai.core import BaseAPI, maybe_transform
from zhipuai.core import NOT_GIVEN, Body, Headers, NotGiven, FileTypes
from zhipuai.core import _legacy_response

import httpx

from zhipuai.core import (
    make_request_options,
)
from zhipuai.core import deepcopy_minimal

if TYPE_CHECKING:
    from zhipuai._client import ZhipuAI

__all__ = ["Audio"]


class Audio(BaseAPI):

    def __init__(self, client: "ZhipuAI") -> None:
        super().__init__(client)

    def speech(
            self,
            *,
            model: str,
            input: str = None,
            voice: str = None,
            response_format: str = None,
            sensitive_word_check: Optional[SensitiveWordCheckRequest] | NotGiven = NOT_GIVEN,
            request_id: str = None,
            user_id: str = None,
            extra_headers: Headers | None = None,
            extra_body: Body | None = None,
            timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> _legacy_response.HttpxBinaryResponseContent:
        body = deepcopy_minimal(
            {
                "model": model,
                "input": input,
                "voice": voice,
                "response_format": response_format,
                "sensitive_word_check": sensitive_word_check,
                "request_id": request_id,
                "user_id": user_id
            }
        )
        return self._post(
            "/audio/speech",
            body=maybe_transform(body, AudioSpeechParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_body=extra_body, timeout=timeout
            ),
            cast_type=_legacy_response.HttpxBinaryResponseContent
        )

    def customization(
            self,
            *,
            model: str,
            input: str = None,
            voice_text: str = None,
            voice_data: FileTypes = None,
            response_format: str = None,
            sensitive_word_check: Optional[SensitiveWordCheckRequest] | NotGiven = NOT_GIVEN,
            request_id: str = None,
            user_id: str = None,
            extra_headers: Headers | None = None,
            extra_body: Body | None = None,
            timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> _legacy_response.HttpxBinaryResponseContent:
        body = deepcopy_minimal(
            {
                "model": model,
                "input": input,
                "voice_text": voice_text,
                "voice_data": voice_data,
                "response_format": response_format,
                "sensitive_word_check": sensitive_word_check,
                "request_id": request_id,
                "user_id": user_id
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["voice_data"]])

        if files:
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/audio/customization",
            body=maybe_transform(body, audio_customization_param.AudioCustomizationParam),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_body=extra_body, timeout=timeout
            ),
            cast_type=_legacy_response.HttpxBinaryResponseContent
        )
