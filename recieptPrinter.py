from escpos.printer import Usb

# Change these to match your printer's Vendor ID and Product ID
VENDOR_ID = 0x0416  # example
PRODUCT_ID = 0x5011  # example

# Connect to the printer
p = Usb(0x0416, 0x5011, interface=0, out_ep=0x03)

def calendar_to_reciept(name: str, description: str, due: str):
    if p:
        # Print Header
        p.set(align="center", bold=True, width=2, height=2)
        p.text("==============================\n")
        p.text(name.upper() + "\n")
        p.text("==============================\n\n")

        # Time Required
        p.set(align="center", bold=True, width=2, height=2)
        p.text(f"{due}\n\n")

        # Description Section
        p.set(align="left", bold=True, width=1, height=1)
        p.text("Description:\n")
        p.set(align="left", bold=False, width=1, height=1)
        p.text(description + "\n\n")

        # Footer
        p.set(align="center", bold=True, width=1, height=1)
        p.text("------------------------------\n")
        p.text("Generated via Google Calendar Event\n")
    else:
        print("ERROR: PRINTER NOT FOUND!")
