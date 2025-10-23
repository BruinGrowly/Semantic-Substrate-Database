"""
Financial Loan Analyzer: Demonstration of the Definitive Semantic Database
"""

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.meaning_database import MeaningDatabase

def analyze_loan_with_auto_context(db: MeaningDatabase, loan_description: str):
    """
    Analyzes a loan application using the new automatic context detection.
    """
    print(f"--- Analyzing Loan with Auto-Context: '{loan_description}' ---")

    # The new API is even simpler. We just analyze with auto-context.
    concept = db.analyze_with_auto_context(loan_description)

    love = concept['love']
    justice = concept['justice']
    power = concept['power']
    wisdom = concept['wisdom']

    print(f"  Meaning Profile (L,J,P,W): ({love:.2f}, {justice:.2f}, {power:.2f}, {wisdom:.2f})")

    insight_score = (love + justice + wisdom) - power

    if insight_score > 0.5:
        print(f"  Insight: High potential for a successful, fair, and prudent loan (Score: {insight_score:.2f}).")
    elif power > 0.6 and justice < 0.4:
         print(f"  Warning: High-risk, potentially predatory loan flagged (Score: {insight_score:.2f}).")
    elif love < 0.4 or justice < 0.4:
        print(f"  Warning: Significant concerns in customer success or fairness flagged (Score: {insight_score:.2f}).")
    else:
        print(f"  Insight: A balanced loan application requiring standard review (Score: {insight_score:.2f}).")

    print("-" * (len(loan_description) + 32))

def main():
    db_path = "financial_demo_v5.db"
    if os.path.exists(db_path):
        os.remove(db_path)

    db = MeaningDatabase(db_path)

    print("\n" + "="*80)
    print("      DEFINITIVE FINANCIAL LOAN ANALYZER (v5.0)")
    print("  Demonstrating Automatic Context Detection")
    print("="*80 + "\n")

    loan_text = "A small business loan for a local entrepreneur with a strong credit score and a clear financial plan to support community growth."
    biblical_text = "The sermon was about divine love, grace, and the righteousness of God's law."

    # Analyze both texts with the new auto-context feature
    analyze_loan_with_auto_context(db, loan_text)
    analyze_loan_with_auto_context(db, biblical_text)

    db.close()

if __name__ == "__main__":
    main()
