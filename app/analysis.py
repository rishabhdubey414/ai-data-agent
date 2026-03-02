def analyze(df, query: str):
    q = query.lower()

    if "total sales" in q:
        return f"Total sales = {df['sales'].sum()}"

    if "average sales" in q:
        return f"Average sales = {df['sales'].mean()}"

    if "top product" in q:
        top = df.groupby("product")["sales"].sum().idxmax()
        return f"Top product = {top}"

    return "No structured metric found"