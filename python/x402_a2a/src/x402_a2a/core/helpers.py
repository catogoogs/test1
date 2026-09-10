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
"""Helper functions for payment requirements."""

from typing import Optional, Union, List
from x402.types import Price, PaymentRequirements
from .merchant import create_payment_requirements


def require_payment(
    price: Price,
    pay_to_address: str,
    resource: str,
    network: str = "base",
    description: str = "Payment required",
) -> PaymentRequirements:
    """Create payment requirements for a service."""
    return create_payment_requirements(
        price=price,
        pay_to_address=pay_to_address,
        resource=resource,
        network=network,
        description=description,
    )


def require_payment_choice(
    options: List[PaymentRequirements],
) -> List[PaymentRequirements]:
    """Create multiple payment options."""
    return options


def paid_service(
    price: Price,
    pay_to_address: str,
    resource: str,
) -> PaymentRequirements:
    """Mark a service as requiring payment."""
    return require_payment(
        price=price,
        pay_to_address=pay_to_address,
        resource=resource,
    )


def smart_paid_service(
    base_price: Price,
    pay_to_address: str,
    resource: str,
    multiplier: float = 1.0,
) -> PaymentRequirements:
    """Create smart pricing for a service."""
    return paid_service(
        price=base_price,
        pay_to_address=pay_to_address,
        resource=resource,
    )


def create_tiered_payment_options(
    base_price: Price,
    pay_to_address: str,
    tiers: List[tuple[str, float]],
) -> List[PaymentRequirements]:
    """Create tiered payment options.
    
    Args:
        base_price: Base price for tier 1
        pay_to_address: Address to receive payments
        tiers: List of (name, multiplier) tuples
        
    Returns:
        List of payment requirements for each tier
    """
    options = []
    for tier_name, multiplier in tiers:
        # Create tiered payment options
        options.append(
            PaymentRequirements(
                scheme="exact",
                network="base",
                asset="0x833589fCD6eDb6E08f4c7C32D4f71b54bda02913",
                pay_to=pay_to_address,
                max_amount_required="1000000",
                resource=f"/service/{tier_name}",
                description=f"Payment for {tier_name} tier",
            )
        )
    return options


def check_payment_context(context: dict) -> bool:
    """Check if payment context is valid."""
    return bool(context and context.get("payment_required"))
