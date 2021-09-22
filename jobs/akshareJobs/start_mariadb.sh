#!/bin/sh

DATE=`date +%Y-%m-%d:%H:%M:%S`
echo $DATE

if [ ! -d "/data/stockdb" ]; then
    mkdir -p /data/stockdb
    /usr/bin/mysql_install_db
fi


/usr/bin/mysqld_safe >> /data/logs/start_stockdb.log