# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from typing import Any, AsyncIterator, Awaitable, Callable, Sequence, Tuple, Optional, Iterator

from google.cloud.notebooks_v1.types import environment
from google.cloud.notebooks_v1.types import execution
from google.cloud.notebooks_v1.types import instance
from google.cloud.notebooks_v1.types import schedule
from google.cloud.notebooks_v1.types import service


class ListInstancesPager:
    """A pager for iterating through ``list_instances`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.notebooks_v1.types.ListInstancesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``instances`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListInstances`` requests and continue to iterate
    through the ``instances`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.notebooks_v1.types.ListInstancesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., service.ListInstancesResponse],
            request: service.ListInstancesRequest,
            response: service.ListInstancesResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.notebooks_v1.types.ListInstancesRequest):
                The initial request object.
            response (google.cloud.notebooks_v1.types.ListInstancesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = service.ListInstancesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[service.ListInstancesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[instance.Instance]:
        for page in self.pages:
            yield from page.instances

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListInstancesAsyncPager:
    """A pager for iterating through ``list_instances`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.notebooks_v1.types.ListInstancesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``instances`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListInstances`` requests and continue to iterate
    through the ``instances`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.notebooks_v1.types.ListInstancesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., Awaitable[service.ListInstancesResponse]],
            request: service.ListInstancesRequest,
            response: service.ListInstancesResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.notebooks_v1.types.ListInstancesRequest):
                The initial request object.
            response (google.cloud.notebooks_v1.types.ListInstancesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = service.ListInstancesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[service.ListInstancesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response
    def __aiter__(self) -> AsyncIterator[instance.Instance]:
        async def async_generator():
            async for page in self.pages:
                for response in page.instances:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListEnvironmentsPager:
    """A pager for iterating through ``list_environments`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.notebooks_v1.types.ListEnvironmentsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``environments`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListEnvironments`` requests and continue to iterate
    through the ``environments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.notebooks_v1.types.ListEnvironmentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., service.ListEnvironmentsResponse],
            request: service.ListEnvironmentsRequest,
            response: service.ListEnvironmentsResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.notebooks_v1.types.ListEnvironmentsRequest):
                The initial request object.
            response (google.cloud.notebooks_v1.types.ListEnvironmentsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = service.ListEnvironmentsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[service.ListEnvironmentsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[environment.Environment]:
        for page in self.pages:
            yield from page.environments

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListEnvironmentsAsyncPager:
    """A pager for iterating through ``list_environments`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.notebooks_v1.types.ListEnvironmentsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``environments`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListEnvironments`` requests and continue to iterate
    through the ``environments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.notebooks_v1.types.ListEnvironmentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., Awaitable[service.ListEnvironmentsResponse]],
            request: service.ListEnvironmentsRequest,
            response: service.ListEnvironmentsResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.notebooks_v1.types.ListEnvironmentsRequest):
                The initial request object.
            response (google.cloud.notebooks_v1.types.ListEnvironmentsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = service.ListEnvironmentsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[service.ListEnvironmentsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response
    def __aiter__(self) -> AsyncIterator[environment.Environment]:
        async def async_generator():
            async for page in self.pages:
                for response in page.environments:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListSchedulesPager:
    """A pager for iterating through ``list_schedules`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.notebooks_v1.types.ListSchedulesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``schedules`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListSchedules`` requests and continue to iterate
    through the ``schedules`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.notebooks_v1.types.ListSchedulesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., service.ListSchedulesResponse],
            request: service.ListSchedulesRequest,
            response: service.ListSchedulesResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.notebooks_v1.types.ListSchedulesRequest):
                The initial request object.
            response (google.cloud.notebooks_v1.types.ListSchedulesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = service.ListSchedulesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[service.ListSchedulesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[schedule.Schedule]:
        for page in self.pages:
            yield from page.schedules

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListSchedulesAsyncPager:
    """A pager for iterating through ``list_schedules`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.notebooks_v1.types.ListSchedulesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``schedules`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListSchedules`` requests and continue to iterate
    through the ``schedules`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.notebooks_v1.types.ListSchedulesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., Awaitable[service.ListSchedulesResponse]],
            request: service.ListSchedulesRequest,
            response: service.ListSchedulesResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.notebooks_v1.types.ListSchedulesRequest):
                The initial request object.
            response (google.cloud.notebooks_v1.types.ListSchedulesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = service.ListSchedulesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[service.ListSchedulesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response
    def __aiter__(self) -> AsyncIterator[schedule.Schedule]:
        async def async_generator():
            async for page in self.pages:
                for response in page.schedules:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListExecutionsPager:
    """A pager for iterating through ``list_executions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.notebooks_v1.types.ListExecutionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``executions`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListExecutions`` requests and continue to iterate
    through the ``executions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.notebooks_v1.types.ListExecutionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., service.ListExecutionsResponse],
            request: service.ListExecutionsRequest,
            response: service.ListExecutionsResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.notebooks_v1.types.ListExecutionsRequest):
                The initial request object.
            response (google.cloud.notebooks_v1.types.ListExecutionsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = service.ListExecutionsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[service.ListExecutionsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[execution.Execution]:
        for page in self.pages:
            yield from page.executions

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListExecutionsAsyncPager:
    """A pager for iterating through ``list_executions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.notebooks_v1.types.ListExecutionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``executions`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListExecutions`` requests and continue to iterate
    through the ``executions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.notebooks_v1.types.ListExecutionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., Awaitable[service.ListExecutionsResponse]],
            request: service.ListExecutionsRequest,
            response: service.ListExecutionsResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.notebooks_v1.types.ListExecutionsRequest):
                The initial request object.
            response (google.cloud.notebooks_v1.types.ListExecutionsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = service.ListExecutionsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[service.ListExecutionsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response
    def __aiter__(self) -> AsyncIterator[execution.Execution]:
        async def async_generator():
            async for page in self.pages:
                for response in page.executions:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)
