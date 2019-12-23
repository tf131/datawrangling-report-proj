#setting up WSL2 for accessing mongoDB Cluster
#Ubuntu-18.04:
$ echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.0 multiverse" \
    | sudo tee /etc/apt/sources.list.d/mongodb-org-4.0.list

sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \
    --recv 9DA31620334BD75D9DCB49F368818C72E52529D4
sudo apt update
sudo apt-get install -y mongodb-org-shell
sudo apt-get install -y mongodb-org-tools


#download tsv bereinigt
wget https://hpi.de/fileadmin/user_upload/fachgebiete/naumann/projekte/repeatability/Restaurants/restaurants_NDPL.tsv
#import bereinigt data
mongoimport --uri "mongodb+srv://tim:fxPgQrWtKb8MY2x5FtkY@cluster4report-dmdb-4pvyi.mongodb.net/restaurants?retryWrites=true&w=majority" --collection restaurants_non_duplicates --type tsv --drop --file restaurants_NDPL.tsv --headerline



#download tsv
wget https://hpi.de/fileadmin/user_upload/fachgebiete/naumann/projekte/repeatability/Restaurants/restaurants.tsv
#import root data
mongoimport --uri "mongodb+srv://tim:fxPgQrWtKb8MY2x5FtkY@cluster4report-dmdb-4pvyi.mongodb.net/restaurants?retryWrites=true&w=majority" --collection restaurants_untouched --type tsv --drop --file restaurants.tsv --headerline

#download tsv bereinigt
wget https://hpi.de/fileadmin/user_upload/fachgebiete/naumann/projekte/repeatability/Restaurants/restaurants_DPL.tsv
#import bereinigt data
mongoimport --uri "mongodb+srv://tim:fxPgQrWtKb8MY2x5FtkY@cluster4report-dmdb-4pvyi.mongodb.net/restaurants?retryWrites=true&w=majority" --collection restaurants_duplicates --type tsv --drop --file restaurants_DPL.tsv --headerline

#mongodump
mongodump --uri "mongodb+srv://tim:fxPgQrWtKb8MY2x5FtkY@cluster4report-dmdb-4pvyi.mongodb.net/restaurants?retryWrites=true&w=majority"