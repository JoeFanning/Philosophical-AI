import os
import urllib.request
import pandas as pd

def download_german_credit_data(dest_folder: str = "src"):
    """
    Programmatically streams the canonical UCI German Credit dataset
    and formats it into a locally accessible CSV.
    """
    # Create the source directory dynamically if it doesn't exist
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
        
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/statlog/german/german.data"
    destination_path = os.path.join(dest_folder, "german_credit_raw.csv")
    
    # Official document headers from the UCI Statlog schema
    column_headers = [
        "checking_status", "duration_months", "credit_history", "purpose", 
        "credit_amount", "savings_status", "employment_since", "installment_commitment", 
        "personal_status_gender", "other_parties", "residence_since", "property_magnitude", 
        "age", "other_payment_plans", "housing", "existing_credits", 
        "job", "num_dependents", "own_telephone", "foreign_worker", "class"
    ]
    
    print(f"⏳ Initiating secure download from UCI Archive...")
    try:
        # Retrieve raw text space-separated matrix file
        temp_file, _ = urllib.request.urlretrieve(url)
        
        # Read into a clean structured Pandas DataFrame
        df = pd.read_csv(temp_file, sep=r'\s+', header=None, names=column_headers)
        
        # Save as a standard structured CSV in your project's code directory
        df.to_csv(destination_path, index=False)
        print(f"✅ Data localized successfully at: {destination_path}")
        print(f"📊 Dataset Dimensions: {df.shape[0]} applicants across {df.shape[1]} metrics.")
        
    except Exception as e:
        print(f"❌ Failed to fetch external dataset repository: {e}")

if __name__ == "__main__":
    download_german_credit_data()
