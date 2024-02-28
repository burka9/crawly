print() {
	echo -e "\n---------------------------------------"
	echo "$1"
	echo -e "---------------------------------------\n"
}


# Create the spider
print "Creating spider $spider_name for $url"
python entry.py $spider_name $url
print "Spider $spider_name created successfully"


# Run the spider
print "Running spider $spider_name"
scrapy crawl $spider_name
print "Spider $spider_name ran successfully"

