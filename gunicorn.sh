#!/bin/bash
sudo gunicorn inkshades2.wsgi:application --bind=unix:/tmp/gunicorn.socket
