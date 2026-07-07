import pandas as pd

def main():
    print("Titanic Survival Analysis")

    try:
        df = pd.read_csv("train.csv")

        print(f"\nNumber of passengers: {len(df)}")
        print(f"Number of columns: {len(df.columns)}")

        print("\nFirst five rows:")
        print(df.head())

        print("\nMissing values:")
        print(df.isnull().sum())

        print("\nSurvival rate:")
        print(f"{df['Survived'].mean() * 100:.2f}%")

    except FileNotFoundError:
        print("train.csv was not found.")
        print("Download the Titanic dataset and place train.csv in this folder.")

if __name__ == "__main__":
    main()
