"""
NASA Open Science Data Management - Internship Registry
Standard: SPD-41a compliant | Version: 2026.2.1
"""
import pandas as pd
from datetime import datetime

class OpportunityRegistry:
    def __init__(self):
        self.registry = []

    def add_entry(self, field, name, sponsor, deadline, stipend, eligibility, info, app_link):
        """
        Appends a standardized entry to the registry.
        Note: app_link is placed as the final metadata field for CSV consistency.
        """
        self.registry.append({
            "Field": field,
            "Opportunity Name": name,
            "Sponsor": sponsor,
            "Deadline": deadline,
            "Stipend": stipend,
            "Eligibility": eligibility,
            "Description": info,
            "Application Link": app_link  # Final column added here
        })

    def export(self):
        """Exports the registry with a standard naming convention for GitHub Actions."""
        if not self.registry:
            return "Error: Registry is empty. No data exported."

        df = pd.DataFrame(self.registry)
        
        # Adding a 'System Last Updated' metadata column for professional audit trails
        df['Last_Updated_UTC'] = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

        # Exporting to CSV (Core for GitHub Pages & Discord Bot)
        df.to_csv("opportunities.csv", index=False, encoding='utf-8')
        
        # Exporting to Excel (Professional Administrative Use)
        df.to_excel("opportunities_dashboard.xlsx", index=False, engine='openpyxl')
        
        return f"Success: {len(df)} entries exported to 'opportunities.csv' and 'opportunities_dashboard.xlsx'."

# --- Professional Entry Example ---
db = OpportunityRegistry()

db.add_entry(
    field="Tech & Agriculture",
    name="IoT4Ag Summer Internship",
    sponsor="UC Merced / IoT4Ag Research Center",
    deadline="5 PM, March 16, 2026",
    stipend="$8,000",
    eligibility="Undergraduate",
    info="10-week full-time research focused on robotics, precision agriculture, and cyber-physical systems.",
    app_link="https://docs.google.com/forms/d/e/1FAIpQLSdj4mJHtILeo9b-ul_5t8roi2idBShMqdCRdTpRMwnGfNZ5-Q/viewform"
)

print(db.export())