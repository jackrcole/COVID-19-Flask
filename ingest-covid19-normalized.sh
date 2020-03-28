# Crude script that pulls the csv and replaces the old one
# Runs daily as a cron job

wget -r -A.csv https://data.beta.nyc/dataset/covid-19-time-series/resource/3d4caf81-7ec0-4112-9700-62ca7364d6bf
mv data.beta.nyc/dataset/ba0dfde7-3a58-4baa-930f-9f27b25b678c/resource/3d4caf81-7ec0-4112-9700-62ca7364d6bf/download/covid19_normalized.csv covid19_normalized.csv
rm -rf data.beta.nyc
git add covid19_normalized.csv
git commit -m "Updated data"
git push origin master