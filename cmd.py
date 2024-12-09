------------------------------------------------------------------------------------
Following are some important commands you can use on the local machine and AWS EC2:-

         ----------- Local Machine -------------------------

conda create -p env python=3.8 -y

source activate ./env

clear

git status

ls -a

pip install ipykernel

git add .

git commit -m 'all files added'

git push

pip install -r requirements.txt

python setup.py install

streamlit run StreamlitApp.py

        --------------------- AWS EC2 -------------------------------

sudo apt update

sudo apt upgrade -y

sudo apt install git curl unzip tar make sudo vim wget -y

git clone "repo"

ls 

cd select folder

sudo apt install python3-pip

pip3 install -r requirements.txt

python3 -m streamlit run StreamlitApp.py

          ---------------
## add & access openai_key => 

create .env file = touch .env # creating folder as .env
                 = ls -a # add files
                 = vi .env # opening file
                 = :wq # for exit()
                 = cat .env # reading
                 
and insert copy openai_key & esc key & :wq --> hit enter 

---------------
