#!usr/bin/bash

gunicorn \
    --bind 0.0.0.0:8080 \
    --workers 7 \
    --log-level=debug \
<<<<<<< HEAD
    --timeout 600 property.wsgi:application
=======
    --timeout 600 csa.wsgi:application
>>>>>>> 4cf109ac867bfbd42d10c5920a81da7dec556e6d
