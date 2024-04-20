# Define lead distribution rules
def distribute_leads(leads, recipients):
    distributed_leads = {}
    for lead in leads:
        for recipient in recipients:
            if lead['location'] == recipient['location']:
                if recipient['location'] not in distributed_leads:
                    distributed_leads[recipient['location']] = []
                distributed_leads[recipient['location']].append(lead['name'])
    return distributed_leads



def main():
    # Define leads
    leads = [
        {"name": "John Doe", "email": "john@example.com", "location": "New York", "lead_type": "Loan"},
        {"name": "Jane Smith", "email": "jane@example.com", "location": "Los Angeles", "lead_type": "Insurance"},
        {"name": "Bob Johnson", "email": "bob@example.com", "location": "Chicago", "lead_type": "Loan"}
    ]
    #lead.update({replace this feild with the name of key} = {replace this field with the values})

    # Define recipients
    recipients = [
        {"name": "Lender 1", "location": "New York"},
        {"name": "Lender 2", "location": "Los Angeles"},
        {"name": "Lender 3", "location": "Chicago"}
    ]

    # Distribute leads based on rules
    distributed_leads = distribute_leads(leads, recipients)

    # Print out distributed leads
    for location, lead_list in distributed_leads.items():
        print(f"Leads in {location}:")
        for lead_name in lead_list:
            print(f"- {lead_name}")


if __name__ == "__main__":
    main()