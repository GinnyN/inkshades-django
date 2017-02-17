[program:inkshades2]
command = /vagrant/gunicorn.sh                                         ; Command to start app
directory = /vagrant/
user = root
stdout_logfile = gunicorn_supervisor.log                                                            ; User to run as
redirect_stderr = true                                                ; Save stderr in the same log
environment=LANG=en_US.UTF-8,LC_ALL=en_US.UTF-8                       ; Set UTF-8 as default encoding