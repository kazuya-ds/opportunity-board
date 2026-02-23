import pandas as pd

class InternshipOpportunity:
    """Represents a standardized internship record."""
    def __init__(self, field, name, sponsor, deadline, app_link, information):
        self.field = field
        self.name = name
        self.sponsor = sponsor
        self.deadline = deadline
        self.app_link = app_link
        self.information = information

    def to_dict(self):
        """Returns dictionary for DataFrame conversion."""
        return {
            "Field": self.field,
            "Opportunity Name": self.name,
            "Sponsor": self.sponsor,
            "Deadline": self.deadline,
            "Application Link": self.app_link,
            "Details": self.information
        }

def main():
    # Dataset instantiation
    opportunities = [
        InternshipOpportunity(
            field="Tech & Agriculture",
            name="IoT4Ag Summer Internship",
            sponsor="UC Merced / IoT4Ag",
            deadline="2026-03-16",
            app_link="https://docs.google.com/forms/d/e/1FAIpQLSdj4mJHtILeo9b-ul_5t8roi2idBShMqdCRdTpRMwnGfNZ5-Q/viewform?usp=header",
            information="Interested in applying your tech skills to solve problems in agriculture? Applications for summer internships at UC Merced are now open, funded by the Internet of Things for Precision Agriculture Engineering Research Center (IoT4Ag). These internships will be in-person, and full-time for 10-weeks (Monday, June 1- Friday, July 31). Interns will receive an $8,000 stipend and will participate in the UC Merced Summer Undergraduate Research Institute (SURI) in addition to conducting research in a lab. Selected interns may also be eligible for covered housing on campus. 


We are seeking undergraduate students from any college or university across all levels and disciplines to join our ongoing projects. We are particularly looking for students with expertise or interest in: - physical systems: mechanical design, hardware, and robot/drone operation; - digital infrastructure: software development (front end, back end, mobile apps, data analytics); - spatial intelligence: GIS and mapping; - system integrity: cybersecurity and AI security testing. While specific skills are a plus, no prior experience is needed."
        )
    ]

    # Process and Export
    df = pd.DataFrame([o.to_dict() for o in opportunities])
    
    # Export as CSV (NASA recommendation for long-term accessibility)
    df.to_csv("opportunities.csv", index=False)
    
    # Export as Excel for administrative use
    df.to_excel("opportunities_dashboard_data.xlsx", index=False, engine='openpyxl')
    
    print("Files 'opportunities.csv' and 'opportunities_dashboard_data.xlsx' generated.")

if __name__ == "__main__":
    main()
