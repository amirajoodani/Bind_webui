#!/bin/bash

cat /etc/bind/*.db | grep -E "^[[:alnum:]]"
