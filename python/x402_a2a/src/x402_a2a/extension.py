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
"""Extension declaration and activation utilities."""

from typing import Dict, Any, Optional


def get_extension_declaration() -> Dict[str, Any]:
    """Get the x402 extension declaration for agent cards."""
    return {
        "uri": "https://github.com/google-a2a/a2a-x402/v0.1",
        "description": "Supports x402 payments using on-chain cryptocurrency",
        "required": True,
    }


def check_extension_activation(headers: Dict[str, str]) -> bool:
    """Check if x402 extension is activated in request headers.
    
    Args:
        headers: HTTP headers from request
        
    Returns:
        True if x402 extension is activated
    """
    extensions = headers.get("X-A2A-Extensions", "")
    return "a2a-x402" in extensions or "x402" in extensions


def add_extension_activation_header(headers: Dict[str, str]) -> Dict[str, str]:
    """Add x402 extension activation to response headers.
    
    Args:
        headers: Existing headers
        
    Returns:
        Headers with x402 extension activated
    """
    headers["X-A2A-Extensions"] = "https://github.com/google-a2a/a2a-x402/v0.1"
    return headers
