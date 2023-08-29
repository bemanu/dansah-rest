echo "BUILD START INSTALLING REQUIREMENTS"
python3.9 -m pip install -r requirements.txt

echo "Collect static files"
python3 manage.py collectstatic


echo "BUILD END"