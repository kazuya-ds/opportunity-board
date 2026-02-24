"""
NASA Open Science Data Management
Standard: SPD-41a compliant
License: Apache 2.0
"""
import pandas as pd

class OpportunityRegistry:
    def __init__(self):
        self.registry = []

    def add_entry(self, field, name, sponsor, deadline, link, stipend, eligibility, info):
        """Standardizes input for industrial career dashboards."""
        self.registry.append({
            "Field": field,
            "Opportunity Name": name,
            "Sponsor": sponsor,
            "Deadline": deadline,
            "Application_Link": link,
            "Stipend": stipend,
            "Eligibility": eligibility,
            "Description": info
        })

    def export(self):
        df = pd.DataFrame(self.registry)
        # Export for open-access transparency
        df.to_csv("opportunities.csv", index=False)
        df.to_excel("opportunities_dashboard.xlsx", index=False, engine='openpyxl')
        return "System: Data exported in CSV and XLSX formats."

# Initialization
db = OpportunityRegistry()
db.add_entry(
    field="Tech & Agriculture",
    name="IoT4Ag Summer Internship",
    sponsor="UC Merced / IoT4Ag Research Center",
    deadline="March 16, 2026",
    link="https://docs.google.com/forms/d/e/1FAIpQLSdj4mJHtILeo9b-ul_5t8roi2idBShMqdCRdTpRMwnGfNZ5-Q/viewform",
    stipend="$8,000",
    eligibility="Undergraduate",
    info="10-week full-time research. Focus on robotics, software, and AI security."
)
print(db.export())