# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
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
import abc
from typing import Awaitable, Callable, Dict, Optional, Sequence, Union

import google.api_core
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, operations_v1
from google.api_core import retry as retries
import google.auth  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.oauth2 import service_account  # type: ignore
import pkg_resources

from google.cloud.notebooks_v1.types import managed_service, runtime

try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            "google-cloud-notebooks",
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


class ManagedNotebookServiceTransport(abc.ABC):
    """Abstract transport class for ManagedNotebookService."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    DEFAULT_HOST: str = "notebooks.googleapis.com"

    def __init__(
        self,
        *,
        host: str = DEFAULT_HOST,
        credentials: ga_credentials.Credentials = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        **kwargs,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scopes (Optional[Sequence[str]]): A list of scopes.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
        """

        # Save the hostname. Default to port 443 (HTTPS) if none is specified.
        if ":" not in host:
            host += ":443"
        self._host = host

        scopes_kwargs = {"scopes": scopes, "default_scopes": self.AUTH_SCOPES}

        # Save the scopes.
        self._scopes = scopes

        # If no credentials are provided, then determine the appropriate
        # defaults.
        if credentials and credentials_file:
            raise core_exceptions.DuplicateCredentialArgs(
                "'credentials_file' and 'credentials' are mutually exclusive"
            )

        if credentials_file is not None:
            credentials, _ = google.auth.load_credentials_from_file(
                credentials_file, **scopes_kwargs, quota_project_id=quota_project_id
            )
        elif credentials is None:
            credentials, _ = google.auth.default(
                **scopes_kwargs, quota_project_id=quota_project_id
            )

        # If the credentials are service account credentials, then always try to use self signed JWT.
        if (
            always_use_jwt_access
            and isinstance(credentials, service_account.Credentials)
            and hasattr(service_account.Credentials, "with_always_use_jwt_access")
        ):
            credentials = credentials.with_always_use_jwt_access(True)

        # Save the credentials.
        self._credentials = credentials

    def _prep_wrapped_messages(self, client_info):
        # Precompute the wrapped methods.
        self._wrapped_methods = {
            self.list_runtimes: gapic_v1.method.wrap_method(
                self.list_runtimes,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_runtime: gapic_v1.method.wrap_method(
                self.get_runtime,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_runtime: gapic_v1.method.wrap_method(
                self.create_runtime,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_runtime: gapic_v1.method.wrap_method(
                self.delete_runtime,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.start_runtime: gapic_v1.method.wrap_method(
                self.start_runtime,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.stop_runtime: gapic_v1.method.wrap_method(
                self.stop_runtime,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.switch_runtime: gapic_v1.method.wrap_method(
                self.switch_runtime,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.reset_runtime: gapic_v1.method.wrap_method(
                self.reset_runtime,
                default_timeout=None,
                client_info=client_info,
            ),
            self.report_runtime_event: gapic_v1.method.wrap_method(
                self.report_runtime_event,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.refresh_runtime_token_internal: gapic_v1.method.wrap_method(
                self.refresh_runtime_token_internal,
                default_timeout=None,
                client_info=client_info,
            ),
        }

    def close(self):
        """Closes resources associated with the transport.

        .. warning::
             Only call this method if the transport is NOT shared
             with other clients - this may cause errors in other clients!
        """
        raise NotImplementedError()

    @property
    def operations_client(self):
        """Return the client designed to process long-running operations."""
        raise NotImplementedError()

    @property
    def list_runtimes(
        self,
    ) -> Callable[
        [managed_service.ListRuntimesRequest],
        Union[
            managed_service.ListRuntimesResponse,
            Awaitable[managed_service.ListRuntimesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_runtime(
        self,
    ) -> Callable[
        [managed_service.GetRuntimeRequest],
        Union[runtime.Runtime, Awaitable[runtime.Runtime]],
    ]:
        raise NotImplementedError()

    @property
    def create_runtime(
        self,
    ) -> Callable[
        [managed_service.CreateRuntimeRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_runtime(
        self,
    ) -> Callable[
        [managed_service.DeleteRuntimeRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def start_runtime(
        self,
    ) -> Callable[
        [managed_service.StartRuntimeRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def stop_runtime(
        self,
    ) -> Callable[
        [managed_service.StopRuntimeRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def switch_runtime(
        self,
    ) -> Callable[
        [managed_service.SwitchRuntimeRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def reset_runtime(
        self,
    ) -> Callable[
        [managed_service.ResetRuntimeRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def report_runtime_event(
        self,
    ) -> Callable[
        [managed_service.ReportRuntimeEventRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def refresh_runtime_token_internal(
        self,
    ) -> Callable[
        [managed_service.RefreshRuntimeTokenInternalRequest],
        Union[
            managed_service.RefreshRuntimeTokenInternalResponse,
            Awaitable[managed_service.RefreshRuntimeTokenInternalResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def kind(self) -> str:
        raise NotImplementedError()


__all__ = ("ManagedNotebookServiceTransport",)
