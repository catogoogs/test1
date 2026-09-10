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
"""Base executor for x402 payment handling."""

from typing import Dict, Any, Optional


class x402BaseExecutor:
    """Base executor class for x402 payment middleware."""

    def __init__(self):
        """Initialize the base executor."""
        self.payment_status = {}

    def extract_payment_requirements(self, response: Dict[str, Any]) -> Optional[Dict]:
        """Extract payment requirements from a response.
        
        Args:
            response: Response containing payment requirements
            
        Returns:
            Payment requirements if present
        """
        metadata = response.get("status", {}).get("message", {}).get("metadata", {})
        return metadata.get("x402.payment.required")

    def track_payment_status(self, task_id: str, status: str) -> None:
        """Track payment status for a task.
        
        Args:
            task_id: Task ID to track
            status: Payment status value
        """
        self.payment_status[task_id] = status

    def get_payment_status(self, task_id: str) -> Optional[str]:
        """Get payment status for a task.
        
        Args:
            task_id: Task ID to query
            
        Returns:
            Payment status if tracked
        """
        return self.payment_status.get(task_id)
