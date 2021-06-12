run: final text
	mv today_info.html /var/www/html

final: text
	today_info > today_info.html
	
text:	
	python today.py
