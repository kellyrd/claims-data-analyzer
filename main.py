import pandas as pd

def load_claims(file_path):
    try:
        df = pd.read_csv(file_path)
        print("Claims file loaded successfully.")
        return df
    except Exception as e:
        print(f"Error loading file: {e}")
        return None

def analyze_claims(df):
    if df is None:
        print("No data to analyze.")
        return

    print("\n--- Summary Report ---")
    print(f"Total claims: {len(df)}")

    missing_values = df.isnull().sum()
    print("\nMissing values per column:")
    print(missing_values)

def main():
    file_path = "sample_claims.csv"
    df = load_claims(file_path)
    analyze_claims(df)

if __name__ == "__main__":
    main()
