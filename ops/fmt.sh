echo -e "\nRuff Fixing linting issues"
ruff check app/ --fix
echo -e "\nRuff Fixing formatting issues"
ruff format app/