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
from .environment import (
    ContainerImage,
    Environment,
    VmImage,
)
from .event import (
    Event,
)
from .execution import (
    Execution,
    ExecutionTemplate,
)
from .instance import (
    Instance,
    ReservationAffinity,
)
from .instance_config import (
    InstanceConfig,
)
from .managed_service import (
    CreateRuntimeRequest,
    DeleteRuntimeRequest,
    GetRuntimeRequest,
    ListRuntimesRequest,
    ListRuntimesResponse,
    ReportRuntimeEventRequest,
    ResetRuntimeRequest,
    StartRuntimeRequest,
    StopRuntimeRequest,
    SwitchRuntimeRequest,
)
from .runtime import (
    EncryptionConfig,
    LocalDisk,
    LocalDiskInitializeParams,
    Runtime,
    RuntimeAcceleratorConfig,
    RuntimeAccessConfig,
    RuntimeMetrics,
    RuntimeShieldedInstanceConfig,
    RuntimeSoftwareConfig,
    VirtualMachine,
    VirtualMachineConfig,
)
from .schedule import (
    Schedule,
)
from .service import (
    CreateEnvironmentRequest,
    CreateExecutionRequest,
    CreateInstanceRequest,
    CreateScheduleRequest,
    DeleteEnvironmentRequest,
    DeleteExecutionRequest,
    DeleteInstanceRequest,
    DeleteScheduleRequest,
    GetEnvironmentRequest,
    GetExecutionRequest,
    GetInstanceHealthRequest,
    GetInstanceHealthResponse,
    GetInstanceRequest,
    GetScheduleRequest,
    IsInstanceUpgradeableRequest,
    IsInstanceUpgradeableResponse,
    ListEnvironmentsRequest,
    ListEnvironmentsResponse,
    ListExecutionsRequest,
    ListExecutionsResponse,
    ListInstancesRequest,
    ListInstancesResponse,
    ListSchedulesRequest,
    ListSchedulesResponse,
    OperationMetadata,
    RegisterInstanceRequest,
    ReportInstanceInfoRequest,
    ResetInstanceRequest,
    RollbackInstanceRequest,
    SetInstanceAcceleratorRequest,
    SetInstanceLabelsRequest,
    SetInstanceMachineTypeRequest,
    StartInstanceRequest,
    StopInstanceRequest,
    TriggerScheduleRequest,
    UpdateInstanceConfigRequest,
    UpdateShieldedInstanceConfigRequest,
    UpgradeInstanceInternalRequest,
    UpgradeInstanceRequest,
)

__all__ = (
    'ContainerImage',
    'Environment',
    'VmImage',
    'Event',
    'Execution',
    'ExecutionTemplate',
    'Instance',
    'ReservationAffinity',
    'InstanceConfig',
    'CreateRuntimeRequest',
    'DeleteRuntimeRequest',
    'GetRuntimeRequest',
    'ListRuntimesRequest',
    'ListRuntimesResponse',
    'ReportRuntimeEventRequest',
    'ResetRuntimeRequest',
    'StartRuntimeRequest',
    'StopRuntimeRequest',
    'SwitchRuntimeRequest',
    'EncryptionConfig',
    'LocalDisk',
    'LocalDiskInitializeParams',
    'Runtime',
    'RuntimeAcceleratorConfig',
    'RuntimeAccessConfig',
    'RuntimeMetrics',
    'RuntimeShieldedInstanceConfig',
    'RuntimeSoftwareConfig',
    'VirtualMachine',
    'VirtualMachineConfig',
    'Schedule',
    'CreateEnvironmentRequest',
    'CreateExecutionRequest',
    'CreateInstanceRequest',
    'CreateScheduleRequest',
    'DeleteEnvironmentRequest',
    'DeleteExecutionRequest',
    'DeleteInstanceRequest',
    'DeleteScheduleRequest',
    'GetEnvironmentRequest',
    'GetExecutionRequest',
    'GetInstanceHealthRequest',
    'GetInstanceHealthResponse',
    'GetInstanceRequest',
    'GetScheduleRequest',
    'IsInstanceUpgradeableRequest',
    'IsInstanceUpgradeableResponse',
    'ListEnvironmentsRequest',
    'ListEnvironmentsResponse',
    'ListExecutionsRequest',
    'ListExecutionsResponse',
    'ListInstancesRequest',
    'ListInstancesResponse',
    'ListSchedulesRequest',
    'ListSchedulesResponse',
    'OperationMetadata',
    'RegisterInstanceRequest',
    'ReportInstanceInfoRequest',
    'ResetInstanceRequest',
    'RollbackInstanceRequest',
    'SetInstanceAcceleratorRequest',
    'SetInstanceLabelsRequest',
    'SetInstanceMachineTypeRequest',
    'StartInstanceRequest',
    'StopInstanceRequest',
    'TriggerScheduleRequest',
    'UpdateInstanceConfigRequest',
    'UpdateShieldedInstanceConfigRequest',
    'UpgradeInstanceInternalRequest',
    'UpgradeInstanceRequest',
)
