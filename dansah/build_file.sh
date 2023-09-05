echo "BUILD START INSTALLING REQUIREMENTS"
python3.9 -m pip install -r requirements.txt

python3 manage.py makemigration --noinput
python3 manage.py migrate --noinput
echo "Collect static files"
python3 manage.py collectstatic --noinput --clear


echo "BUILD END"