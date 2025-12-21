import pandas as pd
import os


def main():
    # Path input & output (sesuai struktur lokal)
    input_path = "telco_customer_churn_raw/telco_customer_churn.csv"
    output_path = "preprocessing/telco_preprocessing.csv"

    # Load dataset
    df = pd.read_csv(input_path)

    # Drop kolom tidak relevan
    df = df.drop(columns=["customerID"])

    # Konversi TotalCharges ke numerik
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

    # Hapus missing value
    df = df.dropna()

    # Encoding target
    df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

    # One-hot encoding fitur kategorikal
    df = pd.get_dummies(df, drop_first=True)

    # Simpan dataset hasil preprocessing
    df.to_csv(output_path, index=False)

    print("Preprocessing selesai. File disimpan di:", output_path)


if __name__ == "__main__":
    main()