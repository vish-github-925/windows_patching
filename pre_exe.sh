#!/bin/bash
export ANSIBLE_LOG_PATH=logs/`date +%Y-%m-%dT%H-%M-%S`.log
ansible-playbook get_hostname_serial.yaml
export ANSIBLE_LOG_PATH=logs/`date +%Y-%m-%dT%H-%M-%S`.log
ansible-playbook -i ser_par_inv.ini ser_par_playbook.yaml
