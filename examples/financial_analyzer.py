"""
Financial Loan Analyzer: A Demonstration of the Purpose-Aware Meaning Database
"""

import os
import sys

# Add the src directory to the Python path to allow for package imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.meaning_database import MeaningDatabase
from src.context_profiles import FINANCIAL_CONTEXT_PROFILE

def analyze_loan(db: MeaningDatabase, loan_description: str):
    """
    Analyzes a loan application description using the financial context.
    """
    print(f"--- Analyzing Loan: '{loan_description}' ---")

    # Store the loan description in the database using the financial context
    db.store_concept(loan_description, FINANCIAL_CONTEXT_PROFILE)

    # Retrieve the stored concept to get its 4D meaning profile
    concept = db.get_concept(loan_description, FINANCIAL_CONTEXT_PROFILE["name"])

    if not concept:
        print("Error: Could not retrieve concept after storing.")
        return

    # Provide insights based on the 4D coordinates
    love = concept['love']
    justice = concept['justice']
    power = concept['power']
    wisdom = concept['wisdom']

    print(f"  Meaning Profile (L,J,P,W): ({love:.2f}, {justice:.2f}, {power:.2f}, {wisdom:.2f})")

    # Fiduciary Duty & Customer Success (Love)
    if love > 0.4:
        print("  Insight (Love): Strong alignment with customer success and community growth.")
    elif love < 0.2:
        print("  Warning (Love): Low alignment with customer success. May be a predatory loan.")

    # Fairness & Compliance (Justice)
    if justice > 0.4:
        print("  Insight (Justice): Appears to be a fair and compliant application.")
    elif justice < 0.2:
        print("  Warning (Justice): Low indication of fairness or compliance. Review terms carefully.")

    # Financial Viability & Risk (Power)
    if power > 0.4:
        print("  Insight (Power): Strong indicators of financial viability (income, assets).")
    elif power < 0.2:
        print("  Warning (Power): Weak indicators of financial viability. High risk.")

    # Prudence & Data-Driven Insight (Wisdom)
    if wisdom > 0.4:
        print("  Insight (Wisdom): Application is based on a prudent, long-term plan.")
    elif wisdom < 0.2:
        print("  Warning (Wisdom): Lacks a clear, strategic plan. May be an impulsive decision.")

    print("-" * (len(loan_description) + 22))

def main():
    """
    Main function to run the financial loan analyzer demonstration.
    """
    db_path = "financial_demo.db"
    if os.path.exists(db_path):
        os.remove(db_path)

    db = MeaningDatabase(db_path)

    print("\n" + "="*80)
    print("      FINANCIAL LOAN ANALYZER DEMONSTRATION")
    print("  Using a Purpose-Aware Meaning Database to Gain Deeper Insights")
    print("="*80 + "\n")

    # Sample loan application descriptions
    loan1 = "A small business loan for a proven, experienced local entrepreneur to support community growth and build a stable, long-term family asset."
    loan2 = "A high-risk, high-interest personal loan to consolidate credit card debt. Applicant has unstable income but offers a vehicle as collateral."
    loan3 = "A home mortgage for a first-time buyer with a strong credit score and a clear financial plan. This is their dream home."
    loan4 = "A legally questionable, non-compliant loan with unclear terms and a high-pressure sales tactic. All about quick, profitable returns."

    # Analyze each loan
    analyze_loan(db, loan1)
    analyze_loan(db, loan2)
    analyze_loan(db, loan3)
    analyze_loan(db, loan4)

    # Demonstrate a semantic search within the financial context
    print("\n" + "="*80)
    print("      SEMANTIC SEARCH FOR 'FAIR AND RESPONSIBLE LOANS'")
    print("="*80 + "\n")

    search_results = db.search_semantic("fair and responsible loans", FINANCIAL_CONTEXT_PROFILE)

    for result in search_results:
        print(f"  - Found: '{result['concept_text']}' (Similarity: {result['semantic_similarity']:.2f})")
        print(f"    Meaning Profile (L,J,P,W): ({result['love']:.2f}, {result['justice']:.2f}, {result['power']:.2f}, {result['wisdom']:.2f})\n")

    db.close()

if __name__ == "__main__":
    main()
