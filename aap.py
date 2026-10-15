import streamlit as st
from Mera_Matrix import Matrix


# Display matrix values in bordered blocks
def display_matrix(matrix):
    for row in matrix.data:
        cols = st.columns(len(row))

        for j, value in enumerate(row):
            with cols[j]:
                st.markdown(
                    f"""
                    <div style="
                        border: 2px solid #4CAF50;
                        border-radius: 12px;
                        padding: 20px;
                        text-align: center;
                        font-size: 24px;
                        font-weight: bold;
                        margin: 5px 0;
                    ">
                        {value}
                    </div>
                    """,
                    unsafe_allow_html=True
                )


# App heading
st.title("🔢 MatrixLab")
st.subheader("Matrix Operations from Scratch")
st.caption("Built with Python • OOP • Linear Algebra")


# Select operation
st.sidebar.header("⚙️ Operations")
operation = st.sidebar.selectbox(
    "Choose an operation",
    [
        "Addition",
        "Subtraction",
        "Multiplication",
        "Transpose",
        "Determinant"
    ]
)


# Matrix A dimensions
st.subheader("Matrix A")
col1, col2 = st.columns(2)

with col1:
    row_a = st.number_input(
        "Rows",
        min_value=1,
        max_value=10,
        value=2,
        step=1,
        key="rows_a"
    )

with col2:
    cols_a = st.number_input(
        "Columns",
        min_value=1,
        max_value=10,
        value=2,
        step=1,
        key="cols_a"
    )


# Matrix A values: keyboard input
matrix_a_data = []
st.write("Enter values for Matrix A:")

for i in range(int(row_a)):
    row = []
    columns = st.columns(int(cols_a))

    for j in range(int(cols_a)):
        value = columns[j].text_input(
            f"A[{i}][{j}]",
            value="0",
            key=f"A_{i}_{j}"
        )

        try:
            number = int(value) if value.strip() not in ("", "-") else 0
        except ValueError:
            st.error(f"A[{i}][{j}] must be a whole number.")
            number = 0

        row.append(number)

    matrix_a_data.append(row)


A = Matrix(int(row_a), int(cols_a))
A.data = matrix_a_data


# Matrix B for operations that need two matrices
if operation in ["Addition", "Subtraction", "Multiplication"]:
    st.subheader("Matrix B")

    col1, col2 = st.columns(2)

    with col1:
        rows_b = st.number_input(
            "Rows",
            min_value=1,
            max_value=10,
            value=2,
            step=1,
            key="rows_b"
        )

    with col2:
        cols_b = st.number_input(
            "Columns",
            min_value=1,
            max_value=10,
            value=2,
            step=1,
            key="cols_b"
        )

    matrix_b_data = []
    st.write("Enter values for Matrix B:")

    for i in range(int(rows_b)):
        row = []
        columns = st.columns(int(cols_b))

        for j in range(int(cols_b)):
            value = columns[j].text_input(
                f"B[{i}][{j}]",
                value="0",
                key=f"B_{i}_{j}"
            )

            try:
                number = int(value) if value.strip() not in ("", "-") else 0
            except ValueError:
                st.error(f"B[{i}][{j}] must be a whole number.")
                number = 0

            row.append(number)

        matrix_b_data.append(row)

    B = Matrix(int(rows_b), int(cols_b))
    B.data = matrix_b_data


# Calculate result
st.divider()
if st.button("✨ Calculate Result"):

    if operation == "Addition":
        if row_a == rows_b and cols_a == cols_b:
            result = A.addition(B)

            st.subheader("➕ Addition Result")
            display_matrix(result)
        else:
            st.error(
                "Addition requires both matrices to have the same dimensions."
            )

    elif operation == "Subtraction":
        if row_a == rows_b and cols_a == cols_b:
            result = A.subtraction(B)

            st.subheader("➖ Subtraction Result")
            display_matrix(result)
        else:
            st.error(
                "Subtraction requires both matrices to have the same dimensions."
            )

    elif operation == "Multiplication":
        if cols_a == rows_b:
            result = A.multiplication(B)

            st.subheader("✖️ Multiplication Result")
            display_matrix(result)
        else:
            st.error(
                "For multiplication, columns of Matrix A must equal "
                "rows of Matrix B."
            )

    elif operation == "Transpose":
        result = A.transpose()

        st.subheader("🔄 Transpose of Matrix A")
        display_matrix(result)

    elif operation == "Determinant":
        if row_a == cols_a:
            result = A.determinant()

            st.subheader("📐 Determinant of Matrix A")
            st.success(f"Determinant = {result}")
        else:
            st.error(
                "Determinant is only defined for a square matrix."
            )
