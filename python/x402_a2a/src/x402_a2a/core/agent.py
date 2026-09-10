# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Agent card creation utilities."""

from typing import Dict, Any, Optional


def create_x402_agent_card(
    agent_name: str,
    description: str,
    version: str = "0.1",
    pay_to_address: Optional[str] = None,
) -> Dict[str, Any]:
    """Create an A2A agent card with x402 extension support.
    
    Args:
        agent_name: Name of the agent
        description: Agent description
        version: API version
        pay_to_address: Address for receiving payments
        
    Returns:
        Agent card structure with x402 extension
    """
    return {
        "name": agent_name,
        "description": description,
        "version": version,
        "capabilities": {
            "extensions": [
                {
                    "uri": "https://github.com/google-a2a/a2a-x402/v0.1",
                    "description": "Supports x402 payments for on-chain settlement",
                    "required": True,
                }
            ]
        },
        "monetization": {
            "pay_to_address": pay_to_address,
        } if pay_to_address else {},
    }
