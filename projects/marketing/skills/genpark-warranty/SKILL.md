# GenPark Warranty-Enforcer Skill (Automated Warranty Execution)

Manages and executes automated product warranties by scanning purchase emails for terms and conditions, then automatically initiating claims for defect reports.

## Commands

### `genpark-warranty audit <product_name>`
Scans the user's historical purchase database and identifies all items still under warranty, flagging those with known manufacture defects.

### `genpark-warranty claim <product_name> --issue <description>`
Automatically generates a formal warranty claim letter, attaches the purchase receipt from the user's GenPark database, and sends it to the manufacturer's RMA department.

## Guidelines
- Priority: Protecting the user's long-term hardware value.
- Target: Manufacturers with complex RMA (Return Merchandise Authorization) systems.
- Tone: Formal, detailed, and persistent.
