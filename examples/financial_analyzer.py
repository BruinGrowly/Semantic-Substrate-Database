"""
Financial Loan Analyzer: A Demonstration of the Definitive, Purpose-Aware Meaning Database
"""

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.meaning_database import MeaningDatabase
from src.context_profiles import FINANCIAL_CONTEXT_PROFILE

def analyze_loan(db: MeaningDatabase, loan_description: str):
    """
    Analyzes a loan application using the definitive financial context model.
    """
    print(f"--- Analyzing Loan: '{loan_description}' ---")

    db.store_concept(loan_description, FINANCIAL_CONTEXT_PROFILE)
    concept = db.get_concept(loan_description, FINANCIAL_CONTEXT_PROFILE["name"])

    if not concept:
        print("Error: Could not retrieve concept.")
        return

    love = concept['love']
    justice = concept['justice']
    power = concept['power']
    wisdom = concept['wisdom']

    print(f"  Meaning Profile (L,J,P,W): ({love:.2f}, {justice:.2f}, {power:.2f}, {wisdom:.2f})")

    # Definitive insights based on the new model
    insight_score = (love + justice + wisdom) - power

    if insight_score > 0.5:
        print(f"  Insight: High potential for a successful, fair, and prudent loan (Score: {insight_score:.2f}).")
    elif power > 0.6 and justice < 0.4:
         print(f"  Warning: High-risk, potentially predatory loan flagged (Score: {insight_score:.2f}).")
    elif love < 0.4 or justice < 0.4:
        print(f"  Warning: Significant concerns in customer success or fairness flagged (Score: {insight_score:.2f}).")
    else:
        print(f"  Insight: A balanced loan application requiring standard review (Score: {insight_score:.2f}).")

    print("-" * (len(loan_description) + 22))

def main():
    db_path = "financial_demo.db"
    if os.path.exists(db_path):
        os.remove(db_path)

    db = MeaningDatabase(db_path)

    print("\n" + "="*80)
    print("      DEFINITIVE FINANCIAL LOAN ANALYZER DEMONSTRATION")
    print("="*80 + "\n")

    # Sample loan application descriptions
    loan1 = "A small business loan for a proven, experienced local entrepreneur to support community growth and build a stable, long-term family asset."
    loan2 = "A high-risk, high-interest personal loan to consolidate credit card debt. Applicant has unstable income."
    loan3 = "A home mortgage for a first-time buyer with a strong credit score and a clear financial plan. This is their dream home."
    loan4 = "A legally questionable, non-compliant loan with unclear terms and a high-pressure sales tactic."

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
