# Create root project folder
$projectName = "QuantumSeminarCompanion"
New-Item -ItemType Directory -Path $projectName
Set-Location $projectName

# Create core folders
$folders = @("components", "data", "pages", "utils", "assets", "tests")
foreach ($folder in $folders) {
    New-Item -ItemType Directory -Path $folder
}

# Create main app file
New-Item -ItemType File -Path "app.py"

# Create requirements.txt
@"
streamlit
pandas
numpy
matplotlib
plotly
scikit-learn
"@ | Set-Content -Path "requirements.txt"

# Create .gitignore
@"
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# Virtual environment
venv/
.env/

# Streamlit cache
.streamlit/

# Logs
*.log

# OS files
.DS_Store
Thumbs.db
"@ | Set-Content -Path ".gitignore"

# Create sample files in each folder
New-Item -ItemType File -Path "components/__init__.py"
New-Item -ItemType File -Path "components/sidebar.py"
New-Item -ItemType File -Path "data/questions.json"
New-Item -ItemType File -Path "pages/01_Home.py"
New-Item -ItemType File -Path "pages/02_QuantumExplorer.py"
New-Item -ItemType File -Path "utils/helpers.py"
New-Item -ItemType File -Path "assets/README.md"
New-Item -ItemType File -Path "tests/test_helpers.py"

Write-Host "✅ Streamlit project '$projectName' created successfully!"
