# 🏛️ Government Scheme Web Scraper – MSME Schemes (India)

This project is focused on **web scraping government schemes** listed on the [MSME (Micro, Small, and Medium Enterprises)](https://msme.gov.in/) official website. The goal is to automate the extraction of structured and clean information about various schemes available for MSMEs in India.

## 🚀 Objectives

- Scrape scheme-specific web pages listed under the MSME site.
- Extract relevant sections from each page, including:
  - Scheme Name
  - Description / Objective
  - Nature of Assistance
  - Who Can Apply (Eligibility)
  - How to Apply
  - Whom to Contact
- Save the extracted data in a analyzable format (Excel/CSV).
- Eliminate redundant or repeated data to ensure each scheme entry is unique and accurate.

---

## 🧰 Technologies Used

- **Python**
- **BeautifulSoup (bs4)** – HTML parsing
- **Requests** – For HTTP requests
- **Pandas** – Data storage and export
- **openpyxl** – Excel file support

---

## 📋 Tasks Performed

### ✅ Web Scraping Pipeline

1. **Collected URLs** of individual MSME schemes manually (currently scraping 9 major scheme pages).
2. **Sent GET requests** using `requests` with appropriate headers.
3. **Parsed HTML content** using `BeautifulSoup` and filtered out unnecessary tags like `<script>`, `<style>`, `<nav>`, and `<footer>`.
4. **Identified relevant keywords** for classification of content into categories:
   - `"Scheme Name"`
   - `"Description"`
   - `"Nature of Assistance"`
   - `"Who Can Apply"`
   - `"How to Apply"`
   - `"Whom to Contact"`
5. Used **string matching and block capture logic** to extract a few lines around each keyword to maintain context.
6. Implemented **fallback logic** using `<h1>`, `<h2>`, or `<title>` for scheme name detection in case it's not explicitly labeled.
7. Handled exceptions gracefully for broken links or non-standard pages.
8. **Exported final structured data** to `Excel (.xlsx)` using `pandas`.

### 🧽 Data Cleaning

- Removed duplicate entries and redundant paragraphs.
- Cleaned up repeated sentences across multiple schemes, especially in the *"Nature of Assistance"* and *"Whom to Contact"* fields.
- Ensured consistent formatting for output and readability.

---

## 📦 Output

- The final structured data is saved to:
  - `Schemes_Info_<timestamp>.xlsx`
- Each row represents a **unique MSME scheme**, and each column captures a specific type of information.

