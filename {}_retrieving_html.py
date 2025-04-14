from bs4 import BeautifulSoup
import pandas as pd
import requests
from datetime import datetime

# List of scheme URLs
urls = [
    "https://msme.gov.in/1-prime-ministers-employment-generation-programme-pmegp",
    "https://msme.gov.in/development-khadi-village-and-coir-industries",
    "https://msme.gov.in/1-marketing-promotion-schemes#A22",
    "https://msme.gov.in/technology-upgradation-and-quality-certification",
    "https://msme.gov.in/entrepreneurship-and-skill-development-programs",
    "https://msme.gov.in/infrastructure-development-program",
    "https://msme.gov.in/establishment-new-technology-centres-extension-centres-under-hub-spoke-model",
    "https://msme.gov.in/scheme-surveys-studies-and-policy-research",
    "https://msme.gov.in/promotion-msmes-ner-and-sikkim"
]

# HTTP headers
HEADERS = {
    'User-Agent': 'Mozilla/5.0',
    'Accept-Language': 'en-US,en;q=0.5'
}

# Keywords to extract sections
keywords = {
    'Scheme Name': ['scheme name'],
    'Description': ['about the scheme', 'description', 'introduction', 'objective'],
    'Nature of Assistance': ['assistance', 'subsidy', 'support', 'benefit'],
    'Who Can Apply': ['eligibility', 'who can apply', 'beneficiaries'],
    'How to Apply': ['how to apply', 'application procedure', 'process'],
    'Whom to Contact': ['contact', 'helpline', 'officer', 'email', 'address']
}

all_data = []

# Process each URL
for url in urls:
    try:
        response = requests.get(url, headers=HEADERS, timeout=15)
        soup = BeautifulSoup(response.content, "html.parser")

        # Remove unwanted tags
        for tag in soup(['script', 'style', 'footer', 'nav']):
            tag.decompose()

        lines = list(dict.fromkeys(soup.get_text(separator='\n', strip=True).split('\n')))
        extracted_data = {key: [] for key in keywords}

        for i, line in enumerate(lines):
            lower_line = line.lower()
            for category, kw_list in keywords.items():
                if any(kw in lower_line for kw in kw_list):
                    block = "\n".join(lines[i:i+3])  # Small block around keyword
                    if block not in extracted_data[category] and len(block) < 800:
                        extracted_data[category].append(block)

        # Combine extracted info
        for key in extracted_data:
            extracted_data[key] = "\n\n".join(extracted_data[key]) if extracted_data[key] else ""

        # Scheme Name from header or fallback
        heading = soup.find(['h1', 'h2', 'h3'])
        if heading:
            extracted_data['Scheme Name'] = heading.get_text(strip=True)
        elif soup.title:
            extracted_data['Scheme Name'] = soup.title.get_text(strip=True)
        else:
            extracted_data['Scheme Name'] = f"Unknown (From: {url})"

        print(f"Extracted: {extracted_data['Scheme Name']}")
        all_data.append(extracted_data)

    except Exception as e:
        print(f"Failed to process {url}: {e}")

# Save to Excel with timestamp
df = pd.DataFrame(all_data)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
file_name = f"Schemes_Info_{timestamp}.xlsx"
df.to_excel(file_name, index=False)
print(f"All data saved to '{file_name}'")
