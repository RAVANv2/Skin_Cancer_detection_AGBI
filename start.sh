#!/bin/bash
uwsgi malonoma_app.ini --protocol=http --socket=0.0.0.0:5005 --lazy --pidfile process.pid -w wsgi &
echo "Service Started!"
