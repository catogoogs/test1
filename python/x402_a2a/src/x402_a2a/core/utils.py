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
"""Utility functions for state management."""

from typing import Optional, Dict, Any


class x402Utils:
    """Utility class for x402 state management."""

    @staticmethod
    def create_payment_submission_message(
        task_id: str, payment_payload: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Create a payment submission message.
        
        Args:
            task_id: Task ID to link payment to
            payment_payload: Signed payment payload
            
        Returns:
            Message structure for submission
        """
        return {
            "taskId": task_id,
            "metadata": {
                "x402.payment.status": "payment-submitted",
                "x402.payment.payload": payment_payload,
            },
        }

    @staticmethod
    def extract_task_id(message: Dict[str, Any]) -> Optional[str]:
        """Extract task ID from a message.
        
        Args:
            message: Message to extract from
            
        Returns:
            Task ID if present, None otherwise
        """
        return message.get("taskId")


def create_payment_submission_message(
    task_id: str, payment_payload: Dict[str, Any]
) -> Dict[str, Any]:
    """Create a payment submission message."""
    return x402Utils.create_payment_submission_message(task_id, payment_payload)


def extract_task_id(message: Dict[str, Any]) -> Optional[str]:
    """Extract task ID from a message."""
    return x402Utils.extract_task_id(message)
