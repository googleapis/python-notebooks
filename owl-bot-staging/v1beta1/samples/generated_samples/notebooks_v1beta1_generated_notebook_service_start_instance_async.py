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
# Generated code. DO NOT EDIT!
#
# Snippet for StartInstance
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-notebooks


# [START notebooks_v1beta1_generated_NotebookService_StartInstance_async]
from google.cloud import notebooks_v1beta1


async def sample_start_instance():
    # Create a client
    client = notebooks_v1beta1.NotebookServiceAsyncClient()

    # Initialize request argument(s)
    request = notebooks_v1beta1.StartInstanceRequest(
        name="name_value",
    )

    # Make the request
    operation = client.start_instance(request=request)

    print("Waiting for operation to complete...")

    response = await operation.result()

    # Handle the response
    print(response)

# [END notebooks_v1beta1_generated_NotebookService_StartInstance_async]
