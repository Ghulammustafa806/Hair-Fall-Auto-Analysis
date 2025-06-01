import os
import pandas as pd
import nbformat
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell
import webbrowser

# =============================================
# 1. PATH CONFIGURATION
# =============================================
FOLDER_PATH = r"C:\Users\GHULAM MUSTAFA\Desktop\automatic system"
CSV_FILE = os.path.join(FOLDER_PATH, "Hair_Fall_Sensor_Dataset.csv")
NOTEBOOK_NAME = os.path.join(FOLDER_PATH, "Hair_Fall_Analysis.ipynb")

# =============================================
# 2. NOTEBOOK CREATION FUNCTION
# =============================================
def create_analysis_notebook():
    # Initialize notebook
    nb = new_notebook()
    
    # Cell 1: Header and Imports (using ASCII-only characters)
    nb.cells.append(new_markdown_cell("# Hair Fall Sensor Analysis"))
    nb.cells.append(new_code_cell("""\
# Essential imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

print("Libraries loaded successfully!")"""))

    # Cell 2: Data Loading
    nb.cells.append(new_markdown_cell("## 1. Data Loading"))
    nb.cells.append(new_code_cell(f"""\
try:
    df = pd.read_csv(r'{CSV_FILE}')
    print(f"Data loaded successfully! Shape: {{df.shape}}")
    print("\\nFirst 3 rows:")
    df.head(3)
except Exception as e:
    print(f"Error loading data: {{str(e)}}")
    raise"""))

    # Cell 3: Sensor Analysis
    nb.cells.append(new_markdown_cell("## 2. Sensor Distribution"))
    nb.cells.append(new_code_cell("""\
# Sensor ID analysis
print("Sensor Value Counts:")
print(df['sensor_id'].value_counts())

plt.figure(figsize=(10,5))
sns.countplot(data=df, x='sensor_id', order=df['sensor_id'].value_counts().index)
plt.title("Sensor Distribution")
plt.xticks(rotation=45)
plt.show()"""))

    # Cell 4: Numerical Features
    nb.cells.append(new_markdown_cell("## 3. Numerical Features"))
    nb.cells.append(new_code_cell("""\
# Create subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle("Numerical Features Distribution")

# Plot distributions
sns.histplot(data=df, x='motion', kde=True, ax=axes[0, 0])
sns.histplot(data=df, x='temperature', kde=True, ax=axes[0, 1])
sns.histplot(data=df, x='distance', kde=True, ax=axes[1, 0])

# Correlation heatmap
corr = df[['motion','temperature','distance']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', ax=axes[1, 1])
plt.tight_layout()
plt.show()"""))

    # Cell 5: Label Analysis
    nb.cells.append(new_markdown_cell("## 4. Label Distribution"))
    nb.cells.append(new_code_cell("""\
# Label analysis
print("Label Distribution:")
print(df['label'].value_counts())

plt.figure(figsize=(8,6))
plt.pie(df['label'].value_counts(), 
        labels=['No Hair Fall', 'Hair Fall'], 
        autopct='%1.1f%%',
        startangle=90)
plt.title("Hair Fall Detection Labels")
plt.show()"""))

    # Save notebook with UTF-8 encoding
    with open(NOTEBOOK_NAME, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)
    
    return NOTEBOOK_NAME

# =============================================
# 3. MAIN EXECUTION
# =============================================
if __name__ == "__main__":
    print("Starting automated analysis...")
    print(f"Working directory: {os.getcwd()}")
    print(f"Looking for CSV at: {CSV_FILE}")
    
    try:
        if not os.path.exists(CSV_FILE):
            raise FileNotFoundError(f"CSV file not found at: {CSV_FILE}")
        
        print("Creating analysis notebook...")
        notebook_path = create_analysis_notebook()
        
        print(f"Success! Notebook created at:\n{notebook_path}")
        print("Opening in VS Code...")
        webbrowser.open(f"vscode://file/{notebook_path}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
        print("\nTroubleshooting tips:")
        print("1. Verify CSV file exists")
        print("2. Check file permissions")
        print("3. Ensure Python has write access to the folder")