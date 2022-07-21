# by: apolzek
killbyport() { kill -9 $(lsof -t -i:$1) ; }
