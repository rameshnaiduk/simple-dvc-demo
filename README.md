create env

'''bash
conda create -n wineq python=3.9.5 -y
'''

activate env
'''bash
conda activate wineq
'''

create a req file

install the requirements

'''bash
pip install -r requirements.txt
'''

download the dataset
'''bash
https://drive.google.com/drive/folders/18zqQiCJVgF7uzXgfbIJ-04zgz1ItNfF5
'''

'''bash
git init
dvc init
dvc add data_given/winequality.csv
git add . && git commit -m "param added'
git push origin main
'''