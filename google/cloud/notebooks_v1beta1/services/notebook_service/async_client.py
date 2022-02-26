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
from collections import OrderedDict
import functools
import re
from typing import Dict, Optional, Sequence, Tuple, Type, Union
import pkg_resources

from google.api_core.client_options import ClientOptions
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore

from google.api_core import operation  # type: ignore
from google.api_core import operation_async  # type: ignore
from google.cloud.notebooks_v1beta1.services.notebook_service import pagers
from google.cloud.notebooks_v1beta1.types import environment
from google.cloud.notebooks_v1beta1.types import instance
from google.cloud.notebooks_v1beta1.types import service
from google.protobuf import empty_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore
from .transports.base import NotebookServiceTransport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import NotebookServiceGrpcAsyncIOTransport
from .client import NotebookServiceClient


class NotebookServiceAsyncClient:
    """API v1beta1 service for Cloud AI Platform Notebooks."""

    _client: NotebookServiceClient

    DEFAULT_ENDPOINT = NotebookServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = NotebookServiceClient.DEFAULT_MTLS_ENDPOINT

    environment_path = staticmethod(NotebookServiceClient.environment_path)
    parse_environment_path = staticmethod(NotebookServiceClient.parse_environment_path)
    instance_path = staticmethod(NotebookServiceClient.instance_path)
    parse_instance_path = staticmethod(NotebookServiceClient.parse_instance_path)
    common_billing_account_path = staticmethod(
        NotebookServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        NotebookServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(NotebookServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        NotebookServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        NotebookServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        NotebookServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(NotebookServiceClient.common_project_path)
    parse_common_project_path = staticmethod(
        NotebookServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(NotebookServiceClient.common_location_path)
    parse_common_location_path = staticmethod(
        NotebookServiceClient.parse_common_location_path
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            NotebookServiceAsyncClient: The constructed client.
        """
        return NotebookServiceClient.from_service_account_info.__func__(NotebookServiceAsyncClient, info, *args, **kwargs)  # type: ignore

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            NotebookServiceAsyncClient: The constructed client.
        """
        return NotebookServiceClient.from_service_account_file.__func__(NotebookServiceAsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: Optional[ClientOptions] = None
    ):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variabel is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        return NotebookServiceClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> NotebookServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            NotebookServiceTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(
        type(NotebookServiceClient).get_transport_class, type(NotebookServiceClient)
    )

    def __init__(
        self,
        *,
        credentials: ga_credentials.Credentials = None,
        transport: Union[str, NotebookServiceTransport] = "grpc_asyncio",
        client_options: ClientOptions = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the notebook service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.NotebookServiceTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = NotebookServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def list_instances(
        self,
        request: Union[service.ListInstancesRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListInstancesAsyncPager:
        r"""Lists instances in a given project and location.

        .. code-block:: python

            from google.cloud import notebooks_v1beta1

            def sample_list_instances():
                # Create a client
                client = notebooks_v1beta1.NotebookServiceClient()

                # Initialize request argument(s)
                request = notebooks_v1beta1.ListInstancesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_instances(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.notebooks_v1beta1.types.ListInstancesRequest, dict]):
                The request object. Request for listing notebook
                instances.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.notebooks_v1beta1.services.notebook_service.pagers.ListInstancesAsyncPager:
                Response for listing notebook
                instances.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        request = service.ListInstancesRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_instances,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListInstancesAsyncPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_instance(
        self,
        request: Union[service.GetInstanceRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> instance.Instance:
        r"""Gets details of a single Instance.

        .. code-block:: python

            from google.cloud import notebooks_v1beta1

            def sample_get_instance():
                # Create a client
                client = notebooks_v1beta1.NotebookServiceClient()

                # Initialize request argument(s)
                request = notebooks_v1beta1.GetInstanceRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_instance(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.notebooks_v1beta1.types.GetInstanceRequest, dict]):
                The request object. Request for getting a notebook
                instance.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.notebooks_v1beta1.types.Instance:
                The definition of a notebook
                instance.

        """
        # Create or coerce a protobuf request object.
        request = service.GetInstanceRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_instance,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def create_instance(
        self,
        request: Union[service.CreateInstanceRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Creates a new Instance in a given project and
        location.


        .. code-block:: python

            from google.cloud import notebooks_v1beta1

            def sample_create_instance():
                # Create a client
                client = notebooks_v1beta1.NotebookServiceClient()

                # Initialize request argument(s)
                instance = notebooks_v1beta1.Instance()
                instance.vm_image.image_name = "image_name_value"
                instance.vm_image.project = "project_value"
                instance.machine_type = "machine_type_value"

                request = notebooks_v1beta1.CreateInstanceRequest(
                    parent="parent_value",
                    instance_id="instance_id_value",
                    instance=instance,
                )

                # Make the request
                operation = client.create_instance(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.notebooks_v1beta1.types.CreateInstanceRequest, dict]):
                The request object. Request for creating a notebook
                instance.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.notebooks_v1beta1.types.Instance`
                The definition of a notebook instance.

        """
        # Create or coerce a protobuf request object.
        request = service.CreateInstanceRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_instance,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            instance.Instance,
            metadata_type=service.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def register_instance(
        self,
        request: Union[service.RegisterInstanceRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Registers an existing legacy notebook instance to the
        Notebooks API server. Legacy instances are instances
        created with the legacy Compute Engine calls. They are
        not manageable by the Notebooks API out of the box. This
        call makes these instances manageable by the Notebooks
        API.


        .. code-block:: python

            from google.cloud import notebooks_v1beta1

            def sample_register_instance():
                # Create a client
                client = notebooks_v1beta1.NotebookServiceClient()

                # Initialize request argument(s)
                request = notebooks_v1beta1.RegisterInstanceRequest(
                    parent="parent_value",
                    instance_id="instance_id_value",
                )

                # Make the request
                operation = client.register_instance(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.notebooks_v1beta1.types.RegisterInstanceRequest, dict]):
                The request object. Request for registering a notebook
                instance.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.notebooks_v1beta1.types.Instance`
                The definition of a notebook instance.

        """
        # Create or coerce a protobuf request object.
        request = service.RegisterInstanceRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.register_instance,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            instance.Instance,
            metadata_type=service.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def set_instance_accelerator(
        self,
        request: Union[service.SetInstanceAcceleratorRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Updates the guest accelerators of a single Instance.

        .. code-block:: python

            from google.cloud import notebooks_v1beta1

            def sample_set_instance_accelerator():
                # Create a client
                client = notebooks_v1beta1.NotebookServiceClient()

                # Initialize request argument(s)
                request = notebooks_v1beta1.SetInstanceAcceleratorRequest(
                    name="name_value",
                    type_="TPU_V3",
                    core_count=1073,
                )

                # Make the request
                operation = client.set_instance_accelerator(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.notebooks_v1beta1.types.SetInstanceAcceleratorRequest, dict]):
                The request object. Request for setting instance
                accelerator.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.notebooks_v1beta1.types.Instance`
                The definition of a notebook instance.

        """
        # Create or coerce a protobuf request object.
        request = service.SetInstanceAcceleratorRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.set_instance_accelerator,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            instance.Instance,
            metadata_type=service.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def set_instance_machine_type(
        self,
        request: Union[service.SetInstanceMachineTypeRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Updates the machine type of a single Instance.

        .. code-block:: python

            from google.cloud import notebooks_v1beta1

            def sample_set_instance_machine_type():
                # Create a client
                client = notebooks_v1beta1.NotebookServiceClient()

                # Initialize request argument(s)
                request = notebooks_v1beta1.SetInstanceMachineTypeRequest(
                    name="name_value",
                    machine_type="machine_type_value",
                )

                # Make the request
                operation = client.set_instance_machine_type(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.notebooks_v1beta1.types.SetInstanceMachineTypeRequest, dict]):
                The request object. Request for setting instance machine
                type.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.notebooks_v1beta1.types.Instance`
                The definition of a notebook instance.

        """
        # Create or coerce a protobuf request object.
        request = service.SetInstanceMachineTypeRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.set_instance_machine_type,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            instance.Instance,
            metadata_type=service.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def set_instance_labels(
        self,
        request: Union[service.SetInstanceLabelsRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Updates the labels of an Instance.

        .. code-block:: python

            from google.cloud import notebooks_v1beta1

            def sample_set_instance_labels():
                # Create a client
                client = notebooks_v1beta1.NotebookServiceClient()

                # Initialize request argument(s)
                request = notebooks_v1beta1.SetInstanceLabelsRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.set_instance_labels(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.notebooks_v1beta1.types.SetInstanceLabelsRequest, dict]):
                The request object. Request for setting instance labels.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.notebooks_v1beta1.types.Instance`
                The definition of a notebook instance.

        """
        # Create or coerce a protobuf request object.
        request = service.SetInstanceLabelsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.set_instance_labels,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            instance.Instance,
            metadata_type=service.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def delete_instance(
        self,
        request: Union[service.DeleteInstanceRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Deletes a single Instance.

        .. code-block:: python

            from google.cloud import notebooks_v1beta1

            def sample_delete_instance():
                # Create a client
                client = notebooks_v1beta1.NotebookServiceClient()

                # Initialize request argument(s)
                request = notebooks_v1beta1.DeleteInstanceRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_instance(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.notebooks_v1beta1.types.DeleteInstanceRequest, dict]):
                The request object. Request for deleting a notebook
                instance.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated
                   empty messages in your APIs. A typical example is to
                   use it as the request or the response type of an API
                   method. For instance:

                      service Foo {
                         rpc Bar(google.protobuf.Empty) returns
                         (google.protobuf.Empty);

                      }

                   The JSON representation for Empty is empty JSON
                   object {}.

        """
        # Create or coerce a protobuf request object.
        request = service.DeleteInstanceRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_instance,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=service.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def start_instance(
        self,
        request: Union[service.StartInstanceRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Starts a notebook instance.

        .. code-block:: python

            from google.cloud import notebooks_v1beta1

            def sample_start_instance():
                # Create a client
                client = notebooks_v1beta1.NotebookServiceClient()

                # Initialize request argument(s)
                request = notebooks_v1beta1.StartInstanceRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.start_instance(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.notebooks_v1beta1.types.StartInstanceRequest, dict]):
                The request object. Request for starting a notebook
                instance
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.notebooks_v1beta1.types.Instance`
                The definition of a notebook instance.

        """
        # Create or coerce a protobuf request object.
        request = service.StartInstanceRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.start_instance,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            instance.Instance,
            metadata_type=service.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def stop_instance(
        self,
        request: Union[service.StopInstanceRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Stops a notebook instance.

        .. code-block:: python

            from google.cloud import notebooks_v1beta1

            def sample_stop_instance():
                # Create a client
                client = notebooks_v1beta1.NotebookServiceClient()

                # Initialize request argument(s)
                request = notebooks_v1beta1.StopInstanceRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.stop_instance(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.notebooks_v1beta1.types.StopInstanceRequest, dict]):
                The request object. Request for stopping a notebook
                instance
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.notebooks_v1beta1.types.Instance`
                The definition of a notebook instance.

        """
        # Create or coerce a protobuf request object.
        request = service.StopInstanceRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.stop_instance,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            instance.Instance,
            metadata_type=service.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def reset_instance(
        self,
        request: Union[service.ResetInstanceRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Resets a notebook instance.

        .. code-block:: python

            from google.cloud import notebooks_v1beta1

            def sample_reset_instance():
                # Create a client
                client = notebooks_v1beta1.NotebookServiceClient()

                # Initialize request argument(s)
                request = notebooks_v1beta1.ResetInstanceRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.reset_instance(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.notebooks_v1beta1.types.ResetInstanceRequest, dict]):
                The request object. Request for reseting a notebook
                instance
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.notebooks_v1beta1.types.Instance`
                The definition of a notebook instance.

        """
        # Create or coerce a protobuf request object.
        request = service.ResetInstanceRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.reset_instance,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            instance.Instance,
            metadata_type=service.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def report_instance_info(
        self,
        request: Union[service.ReportInstanceInfoRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Allows notebook instances to
        report their latest instance information to the
        Notebooks API server. The server will merge the reported
        information to the instance metadata store. Do not use
        this method directly.


        .. code-block:: python

            from google.cloud import notebooks_v1beta1

            def sample_report_instance_info():
                # Create a client
                client = notebooks_v1beta1.NotebookServiceClient()

                # Initialize request argument(s)
                request = notebooks_v1beta1.ReportInstanceInfoRequest(
                    name="name_value",
                    vm_id="vm_id_value",
                )

                # Make the request
                operation = client.report_instance_info(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.notebooks_v1beta1.types.ReportInstanceInfoRequest, dict]):
                The request object. Request for notebook instances to
                report information to Notebooks API.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.notebooks_v1beta1.types.Instance`
                The definition of a notebook instance.

        """
        # Create or coerce a protobuf request object.
        request = service.ReportInstanceInfoRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.report_instance_info,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            instance.Instance,
            metadata_type=service.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def is_instance_upgradeable(
        self,
        request: Union[service.IsInstanceUpgradeableRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> service.IsInstanceUpgradeableResponse:
        r"""Check if a notebook instance is upgradable.

        .. code-block:: python

            from google.cloud import notebooks_v1beta1

            def sample_is_instance_upgradeable():
                # Create a client
                client = notebooks_v1beta1.NotebookServiceClient()

                # Initialize request argument(s)
                request = notebooks_v1beta1.IsInstanceUpgradeableRequest(
                    notebook_instance="notebook_instance_value",
                )

                # Make the request
                response = client.is_instance_upgradeable(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.notebooks_v1beta1.types.IsInstanceUpgradeableRequest, dict]):
                The request object. Request for checking if a notebook
                instance is upgradeable.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.notebooks_v1beta1.types.IsInstanceUpgradeableResponse:
                Response for checking if a notebook
                instance is upgradeable.

        """
        # Create or coerce a protobuf request object.
        request = service.IsInstanceUpgradeableRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.is_instance_upgradeable,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("notebook_instance", request.notebook_instance),)
            ),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def upgrade_instance(
        self,
        request: Union[service.UpgradeInstanceRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Upgrades a notebook instance to the latest version.

        .. code-block:: python

            from google.cloud import notebooks_v1beta1

            def sample_upgrade_instance():
                # Create a client
                client = notebooks_v1beta1.NotebookServiceClient()

                # Initialize request argument(s)
                request = notebooks_v1beta1.UpgradeInstanceRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.upgrade_instance(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.notebooks_v1beta1.types.UpgradeInstanceRequest, dict]):
                The request object. Request for upgrading a notebook
                instance
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.notebooks_v1beta1.types.Instance`
                The definition of a notebook instance.

        """
        # Create or coerce a protobuf request object.
        request = service.UpgradeInstanceRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.upgrade_instance,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            instance.Instance,
            metadata_type=service.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def upgrade_instance_internal(
        self,
        request: Union[service.UpgradeInstanceInternalRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Allows notebook instances to
        call this endpoint to upgrade themselves. Do not use
        this method directly.


        .. code-block:: python

            from google.cloud import notebooks_v1beta1

            def sample_upgrade_instance_internal():
                # Create a client
                client = notebooks_v1beta1.NotebookServiceClient()

                # Initialize request argument(s)
                request = notebooks_v1beta1.UpgradeInstanceInternalRequest(
                    name="name_value",
                    vm_id="vm_id_value",
                )

                # Make the request
                operation = client.upgrade_instance_internal(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.notebooks_v1beta1.types.UpgradeInstanceInternalRequest, dict]):
                The request object. Request for upgrading a notebook
                instance from within the VM
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.notebooks_v1beta1.types.Instance`
                The definition of a notebook instance.

        """
        # Create or coerce a protobuf request object.
        request = service.UpgradeInstanceInternalRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.upgrade_instance_internal,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            instance.Instance,
            metadata_type=service.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def list_environments(
        self,
        request: Union[service.ListEnvironmentsRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListEnvironmentsAsyncPager:
        r"""Lists environments in a project.

        .. code-block:: python

            from google.cloud import notebooks_v1beta1

            def sample_list_environments():
                # Create a client
                client = notebooks_v1beta1.NotebookServiceClient()

                # Initialize request argument(s)
                request = notebooks_v1beta1.ListEnvironmentsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_environments(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.notebooks_v1beta1.types.ListEnvironmentsRequest, dict]):
                The request object. Request for listing environments.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.notebooks_v1beta1.services.notebook_service.pagers.ListEnvironmentsAsyncPager:
                Response for listing environments.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        request = service.ListEnvironmentsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_environments,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListEnvironmentsAsyncPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_environment(
        self,
        request: Union[service.GetEnvironmentRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> environment.Environment:
        r"""Gets details of a single Environment.

        .. code-block:: python

            from google.cloud import notebooks_v1beta1

            def sample_get_environment():
                # Create a client
                client = notebooks_v1beta1.NotebookServiceClient()

                # Initialize request argument(s)
                request = notebooks_v1beta1.GetEnvironmentRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_environment(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.notebooks_v1beta1.types.GetEnvironmentRequest, dict]):
                The request object. Request for getting a notebook
                environment.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.notebooks_v1beta1.types.Environment:
                Definition of a software environment
                that is used to start a notebook
                instance.

        """
        # Create or coerce a protobuf request object.
        request = service.GetEnvironmentRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_environment,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def create_environment(
        self,
        request: Union[service.CreateEnvironmentRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Creates a new Environment.

        .. code-block:: python

            from google.cloud import notebooks_v1beta1

            def sample_create_environment():
                # Create a client
                client = notebooks_v1beta1.NotebookServiceClient()

                # Initialize request argument(s)
                environment = notebooks_v1beta1.Environment()
                environment.vm_image.image_name = "image_name_value"
                environment.vm_image.project = "project_value"

                request = notebooks_v1beta1.CreateEnvironmentRequest(
                    parent="parent_value",
                    environment_id="environment_id_value",
                    environment=environment,
                )

                # Make the request
                operation = client.create_environment(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.notebooks_v1beta1.types.CreateEnvironmentRequest, dict]):
                The request object. Request for creating a notebook
                environment.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.notebooks_v1beta1.types.Environment` Definition of a software environment that is used to start a notebook
                   instance.

        """
        # Create or coerce a protobuf request object.
        request = service.CreateEnvironmentRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_environment,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            environment.Environment,
            metadata_type=service.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def delete_environment(
        self,
        request: Union[service.DeleteEnvironmentRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Deletes a single Environment.

        .. code-block:: python

            from google.cloud import notebooks_v1beta1

            def sample_delete_environment():
                # Create a client
                client = notebooks_v1beta1.NotebookServiceClient()

                # Initialize request argument(s)
                request = notebooks_v1beta1.DeleteEnvironmentRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_environment(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.notebooks_v1beta1.types.DeleteEnvironmentRequest, dict]):
                The request object. Request for deleting a notebook
                environment.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated
                   empty messages in your APIs. A typical example is to
                   use it as the request or the response type of an API
                   method. For instance:

                      service Foo {
                         rpc Bar(google.protobuf.Empty) returns
                         (google.protobuf.Empty);

                      }

                   The JSON representation for Empty is empty JSON
                   object {}.

        """
        # Create or coerce a protobuf request object.
        request = service.DeleteEnvironmentRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_environment,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=service.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution("google-cloud-notebooks",).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = ("NotebookServiceAsyncClient",)
