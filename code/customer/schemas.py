from ninja import Schema, ModelSchema, FilterSchema, Field
from datetime import datetime
from typing import Optional, List, Self
from pydantic import model_validator

from customer.models import Customer, Address

class AddressIn(Schema):
    customer_id: int
    address1: str
    address2: Optional[str] = ''
    city: str
    first_name: Optional[str] = ''
    last_name: Optional[str] = ''
    phone: Optional[str] = ''
    province: str
    country: str
    zip: str
    company: str
    name: Optional[str] = ''

class AddressOut(Schema):
    id: int
    customer_id: int
    first_name: str = Field(alias='customer.user.first_name')
    last_name: str = Field(alias='customer.user.last_name')
    company: str
    address1: str
    address2: str
    city: str
    province: str
    zip: str
    phone: Optional[str] = ''
    name: str
    default: bool

class AllAddrResp(Schema):
    customers_address: List[AddressOut]

class AddressResp(Schema):
    customer_address: AddressOut

class CustomerIn(Schema):
    first_name: str
    last_name: str
    email: str
    password: str
    phone: str
    verified_email: bool
    send_email_welcome: bool
    created_at: datetime
    state: str
    currency: str

class CustomerUpdate(Schema):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    password: Optional[str]
    phone: Optional[str]
    verified_email: Optional[bool]
    send_email_welcome: Optional[bool]
    state: Optional[str]
    currency: Optional[str]

class AddressUpdate(Schema):
    address1: Optional[str]
    address2: Optional[str]
    city: Optional[str]
    province: Optional[str]
    country: Optional[str]
    zip: Optional[str]
    phone: Optional[str]
    company: Optional[str]
    default: Optional[bool]
    
class CustomerOut(Schema):
    id: int
    email: str = Field(alias='user.email')
    created_at: datetime
    updated_at: datetime
    first_name: str = Field(alias='user.first_name')
    last_name: str = Field(alias='user.last_name')
    order_counts: int
    state: str
    verified_email: bool
    currency: str
    phone: str
    addresses: Optional[List[AddressOut]] = Field(alias='address_set')

class CustomerResp(Schema):
    customers: List[CustomerOut]

class SingleCustomerResp(Schema):
    customer: CustomerOut