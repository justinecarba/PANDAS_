import os

import pandas as pd


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SALES_FILE = os.path.join(BASE_DIR, "sales.csv")
REQUIRED_COLUMNS = {"OrderID", "Product", "Category", "Price", "Quantity"}


def load_sales_data(file_path: str = SALES_FILE) -> pd.DataFrame:
    """Load sales records, validate required fields, and calculate revenue."""
    sales = pd.read_csv(file_path)
    missing_columns = REQUIRED_COLUMNS.difference(sales.columns)
    if missing_columns:
        missing = ", ".join(sorted(missing_columns))
        raise ValueError(f"The sales CSV is missing required columns: {missing}")
    if sales.empty:
        raise ValueError("The sales CSV contains no records.")

    required_data = ["OrderID", "Product", "Category", "Price", "Quantity"]
    if sales[required_data].isna().any().any():
        raise ValueError("The sales CSV has blank values in required fields.")

    sales["Price"] = pd.to_numeric(sales["Price"], errors="raise")
    sales["Quantity"] = pd.to_numeric(sales["Quantity"], errors="raise")
    sales["Revenue"] = sales["Price"] * sales["Quantity"]
    return sales


def display_sales(data: pd.DataFrame) -> None:
    print("\n" + "*" * 57)
    print("                    YOUR SALES")
    print("*" * 57)
    print(data.to_string(index=False))
    print("*" * 57)


def calculate_revenue(data: pd.DataFrame) -> None:
    data["Revenue"] = data["Price"] * data["Quantity"]
    print("Revenue calculations completed.")
    display_sales(data)


def total_revenue(data: pd.DataFrame) -> None:
    print(f"Total Revenue: PHP {data['Revenue'].sum():,.2f}")


def best_selling_product(data: pd.DataFrame) -> None:
    product_sales = data.groupby("Product")["Quantity"].sum()
    best_product = product_sales.idxmax()
    quantity_sold = product_sales.max()
    print(f"Best-Selling Product: {best_product}")
    print(f"Quantity Sold: {quantity_sold:,.2f}")


def most_revenue(data: pd.DataFrame) -> None:
    category_revenue = data.groupby("Category")["Revenue"].sum()
    best_category = category_revenue.idxmax()
    revenue = category_revenue.max()
    print(f"Top Revenue Category: {best_category}")
    print(f"Revenue: PHP {revenue:,.2f}")


def average_order(data: pd.DataFrame) -> None:
    order_revenue = data.groupby("OrderID")["Revenue"].sum()
    print(f"Average Order Value: PHP {order_revenue.mean():,.2f}")


def highest_value(data: pd.DataFrame) -> None:
    highest_sale = data["Revenue"].max()
    print(f"Highest Sale Revenue: PHP {highest_sale:,.2f}")


def total_products_sold(data: pd.DataFrame) -> None:
    quantity_sold = data["Quantity"].sum()
    print(f"Total Products Sold: {quantity_sold:,.2f}")


def show_complete_data(data: pd.DataFrame) -> None:
    import matplotlib.pyplot as plt

    product_revenue = data.groupby("Product", sort=False)["Revenue"].sum()
    products = product_revenue.index.astype(str).to_numpy()
    revenues = product_revenue.to_numpy(dtype="float64")

    figure, axis = plt.subplots(figsize=(10, 6))
    bars = axis.bar(products, revenues)
    for bar, revenue in zip(bars, revenues):
        axis.annotate(
            f"PHP {revenue:,.0f}",
            (bar.get_x() + bar.get_width() / 2, bar.get_height()),
            xytext=(0, 3),
            textcoords="offset points",
            ha="center",
            va="bottom",
        )

    axis.set_title("Store Sales Analyzer")
    axis.set_xlabel("Products")
    axis.set_ylabel("Revenue (PHP)")
    axis.tick_params(axis="x", labelrotation=45)
    axis.grid(axis="y", linestyle="--", alpha=0.5)
    axis.set_axisbelow(True)
    figure.tight_layout()
    plt.show()
    plt.close(figure)


def main() -> None:
    data = load_sales_data()
    actions = {
        "1": display_sales,
        "2": calculate_revenue,
        "3": total_revenue,
        "4": best_selling_product,
        "5": most_revenue,
        "6": average_order,
        "7": highest_value,
        "8": total_products_sold,
        "9": show_complete_data,
    }
    menu = (
        "\n"
        + "*" * 57
        + "\n                    SALES ANALYZER\n"
        + "*" * 57
        + "\n1. Display Sales"
        + "\n2. Calculate Revenue"
        + "\n3. View Total Revenue"
        + "\n4. Best-Selling Product"
        + "\n5. Category with Most Revenue"
        + "\n6. Average Order Value"
        + "\n7. Highest Sale Revenue"
        + "\n8. Total Products Sold"
        + "\n9. Show Complete Data (Chart)"
        + "\n10. Exit"
        + "\n"
        + "*" * 57
    )

    while True:
        print(menu)
        choice = input("Enter your choice (1-10): ").strip()

        if choice == "10":
            confirm = input("Are you sure you want to exit? (Y/N): ").strip().upper()
            if confirm == "Y":
                print("Exiting the program.")
                break
            print("Returning to the menu.")
            continue

        action = actions.get(choice)
        if action is None:
            print("Invalid choice. Please enter a number from 1 to 10.")
            continue
        action(data)


if __name__ == "__main__":
    main()
