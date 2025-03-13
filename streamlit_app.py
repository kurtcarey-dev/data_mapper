import streamlit as st
import pandas as pd
from pydantic import BaseModel, Field, ValidationError
from typing import Dict, List, Optional, Any
import json

# App setup
st.set_page_config(page_title="Simple CSV Mapper", page_icon="📊")
st.title("Simple CSV Mapper")

# Initialize session state for persistent data
if 'mappings' not in st.session_state:
    st.session_state.mappings = {}

from pydantic import BaseModel, Field
from typing import Optional, List, Union
from datetime import datetime
from enum import Enum

class Boolean(Enum):
    TRUE = "True"
    FALSE = "False"
    ONE = "1"
    ZERO = "0"

class RateType(Enum):
    PERCENTAGE = "Percentage"
    FIXED = "Fixed"

class Deposit(BaseModel):
    deposit_date: datetime = Field(..., alias="DepositDate")
    amount: float = Field(..., alias="Amount")
    daypart_name: Optional[str] = Field(None, alias="DaypartName")
    employee_number: Optional[str] = Field(None, alias="EmployeeNumber")
    number: Optional[str] = Field(None, alias="Number")
    revenue_center_name: Optional[str] = Field(None, alias="RevenueCenterName")
    closed_time: Optional[datetime] = Field(None, alias="ClosedTime")

class Discount(BaseModel):
    comp_promo_check_number: str = Field(..., alias="CompPromo_CheckNumber")
    comp_comp_name: str = Field(..., alias="Comp_CompName")
    comp_employee_number: Optional[str] = Field(None, alias="Comp_EmployeeNumber")
    comp_revenue_center_name: Optional[str] = Field(None, alias="Comp_RevenueCenterName")
    comp_time: Optional[datetime] = Field(None, alias="Comp_Time")
    comp_amount: float = Field(..., alias="Comp_Amount")
    comp_drawer_number: Optional[str] = Field(None, alias="Comp_DrawerNumber")
    promo_promo_name: str = Field(..., alias="Promo_PromoName")
    promo_employee_number: Optional[str] = Field(None, alias="Promo_EmployeeNumber")
    promo_revenue_center_name: Optional[str] = Field(None, alias="Promo_RevenueCenterName")
    promo_time: Optional[datetime] = Field(None, alias="Promo_Time")
    promo_amount: float = Field(..., alias="Promo_Amount")
    promo_drawer_number: Optional[str] = Field(None, alias="Promo_DrawerNumber")

class Employee(BaseModel):
    employee_id: str = Field(..., alias="EmployeeId")
    first_name: str = Field(..., alias="FirstName")
    middle_name: Optional[str] = Field(None, alias="MiddleName")
    last_name: str = Field(..., alias="LastName")
    payroll_id: Optional[str] = Field(None, alias="PayrollId")
    email: Optional[str] = Field(None, alias="Email")
    phone: Optional[str] = Field(None, alias="Phone")
    address: Optional[str] = Field(None, alias="Address")
    city: Optional[str] = Field(None, alias="City")
    state: Optional[str] = Field(None, alias="State")
    zip: Optional[str] = Field(None, alias="Zip")
    birthdate: Optional[datetime] = Field(None, alias="Birthdate")
    is_inactive: Optional[Union[Boolean, bool]] = Field(None, alias="IsInactive")

class HouseAccount(BaseModel):
    house_account_number: str = Field(..., alias="HouseAccountNumber")
    house_account_name: str = Field(..., alias="HouseAccountName")
    address: Optional[str] = Field(None, alias="Address")
    city: Optional[str] = Field(None, alias="City")
    state: Optional[str] = Field(None, alias="State")
    postal_code: Optional[str] = Field(None, alias="PostalCode")
    first_name: Optional[str] = Field(None, alias="FirstName")
    last_name: Optional[str] = Field(None, alias="LastName")
    phone_number: Optional[str] = Field(None, alias="PhoneNumber")
    email_address: Optional[str] = Field(None, alias="EmailAddress")

class Job(BaseModel):
    job_code: str = Field(..., alias="JobCode")
    job_name: str = Field(..., alias="JobName")
    default_pay_rate: Optional[float] = Field(None, alias="DefaultPayRate")
    job_description: Optional[str] = Field(None, alias="JobDescription")

class LaborDetail(BaseModel):
    employee_number: str = Field(..., alias="EmployeeNumber")
    shift_number: int = Field(..., alias="ShiftNumber")
    clock_in_date: datetime = Field(..., alias="ClockInDate")
    clock_in_time: datetime = Field(..., alias="ClockInTime")
    clock_out_time: datetime = Field(..., alias="ClockOutTime")
    credit_tips: Optional[float] = Field(None, alias="CreditTips")
    declared_tips: Optional[float] = Field(None, alias="DeclaredTips")
    sales: Optional[float] = Field(None, alias="Sales")
    job_code: Optional[str] = Field(None, alias="JobCode")
    job_name: Optional[str] = Field(None, alias="JobName")
    pay_rate: Optional[float] = Field(None, alias="PayRate")
    regular_hours: Optional[float] = Field(None, alias="RegularHours")
    is_unpaid_break: Optional[Union[Boolean, bool]] = Field(None, alias="IsUnpaidBreak")
    is_paid_break: Optional[Union[Boolean, bool]] = Field(None, alias="IsPaidBreak")

class MenuItem(BaseModel):
    item_number: str = Field(..., alias="ItemNumber")
    item_name: str = Field(..., alias="ItemName")
    plu: Optional[str] = Field(None, alias="PLU")
    category_name: Optional[str] = Field(None, alias="CategoryName")
    item_cost: Optional[float] = Field(None, alias="ItemCost")
    sku: Optional[str] = Field(None, alias="SKU")

class NonSalesRevenue(BaseModel):
    non_sales_revenue_check_number: str = Field(..., alias="NonSalesRevenue_CheckNumber")
    non_sales_revenue_amount: float = Field(..., alias="NonSalesRevenue_Amount")
    non_sales_revenue_quantity: Optional[int] = Field(None, alias="NonSalesRevenue_Quantity")
    non_sales_revenue_daypart_name: Optional[str] = Field(None, alias="NonSalesRevenue_DaypartName")
    non_sales_revenue_employee_number: Optional[str] = Field(None, alias="NonSalesRevenue_EmployeeNumber")
    non_sales_revenue_revenue_center_name: Optional[str] = Field(None, alias="NonSalesRevenue_RevenueCenterName")
    non_sales_revenue_time: Optional[datetime] = Field(None, alias="NonSalesRevenue_Time")
    non_sales_revenue_name: str = Field(..., alias="NonSalesRevenue_Name")

class PaidInOut(BaseModel):
    amount: float = Field(..., alias="Amount")
    affects_cash: Optional[Union[Boolean, bool]] = Field(None, alias="AffectsCash")
    daypart_name: Optional[str] = Field(None, alias="DaypartName")
    employee_number: Optional[str] = Field(None, alias="EmployeeNumber")
    paid_in_out_name: str = Field(..., alias="PaidInOutName")
    time: Optional[datetime] = Field(None, alias="Time")
    notes: Optional[str] = Field(None, alias="Notes")

class Payment(BaseModel):
    payment_check_number: str = Field(..., alias="Payment_CheckNumber")
    payment_employee_number: Optional[str] = Field(None, alias="Payment_EmployeeNumber")
    payment_guest_name: Optional[str] = Field(None, alias="Payment_GuestName")
    payment_tender_identity: Optional[str] = Field(None, alias="Payment_TenderIdentity")
    payment_tender_number: str = Field(..., alias="Payment_TenderNumber")
    payment_time: Optional[datetime] = Field(None, alias="Payment_Time")
    payment_tip: Optional[float] = Field(None, alias="Payment_Tip")
    payment_revenue_center_name: Optional[str] = Field(None, alias="Payment_RevenueCenterName")
    payment_base_amount: float = Field(..., alias="Payment_BaseAmount")
    payment_drawer_number: Optional[str] = Field(None, alias="Payment_DrawerNumber")
    payment_auto_gratuity_name: Optional[str] = Field(None, alias="Payment_AutoGratuityName")
    payment_autogratuity_amount: Optional[float] = Field(None, alias="Payment_AutogratuityAmount")

class Refund(BaseModel):
    refund_check_number: str = Field(..., alias="Refund_CheckNumber")
    refund_employee_number: Optional[str] = Field(None, alias="Refund_EmployeeNumber")
    refund_time: Optional[datetime] = Field(None, alias="Refund_Time")
    refund_revenue_center_name: Optional[str] = Field(None, alias="Refund_RevenueCenterName")
    refund_daypart_name: Optional[str] = Field(None, alias="Refund_DaypartName")
    refund_item_number: Optional[str] = Field(None, alias="Refund_ItemNumber")
    refund_manager_employee_number: Optional[str] = Field(None, alias="Refund_ManagerEmployeeNumber")
    refund_order_mode_name: Optional[str] = Field(None, alias="Refund_OrderModeName")
    refund_refund_name: Optional[str] = Field(None, alias="Refund_RefundName")
    refund_tender_number: Optional[str] = Field(None, alias="Refund_TenderNumber")
    refund_drawer_number: Optional[str] = Field(None, alias="Refund_DrawerNumber")
    refund_notes: Optional[str] = Field(None, alias="Refund_Notes")
    refund_tax_amount: Optional[float] = Field(None, alias="Refund_TaxAmount")
    refund_tax_number: Optional[int] = Field(None, alias="Refund_TaxNumber")
    refund_amount: float = Field(..., alias="Refund_Amount")
    refund_quantity: Optional[int] = Field(None, alias="Refund_Quantity")

class ItemSaleModifier(BaseModel):
    item_number: str = Field(..., alias="ItemSale_Modifiers_ItemNumber")
    quantity: int = Field(..., alias="ItemSale_Modifiers_Quantity")
    gross_amount: float = Field(..., alias="ItemSale_Modfiers_GrossAmount")

class ItemSaleComp(BaseModel):
    comp_name: str = Field(..., alias="ItemSale_Comp_CompName")
    employee_number: Optional[str] = Field(None, alias="ItemSale_Comp_EmployeeNumber")
    revenue_center_name: Optional[str] = Field(None, alias="ItemSale_Comp_RevenueCenterName")
    time: Optional[datetime] = Field(None, alias="ItemSale_Comp_Time")
    amount: float = Field(..., alias="ItemSale_Comp_Amount")
    drawer_number: Optional[str] = Field(None, alias="ItemSale_Comp_DrawerNumber")

class ItemSalePromo(BaseModel):
    promo_name: str = Field(..., alias="ItemSale_Promo_PromoName")
    employee_number: Optional[str] = Field(None, alias="ItemSale_Promo_EmployeeNumber")
    revenue_center_name: Optional[str] = Field(None, alias="ItemSale_Promo_RevenueCenterName")
    time: Optional[datetime] = Field(None, alias="ItemSale_Promo_Time")
    amount: float = Field(..., alias="ItemSale_Promo_Amount")
    drawer_number: Optional[str] = Field(None, alias="ItemSale_Promo_DrawerNumber")

class ItemSale(BaseModel):
    employee_number: Optional[str] = Field(None, alias="ItemSale_EmployeeNumber")
    ticket_item_number: int = Field(..., alias="ItemSale_TicketItemNumber")
    item_number: str = Field(..., alias="ItemSale_ItemNumber")
    revenue_center_name: Optional[str] = Field(None, alias="ItemSale_RevenueCenterName")
    time: Optional[datetime] = Field(None, alias="ItemSale_Time")
    quantity: Optional[int] = Field(None, alias="ItemSale_Quantity")
    gross_amount: float = Field(..., alias="ItemSale_GrossAmount")
    modifiers: Optional[List[ItemSaleModifier]] = None
    comp: Optional[ItemSaleComp] = None
    promo: Optional[ItemSalePromo] = None

class SalesDetail(BaseModel):
    check_number: str = Field(..., alias="CheckNumber")
    open_time: Optional[datetime] = Field(None, alias="OpenTime")
    close_time: datetime = Field(..., alias="CloseTime")
    revenue_center_name: Optional[str] = Field(None, alias="RevenueCenterName")
    order_mode_name: Optional[str] = Field(None, alias="OrderModeName")
    employee_number: Optional[str] = Field(None, alias="EmployeeNumber")
    guest_count: Optional[int] = Field(None, alias="GuestCount")
    table_name: Optional[str] = Field(None, alias="TableName")
    item_sales: Optional[List[ItemSale]] = None

class Surcharge(BaseModel):
    surcharge_check_number: str = Field(..., alias="Surcharge_CheckNumber")
    surcharge_amount: float = Field(..., alias="Surcharge_Amount")
    surcharge_daypart_name: Optional[str] = Field(None, alias="Surcharge_DaypartName")
    surcharge_employee_number: Optional[str] = Field(None, alias="Surcharge_EmployeeNumber")
    surcharge_revenue_center_number: Optional[str] = Field(None, alias="Surcharge_RevenueCenterNumber")
    surcharge_time: Optional[datetime] = Field(None, alias="Surcharge_Time")
    surcharge_name: str = Field(..., alias="Surcharge_Name")

class TaxDefinition(BaseModel):
    number: str = Field(..., alias="Number")
    name: str = Field(..., alias="Name")
    rate: Optional[float] = Field(None, alias="Rate")
    rate_type: Optional[RateType] = Field(None, alias="RateType")
    is_inclusive: Optional[Union[Boolean, bool]] = Field(None, alias="IsInclusive")

class TaxDetail(BaseModel):
    check_number: str = Field(..., alias="CheckNumber")
    tax_tax_number: str = Field(..., alias="Tax_TaxNumber")
    tax_revenue_center_name: Optional[str] = Field(None, alias="Tax_RevenueCenterName")
    tax_amount: float = Field(..., alias="Tax_Amount")
    is_inclusive: Optional[Union[Boolean, bool]] = Field(None, alias="IsInclusive")

class Tender(BaseModel):
    number: str = Field(..., alias="Number")
    name: str = Field(..., alias="Name")
    type: Optional[str] = Field(None, alias="Type")

class Till(BaseModel):
    business_date: datetime = Field(..., alias="BusinessDate")
    drawer_number: str = Field(..., alias="DrawerNumber")
    expected_amount: float = Field(..., alias="ExpectedAmount")
    employee_number: Optional[str] = Field(None, alias="EmployeeNumber")
    is_closed: Union[Boolean, bool] = Field(..., alias="IsClosed")
    closed_time: Optional[datetime] = Field(None, alias="ClosedTime")

class Void(BaseModel):
    void_check_number: str = Field(..., alias="Void_CheckNumber")
    void_item_number: Optional[str] = Field(None, alias="Void_ItemNumber")
    void_employee_number: Optional[str] = Field(None, alias="Void_EmployeeNumber")
    void_revenue_center_name: Optional[str] = Field(None, alias="Void_RevenueCenterName")
    void_time: Optional[datetime] = Field(None, alias="Void_Time")
    void_amount: float = Field(..., alias="Void_Amount")
    void_quantity: Optional[int] = Field(None, alias="Void_Quantity")
    void_name: Optional[str] = Field(None, alias="Void_Name")
    void_notes: Optional[str] = Field(None, alias="Void_Notes")
    void_drawer_number: Optional[str] = Field(None, alias="Void_DrawerNumber")

# Register available schemas
SCHEMAS = {
    "deposit": Deposit,
    "discount": Discount,
    "employee": Employee,
    "house_account": HouseAccount,
    "job": Job,
    "labor_detail": LaborDetail,
    "menu_item": MenuItem,
    "non_sales_revenue": NonSalesRevenue,
    "paid_in_out": PaidInOut,
    "payment": Payment,
    "refund": Refund,
    "sales_detail": SalesDetail,
    "surcharge": Surcharge,
    "tax_definition": TaxDefinition,
    "tax_detail": TaxDetail,
    "tender": Tender,
    "till": Till,
    "void": Void
}


# Helper functions
def get_schema_fields(schema_class):
    """Get fields with their properties from a schema class"""
    fields = {}
    
    for name in schema_class.__annotations__:
        # Get field description directly from the Field object
        field_obj = getattr(schema_class, name, None)
        description = getattr(field_obj, "description", f"Field: {name}")
        
        fields[name] = {
            "type": schema_class.__annotations__[name],
            "required": "..." in str(schema_class.__annotations__[name]),
            "description": description
        }
    
    return fields

def detect_schema(columns):
    """Simple schema detection based on column overlap"""
    results = []
    
    for schema_name, schema_class in SCHEMAS.items():
        schema_fields = set(schema_class.__annotations__.keys())
        matching_fields = schema_fields.intersection(set(columns))
        
        if len(schema_fields) > 0:
            score = len(matching_fields) / len(schema_fields)
            results.append({
                "schema": schema_name,
                "score": score,
                "matching": len(matching_fields),
                "total": len(schema_fields)
            })
    
    # Sort by score (highest first)
    results.sort(key=lambda x: x["score"], reverse=True)
    return results

def validate_data(df, schema_name, mapping):
    """Validate sample data against schema"""
    schema_class = SCHEMAS[schema_name]
    errors = []
    
    # Create a renamed dataframe based on mapping
    renamed_df = df.copy()
    reverse_mapping = {csv_col: schema_field for schema_field, csv_col in mapping.items()}
    
    for csv_col, schema_field in reverse_mapping.items():
        if csv_col in renamed_df.columns:
            renamed_df = renamed_df.rename(columns={csv_col: schema_field})
    
    # Check first 5 rows
    for i in range(min(5, len(renamed_df))):
        row = renamed_df.iloc[i].to_dict()
        row_data = {k: v for k, v in row.items() if k in schema_class.__annotations__}
        
        try:
            schema_class(**row_data)
        except ValidationError as e:
            errors.append(f"Row {i+1}: {str(e)}")
            
    return errors

# Main app function
def main():
    # Sidebar with app info
    with st.sidebar:
        st.header("About")
        st.write("""
        Map CSV files to predefined schemas.
        
        1. Upload a CSV file
        2. Select a schema
        3. Map the fields
        4. Export your mapping
        """)
        
        # Show available schemas
        st.header("Available Schemas")
        for name, schema in SCHEMAS.items():
            with st.expander(f"{name.capitalize()} Schema"):
                fields = get_schema_fields(schema)
                for field_name, info in fields.items():
                    st.write(f"**{field_name}**{' (required)' if info['required'] else ''}: {info['description']}")
    
    # File upload
    uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
    
    if not uploaded_file:
        st.info("Please upload a CSV file to begin")
        
        # Show existing mappings if any
        if st.session_state.mappings:
            st.header("Existing Mappings")
            st.json(st.session_state.mappings)
            
            if st.button("Download Mappings as JSON"):
                mapping_json = json.dumps(st.session_state.mappings, indent=2)
                st.download_button(
                    "Download",
                    data=mapping_json,
                    file_name="field_mappings.json",
                    mime="application/json"
                )
                
        return
    
    # Process uploaded file
    try:
        df = pd.read_csv(uploaded_file)
        st.success(f"Successfully loaded CSV with {len(df)} rows and {len(df.columns)} columns")
        
        # Display sample data
        with st.expander("Preview Data"):
            st.dataframe(df.head())
        
        # Schema detection and selection
        schema_options = detect_schema(df.columns)
        
        st.header("Select Schema")
        
        # Display schema options with match scores
        cols = st.columns(min(3, len(schema_options)))
        for i, schema_info in enumerate(schema_options[:3]):  # Show top 3 matches
            with cols[i]:
                score_percent = int(schema_info["score"] * 100)
                st.metric(
                    f"{schema_info['schema'].capitalize()} Schema",
                    f"{score_percent}% match",
                    f"{schema_info['matching']}/{schema_info['total']} fields"
                )
        
        # Schema selection dropdown
        schema_name = st.selectbox(
            "Select schema for this file:",
            options=[s["schema"] for s in schema_options],
            index=0 if schema_options else 0,
            format_func=lambda x: x.capitalize()
        )
        
        if schema_name:
            schema_class = SCHEMAS[schema_name]
            schema_fields = get_schema_fields(schema_class)
            
            st.header("Map Fields")
            st.write(f"Map CSV columns to {schema_name.capitalize()} schema fields:")
            
            # Create mapping interface
            mapping = {}
            csv_columns = ["Not mapped"] + list(df.columns)
            
            # Group fields in rows of 3 for better layout
            field_names = list(schema_fields.keys())
            
            for i in range(0, len(field_names), 3):
                cols = st.columns(3)
                for j in range(3):
                    if i+j < len(field_names):
                        field = field_names[i+j]
                        info = schema_fields[field]
                        
                        with cols[j]:
                            # Set default mapping if column name matches field name
                            default_index = 0
                            if field in df.columns:
                                default_index = csv_columns.index(field)
                            
                            # Field mapping dropdown
                            selected = st.selectbox(
                                f"{field}{' *' if info['required'] else ''}",
                                options=csv_columns,
                                index=default_index,
                                key=f"field_{field}",
                                help=info['description']
                            )
                            
                            if selected != "Not mapped":
                                mapping[field] = selected
            
            # Validation and Save section
            if mapping:
                st.header("Validation")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    if st.button("Validate Mapping"):
                        errors = validate_data(df, schema_name, mapping)
                        
                        if errors:
                            st.error("Validation Issues:")
                            for error in errors:
                                st.write(error)
                        else:
                            st.success("✅ Data validation passed!")
                
                with col2:
                    if st.button("Save Mapping"):
                        st.session_state.mappings[uploaded_file.name] = {
                            "schema": schema_name,
                            "mapping": mapping
                        }
                        st.success(f"Mapping saved for {uploaded_file.name}")
                
                # Export option
                st.header("Export")
                if st.button("Download This Mapping"):
                    single_mapping = {
                        uploaded_file.name: {
                            "schema": schema_name,
                            "mapping": mapping
                        }
                    }
                    mapping_json = json.dumps(single_mapping, indent=2)
                    st.download_button(
                        "Download JSON",
                        data=mapping_json,
                        file_name=f"{uploaded_file.name}_mapping.json",
                        mime="application/json"
                    )
            else:
                st.warning("Please map at least one field")
                
    except Exception as e:
        st.error(f"Error processing file: {str(e)}")

if __name__ == "__main__":
    main()