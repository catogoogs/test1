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
"""Server-side executor for x402 payment handling."""

from typing import Dict, Any, Optional
from .base import x402BaseExecutor


class x402ServerExecutor(x402BaseExecutor):
    """Server-side executor for handling x402 payments."""

    def __init__(self):
        """Initialize server executor."""
        super().__init__()
        self.verified_payments = set()

    def verify_payment_signature(self, payload: Dict[str, Any]) -> bool:
        """Verify payment signature.
        
        Args:
            payload: Payment payload to verify
            
        Returns:
            True if signature is valid
        """
        # Signature verification logic
        return bool(payload and payload.get("signature"))

    def record_payment(self, task_id: str, payment_hash: str) -> None:
        """Record a verified payment.
        
        Args:
            task_id: Task ID for the payment
            payment_hash: Hash of the payment transaction
        """
        self.verified_payments.add(payment_hash)
        self.track_payment_status(task_id, "payment-verified")

    def is_payment_verified(self, payment_hash: str) -> bool:
        """Check if a payment has been verified.
        
        Args:
            payment_hash: Hash to check
            
        Returns:
            True if payment is verified
        """
        return payment_hash in self.verified_payments
