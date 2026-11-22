param(
    [string]$Message = "chore: update study hub"
)

$ErrorActionPreference = "Stop"

python scripts/import_official_2025.py
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

python scripts/export_db.py
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

python scripts/generate_lessons.py
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

python -m unittest discover -s tests -v
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

node --test tests/*.test.mjs
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

git status
$changes = git status --porcelain
if ($changes) {
    git add .
    git commit -m $Message
    git push origin main
} else {
    Write-Host "Working tree clean. Nothing to commit."
}
