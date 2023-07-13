echo "BUILD START"
python3 -m pip install -r requirements.txt
python3 maanger.py collectstatic --noinput --clear
echo "BUILD END"