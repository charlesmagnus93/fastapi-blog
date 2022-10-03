# start virtuel env
    source blogApi-env/Scripts/activate

# Install packages
    pip install -r requirements.txt

# start app
    uvicorn main:app