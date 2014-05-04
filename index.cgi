#!/bin/sh
#
# Content negotiation for PiClass website
#

IFS=","
for lang in $HTTP_ACCEPT_LANGUAGE
do
	lang=${lang%;*} lang=${lang# } lang=${lang%-*}
	[ -f "index.${lang}.html" ] &&  break
done
unset IFS
[ -f "index.${lang}.html" ] || lang="en"

echo "Location: index.${lang}.html"
echo ""

exit 0
