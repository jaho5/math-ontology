import streamlit as st
import pandas as pd
from database import connect_to_db, list_tables, get_table_schema, get_table_data, execute_query

def main():
    st.title("SQLite Database Viewer")
    
    # Database connection
    db_path = st.sidebar.text_input("Database Path", "data/sample.db")
    conn = connect_to_db(db_path)
    
    # List tables
    tables = list_tables(conn)
    
    # Operations
    operation = st.sidebar.radio("Operation", ["View Table", "Join Tables"])
    
    if operation == "View Table":
        display_table(conn, tables)
    else:
        display_join_interface(conn, tables)

def display_table(conn, tables):
    selected_table = st.selectbox("Select Table", tables)
    
    if selected_table:
        # Display schema
        st.subheader("Table Schema")
        schema = get_table_schema(conn, selected_table)
        st.dataframe(schema)
        
        # Display data
        st.subheader("Table Data")
        data = get_table_data(conn, selected_table)
        st.dataframe(data)

def display_join_interface(conn, tables):
    st.subheader("Join Tables")
    
    col1, col2 = st.columns(2)
    
    with col1:
        table1 = st.selectbox("First Table", tables, key="table1")
        if table1:
            schema1 = get_table_schema(conn, table1)
            join_columns1 = schema1['name'].tolist()
            join_column1 = st.selectbox("Join Column (First Table)", join_columns1)
    
    with col2:
        table2 = st.selectbox("Second Table", tables, key="table2")
        if table2:
            schema2 = get_table_schema(conn, table2)
            join_columns2 = schema2['name'].tolist()
            join_column2 = st.selectbox("Join Column (Second Table)", join_columns2)
    
    join_type = st.selectbox("Join Type", ["INNER JOIN", "LEFT JOIN", "RIGHT JOIN", "FULL OUTER JOIN"])
    
    if st.button("Execute Join"):
        perform_join(conn, table1, table2, join_column1, join_column2, join_type)

def perform_join(conn, table1, table2, join_column1, join_column2, join_type):
    # Get schemas to handle column names properly
    schema1 = get_table_schema(conn, table1)
    schema2 = get_table_schema(conn, table2)
    
    # Create column selection with table prefixes to avoid duplicate column names
    columns1 = [f'{table1}.{col} AS {table1}_{col}' for col in schema1['name']]
    columns2 = [f'{table2}.{col} AS {table2}_{col}' for col in schema2['name']]
    
    all_columns = columns1 + columns2
    column_selection = ",\n        ".join(all_columns)
    
    query = f"""
    SELECT 
        {column_selection}
    FROM {table1}
    {join_type} {table2}
    ON {table1}.{join_column1} = {table2}.{join_column2}
    """
    
    try:
        result = execute_query(conn, query)
        st.subheader("Join Result")
        st.dataframe(result)
    except Exception as e:
        st.error(f"Error executing join: {e}")

if __name__ == "__main__":
    main()
